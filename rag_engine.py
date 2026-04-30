import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


class RAGEngine:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"}
        )
        self.vectorstore = None
        self.retriever = None
        self.chain = None

        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY not found.")

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
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 4})

        prompt = ChatPromptTemplate.from_template("""
You are a helpful research assistant. Use the following context from the uploaded documents to answer the question accurately and concisely.

If the answer is not found in the context, say "I couldn't find this information in the uploaded documents."

Context:
{context}

Question: {question}

Answer:""")

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        self.chain = (
            {"context": self.retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )

        return len(chunks)

    def query(self, question: str):
        if not self.chain:
            raise ValueError("No documents processed yet.")

        answer = self.chain.invoke(question)

        source_docs = self.retriever.invoke(question)
        sources = []
        for doc in source_docs:
            sources.append({
                "content": doc.page_content[:300] + "...",
                "metadata": doc.metadata,
                "relevance": "High"
            })

        return answer, sources
