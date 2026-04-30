# 🔍 Intelligent Document Q&A System (RAG Application)

An AI-powered PDF Question & Answer system that lets you upload documents and get precise, source-grounded answers using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📄 Upload documents (PDF) and ask questions in plain natural language
- 🧠 RAG pipeline — answers are strictly grounded in your document content (no hallucinations)
- 🔎 Semantic vector search using ChromaDB for accurate chunk retrieval
- 💬 Chat history management with conversational context
- 📤 Export conversations for reference
- ⚡ Real-time responses powered by Llama 3.2 via Ollama

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python, Flask |
| LLM Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | HuggingFace Transformers |
| LLM Model | Ollama (Llama 3.2) |
| PDF Processing | PyPDF |

---

## 📁 Project Structure

```
rag-research-assistant/
├── app.py              # Main Streamlit application
├── rag_engine.py       # Core RAG pipeline logic
├── simple_app.py       # Lightweight version of the app
├── test_app.py         # Unit tests
├── requirements.txt    # Project dependencies
└── README.md
```

---

## ⚙️ How It Works

1. **Upload** — User uploads a PDF document
2. **Chunking** — Document is split into smaller, manageable chunks
3. **Embedding** — Each chunk is converted into vector embeddings using HuggingFace
4. **Storage** — Embeddings are stored in ChromaDB vector database
5. **Query** — User asks a question; the system finds the most relevant chunks
6. **Generation** — Llama 3.2 generates an answer grounded strictly in retrieved chunks
7. **Response** — Answer is displayed with source citations

---

## 📦 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/mariam-1209/rag-research-assistant.git
cd rag-research-assistant

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install Ollama and pull the model
# Download Ollama from https://ollama.com
ollama pull llama3.2
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`

---

## 💡 Key Implementation Highlights

- **Hallucination-free answers** — LLM responses are anchored strictly to retrieved document chunks, not general training knowledge
- **Semantic search** — ChromaDB enables similarity-based retrieval far beyond simple keyword matching
- **Modular design** — RAG logic is separated into `rag_engine.py` for clean, reusable architecture
- **Lightweight mode** — `simple_app.py` available for low-resource environments

---

## 🔮 Future Improvements

- [ ] Support for DOCX and TXT file formats
- [ ] Multi-document upload and cross-document Q&A
- [ ] Per-response confidence scoring
- [ ] Source highlighting in the UI
- [ ] Deploy on Streamlit Cloud

---

## 👩‍💻 Author

**Mariam Noorani**  
B.E. Computer Science & Engineering — Malnad College of Engineering, Hassan  
📧 mariamnoorani00@gmail.com  
🔗 [GitHub](https://github.com/mariam-1209)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
