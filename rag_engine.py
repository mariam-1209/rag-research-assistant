from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from groq import Groq
import os

class RAGEngine:
    def __init__(self):
        print("Initializing RAG Engine...")
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'},
            encode_kwargs={'normalize_embeddings': True}
        )
        self.vectorstore = None
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        print("RAG Engine initialized!")
        
    def process_documents(self, pdf_paths):
        print(f"Processing {len(pdf_paths)} documents...")
        all_splits = []
        
        for pdf_path in pdf_paths:
            print(f"Loading: {pdf_path}")
            try:
                loader = PyPDFLoader(pdf_path)
                documents = loader.load()
                print(f"Loaded {len(documents)} pages")
                
                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=800,
                    chunk_overlap=100
                )
                
                splits = text_splitter.split_documents(documents)
                print(f"Created {len(splits)} chunks")
                all_splits.extend(splits)
                
            except Exception as e:
                print(f"Error: {e}")
                continue
        
        if not all_splits:
            raise Exception("No documents processed!")
        
        print(f"Total chunks: {len(all_splits)}")
        print("Creating database...")
        
        self.vectorstore = Chroma.from_documents(
            documents=all_splits,
            embedding=self.embeddings,
            persist_directory="./chroma_db"
        )
        
        print("Done!")
        return len(all_splits)
    
    def query(self, question):
        if not self.vectorstore:
            return "⚠️ Upload documents first!", []
        
        print(f"Searching for: {question}")
        
        docs = self.vectorstore.similarity_search(question, k=3)
        
        if not docs:
            return "Nothing found in documents.", []
        
        sources = []
        context_parts = []
        
        for i, doc in enumerate(docs, 1):
            context_parts.append(doc.page_content)
            sources.append({
                'content': doc.page_content[:200] + "...",
                'metadata': doc.metadata,
                'relevance': f"Source {i}"
            })
        
        context = "\n\n".join(context_parts)
        
        # Call Groq API
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Answer questions ONLY based on the provided document context. Do not use outside knowledge. Be specific and detailed."
                },
                {
                    "role": "user",
                    "content": f"""Here are excerpts from the uploaded document:

{context}

Question: {question}

Answer based ONLY on the document excerpts above. Be specific:"""
                }
            ],
            temperature=0,
            max_tokens=500
        )
        
        answer = response.choices[0].message.content
        return answer, sources 