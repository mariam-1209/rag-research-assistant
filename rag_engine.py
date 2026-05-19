import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import HumanMessage, AIMessage


class RAGEngine:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"}
        )
        self.vectorstore = None
        self.retriever = None
        self.chat_history = []  # ← memory stored here

        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY not found.")

        self.llm = ChatGroq(
            groq_api_key=groq_api_key,
            model_name="llama-3.3-70b-versatile",
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

        # Reset memory when new doc is loaded
        self.chat_history = []

        return len(chunks)

    def query(self, question: str):
        if not self.retriever:
            raise ValueError("No documents processed yet.")

        # Get relevant docs
        source_docs = self.retriever.invoke(question)
        context = "\n\n".join(doc.page_content for doc in source_docs)

        # Build prompt with memory
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful research assistant. Answer questions based on the provided document context.
If the answer is not in the context, say so clearly.
Be concise and accurate.

Document Context:
{context}"""),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}")
        ])

        chain = prompt | self.llm | StrOutputParser()

        answer = chain.invoke({
            "context": context,
            "chat_history": self.chat_history,
            "question": question
        })

        # Save to memory
        self.chat_history.append(HumanMessage(content=question))
        self.chat_history.append(AIMessage(content=answer))

        # Keep last 10 exchanges (20 messages) to avoid token overflow
        if len(self.chat_history) > 20:
            self.chat_history = self.chat_history[-20:]

        sources = []
        for doc in source_docs:
            sources.append({
                "content": doc.page_content[:300] + "...",
                "metadata": doc.metadata,
                "relevance": "High"
            })

        return answer, sources
