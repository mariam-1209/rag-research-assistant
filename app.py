import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Research Studio", layout="wide", initial_sidebar_state="expanded")

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

if 'messages'       not in st.session_state: st.session_state.messages       = []
if 'docs_processed' not in st.session_state: st.session_state.docs_processed = False
if 'rag_engine'     not in st.session_state: st.session_state.rag_engine     = None

# Load API key from Streamlit secrets silently
groq_key = st.secrets.get("GROQ_API_KEY", "") if hasattr(st, "secrets") else ""
if groq_key:
    os.environ["GROQ_API_KEY"] = groq_key

# ── SIDEBAR ──
with st.sidebar:
    st.markdown("""<div class="brand">
      <div class="bhex">⬡</div>
      <div><div class="bname">Research Studio</div><div class="bsub">Academic Intelligence</div></div>
    </div>""", unsafe_allow_html=True)

    # Upload
    st.markdown('<div class="sb-block"><div class="sb-lbl">Document Upload</div>', unsafe_allow_html=True)
    uploaded_files = st.file_uploader(
        "PDF", type=['pdf'], accept_multiple_files=True, label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # API key — only show if not in secrets
    if not groq_key:
        st.markdown('<div class="sb-block"><div class="sb-lbl">API Key</div>', unsafe_allow_html=True)
        st.markdown("<div style='padding:0'>", unsafe_allow_html=True)
        manual_key = st.text_input("k", type="password", placeholder="gsk_••••••••••••", label_visibility="collapsed")
        if manual_key:
            os.environ["GROQ_API_KEY"] = manual_key
            groq_key = manual_key
        st.markdown("</div></div>", unsafe_allow_html=True)

    # Buttons
    st.markdown("<div style='padding:16px 20px 0;display:flex;gap:8px'>", unsafe_allow_html=True)
    c1, c2 = st.columns([3, 2])
    with c1:
        if st.button("⬡  Index Corpus", key="idx"):
            if not os.environ.get("GROQ_API_KEY"): st.error("API key required")
            elif not uploaded_files: st.error("Upload a PDF first")
            else:
                os.makedirs("data", exist_ok=True)
                paths = []
                for f in uploaded_files:
                    p = f"data/{f.name}"
                    with open(p,"wb") as o: o.write(f.getbuffer())
                    paths.append(p)
                with st.spinner("Indexing..."):
                    try:
                        from rag_engine import RAGEngine
                        if not st.session_state.rag_engine: st.session_state.rag_engine = RAGEngine()
                        chunks = st.session_state.rag_engine.process_documents(paths)
                        st.session_state.docs_processed = True
                        st.success(f"✓ {chunks} chunks indexed")
                        st.rerun()
                    except Exception as e: st.error(str(e))
    with c2:
        if st.button("Clear", key="clr"):
            st.session_state.messages=[]; st.session_state.docs_processed=False; st.session_state.rag_engine=None
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # Status
    st.markdown("<div class='status-wrap'>", unsafe_allow_html=True)
    if st.session_state.docs_processed:
        st.markdown('<div class="status on"><span class="dot"></span>Corpus Ready</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status"><span class="dot"></span>Awaiting Input</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Nav
    st.markdown("""<div class="nav-wrap">
      <div class="nav-item on"><span class="nav-icon">☁</span>Upload Documents</div>
      <div class="nav-item"><span class="nav-icon">⬡</span>API Configuration</div>
      <div class="nav-item"><span class="nav-icon">◫</span>Session Index</div>
      <div class="nav-item"><span class="nav-icon">⚡</span>Live Research</div>
    </div>""", unsafe_allow_html=True)

    # Stats
    if st.session_state.messages:
        st.markdown("<div style='padding:12px 20px 0;display:grid;grid-template-columns:1fr 1fr;gap:8px'>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: st.metric("Queries",   len([m for m in st.session_state.messages if m['role']=='user']))
        with c2: st.metric("Responses", len([m for m in st.session_state.messages if m['role']=='assistant']))
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
    st.markdown("""<div class="prof">
      <div class="pav">MN</div>
      <div><div class="pname">Mariam Noorani</div><div class="prole">Research Assistant</div></div>
      <div style="margin-left:auto;font-size:16px;color:#333;cursor:pointer">⚙</div>
    </div>""", unsafe_allow_html=True)

# ── MAIN ──
st.markdown('<div class="topbar"><div class="ttitle">Personal Research Assistant</div></div>', unsafe_allow_html=True)
st.markdown('<div class="chat-wrap">', unsafe_allow_html=True)

if not st.session_state.messages:
    if st.session_state.docs_processed:
        st.markdown("""<div class="estate">
          <div class="ebox">✦</div>
          <div class="etitle">Ready to answer your questions.</div>
          <div class="esub">Your document has been indexed. Ask anything about it below.</div>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="estate">
          <div class="ebox">✦✦</div>
          <div class="etitle">How can I assist your inquiry today?</div>
          <div class="esub">Upload a PDF, index it, then ask questions in natural language — grounded strictly in your document.</div>
        </div>
        <div class="srow">
          <div class="sc">
            <div class="sn">Step 01</div>
            <div class="si">🔑</div>
            <div class="sh">Configure API</div>
            <div class="sb2">Connect to the Groq inference engine with your free API key from console.groq.com</div>
          </div>
          <div class="sc">
            <div class="sn">Step 02</div>
            <div class="si">📄</div>
            <div class="sh">Upload Your PDF</div>
            <div class="sb2">Drop any research paper, report, or document into the sidebar uploader</div>
          </div>
          <div class="sc">
            <div class="sn">Step 03</div>
            <div class="si">⚡</div>
            <div class="sh">Ask Anything</div>
            <div class="sb2">Ask questions in plain English and get precise, source-cited answers instantly</div>
          </div>
        </div>""", unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg['role'] == 'user':
        st.markdown(f"""<div class="mwrap muser">
          <div class="muser-inner">
            <div class="mbub">{msg['content']}</div>
            <div class="mmeta">You</div>
          </div>
        </div>""", unsafe_allow_html=True)
    else:
        srcs = msg.get('sources', [])
        chips = "".join(f'<span class="srcc">Source {i+1}</span>' for i, _ in enumerate(srcs))
        src_html = f'<div class="srcrow"><span class="srclbl">◦ {len(srcs)} citation(s)</span>{chips}</div>' if srcs else ""
        st.markdown(f"""<div class="mwrap">
          <div class="atag">⬡ Academic Synthesis</div>
          <div class="abub">{msg['content']}{src_html}</div>
        </div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

prompt = st.chat_input(
    "Ask a question about your document..." if st.session_state.docs_processed else "Upload and index a document to get started...",
    disabled=not st.session_state.docs_processed
)
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.spinner("Synthesizing response..."):
        try:
            response, sources = st.session_state.rag_engine.query(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response, "sources": sources})
        except Exception as e:
            st.session_state.messages.append({"role": "assistant", "content": f"Error: {str(e)}", "sources": []})
    st.rerun()

st.markdown("""<div class="foot">
  <div>
    <div class="fmade">Made by</div>
    <div class="fname">Mariam Noorani</div>
  </div>
  <div class="flinks">
    <div class="flink">Documentation</div>
    <div class="flink">License</div>
  </div>
</div>""", unsafe_allow_html=True)
