import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


class RAGEngine:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"}
        )
        self.vectorstore = None
        self.qa_chain = None

        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY not found. Please set it in Streamlit secrets.")

        self.llm = ChatGroq(
            groq_api_key=groq_api_key,
            model_name="llama3-8b-8192",
            temperature=0.1,
            max_tokens=1024
        )

    def process_documents(self, pdf_paths: list) -> int:
        all_docs = []
        for path in pdf_paths:
            loader = PyPDFLoader(path)
            docs = loader.load()
            all_docs.extend(docs)

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = splitter.split_documents(all_docs)

        self.vectorstore = FAISS.from_documents(chunks, self.embeddings)

        prompt_template = """You are a helpful research assistant. Use the following context from the uploaded documents to answer the question accurately and concisely.

If the answer is not found in the context, say "I couldn't find this information in the uploaded documents."

Context:
{context}

Question: {question}

Answer:"""

        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(search_kwargs={"k": 4}),
            chain_type_kwargs={"prompt": prompt},
            return_source_documents=True
        )

        return len(chunks)

    def query(self, question: str):
        if not self.qa_chain:
            raise ValueError("No documents processed yet. Please upload and process PDFs first.")

        result = self.qa_chain({"query": question})
        answer = result["result"]

        sources = []
        for doc in result.get("source_documents", []):
            sources.append({
                "content": doc.page_content[:300] + "...",
                "metadata": doc.metadata,
                "relevance": "High"
            })

        return answer, sources
