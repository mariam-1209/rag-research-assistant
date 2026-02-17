import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Research Assistant", page_icon="📚", layout="wide")

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'docs_processed' not in st.session_state:
    st.session_state.docs_processed = False

st.title("📚 Personal Research Assistant")
st.markdown("Upload your PDFs and ask questions about them using AI!")

with st.sidebar:
    st.header("📄 Upload Documents")
    st.markdown("Upload one or more PDF files to get started")
    
    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=['pdf'],
        accept_multiple_files=True,
        help="Upload research papers, reports, or any PDF documents"
    )
    
    # Show file info
    if uploaded_files:
        total_mb = sum([f.size for f in uploaded_files]) / (1024 * 1024)
        if total_mb > 50:
            st.warning(f"⚠️ Large upload detected: {total_mb:.1f} MB. Processing may take 2-3 minutes.")
        st.caption(f"📁 {len(uploaded_files)} file(s) selected ({total_mb:.2f} MB)")
    
    if st.button("🚀 Process Documents", type="primary"):
        if uploaded_files:
            os.makedirs("data", exist_ok=True)
            pdf_paths = []
            
            total_size = sum([f.size for f in uploaded_files]) / (1024 * 1024)
            st.info(f"📊 Processing {len(uploaded_files)} files ({total_size:.2f} MB)")
            
            for uploaded_file in uploaded_files:
                file_path = f"data/{uploaded_file.name}"
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                pdf_paths.append(file_path)
            
            # Processing with progress
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                from rag_engine import RAGEngine
                
                status_text.text("Loading AI models...")
                progress_bar.progress(20)
                
                if 'rag_engine' not in st.session_state:
                    st.session_state.rag_engine = RAGEngine()
                
                progress_bar.progress(40)
                status_text.text("Processing documents...")
                
                num_chunks = st.session_state.rag_engine.process_documents(pdf_paths)
                
                progress_bar.progress(100)
                status_text.text("Done!")
                
                st.session_state.docs_processed = True
                st.success(f"✅ Processed {len(uploaded_files)} documents into {num_chunks} chunks!")
                
                st.info(f"📈 Document Stats:\n- Files: {len(uploaded_files)}\n- Chunks: {num_chunks}\n- Avg chunks per file: {num_chunks//len(uploaded_files)}")
                
                st.balloons()
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                progress_bar.empty()
                status_text.empty()
        else:
            st.warning("⚠️ Please upload at least one PDF file")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    # Export chat
    if st.session_state.messages and st.button("📥 Export Chat"):
        chat_text = "\n\n".join([f"{msg['role'].upper()}: {msg['content']}" for msg in st.session_state.messages])
        st.download_button(
            label="Download Chat History",
            data=chat_text,
            file_name="chat_history.txt",
            mime="text/plain"
        )
    
    st.divider()
    if st.session_state.docs_processed:
        st.success("✅ Documents ready!")
    else:
        st.info("📝 Upload documents to start")

st.header("💬 Ask Questions")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask anything about your documents...", disabled=not st.session_state.docs_processed):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            try:
                response, sources = st.session_state.rag_engine.query(prompt)
                st.markdown(response)
                
                if sources:
                    with st.expander("📚 Sources Used"):
                        for i, source in enumerate(sources, 1):
                            st.markdown(f"**Source {i}** (Relevance: {source['relevance']})")
                            st.text(source['content'])
                            if 'page' in source['metadata']:
                                st.caption(f"Page: {source['metadata']['page']}")
                            st.divider()
                
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"❌ Error: {str(e)}"
                st.error(error_msg)

if not st.session_state.docs_processed:
    st.info("👈 Upload PDF documents in the sidebar to get started!")
    
    with st.expander("ℹ️ How to Use This App"):
        st.markdown("""
        **Step 1:** Upload one or more PDF files using the sidebar
        
        **Step 2:** Click "🚀 Process Documents" (takes 30-60 seconds first time)
        
        **Step 3:** Ask questions about your documents in the chat!
        
        **Example Questions:**
        - What is this document about?
        - Summarize the main findings
        - What are the key concepts?
        - Explain [specific topic] from the document
        
        **Features:**
        - ✅ Upload multiple PDFs at once
        - ✅ Handles large documents (1000+ pages)
        - ✅ See which parts of documents were used (click "📚 Sources Used")
        - ✅ Export your chat history
        - ✅ 100% local AI (no API costs!)
        """)

# Footer with stats
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Documents Processed", "✅" if st.session_state.docs_processed else "0")
with col2:
    st.metric("Messages", len(st.session_state.messages))
with col3:
    st.metric("AI Model", "Llama 3.2 (Local)") 