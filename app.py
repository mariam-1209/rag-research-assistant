import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Research Studio", layout="wide", initial_sidebar_state="expanded")

# Load CSS from file — avoids Streamlit dumping it as text
def load_css():
    with open("style.css") as f:
        st.markdown(f"<link href='https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600;700&display=swap' rel='stylesheet'><style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

if 'messages'       not in st.session_state: st.session_state.messages       = []
if 'docs_processed' not in st.session_state: st.session_state.docs_processed = False
if 'rag_engine'     not in st.session_state: st.session_state.rag_engine     = None

# ── SIDEBAR ──
with st.sidebar:
    st.markdown('<div class="brand"><div class="bhex">⬡</div><div><div class="bname">Research Studio</div><div class="bsub">Academic Intelligence</div></div></div>', unsafe_allow_html=True)

    st.markdown('<div class="slabel">Document Upload</div>', unsafe_allow_html=True)
    uploaded_files = st.file_uploader("PDF", type=['pdf'], accept_multiple_files=True, label_visibility="collapsed")

    st.markdown('<div class="slabel">API Key</div>', unsafe_allow_html=True)
    st.markdown("<div style='padding:0 1rem'>", unsafe_allow_html=True)
    groq_key = st.text_input("k", type="password", placeholder="gsk_••••••••••••", label_visibility="collapsed")
    if groq_key: os.environ["GROQ_API_KEY"] = groq_key
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='padding:.5rem 1rem 0'>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Index", key="idx"):
            if not groq_key: st.error("API key required")
            elif not uploaded_files: st.error("Upload PDF first")
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
                        st.success(f"✓ {chunks} chunks")
                        st.rerun()
                    except Exception as e: st.error(str(e))
    with c2:
        if st.button("Clear", key="clr"):
            st.session_state.messages=[]; st.session_state.docs_processed=False; st.session_state.rag_engine=None
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='padding:.5rem 1rem 0'>", unsafe_allow_html=True)
    cls = "spill on" if st.session_state.docs_processed else "spill"
    lbl = "Corpus Ready" if st.session_state.docs_processed else "Awaiting Input"
    st.markdown(f'<div class="{cls}"><span class="dot"></span>{lbl}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""<div style="margin-top:.5rem">
    <div class="nitem on"><span>☁</span>Upload Documents</div>
    <div class="nitem"><span>⬡</span>API Configuration</div>
    <div class="nitem"><span>◫</span>Session Index</div>
    <div class="nitem"><span>⚡</span>Live Research</div>
    </div>""", unsafe_allow_html=True)

    if st.session_state.messages:
        st.markdown("<div style='padding:.5rem 1rem 0'>", unsafe_allow_html=True)
        c1,c2=st.columns(2)
        with c1: st.metric("Queries",  len([m for m in st.session_state.messages if m['role']=='user']))
        with c2: st.metric("Answers",  len([m for m in st.session_state.messages if m['role']=='assistant']))
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown('<div class="prof"><div class="pav">MN</div><div><div class="pname">Mariam Noorani</div><div class="prole">Research Assistant</div></div><div style="margin-left:auto;color:#444;cursor:pointer">⚙</div></div>', unsafe_allow_html=True)

# ── MAIN ──
st.markdown('<div class="topbar"><div class="ttitle">Personal Research Assistant</div></div>', unsafe_allow_html=True)
st.markdown('<div class="cwrap">', unsafe_allow_html=True)

if not st.session_state.messages:
    if st.session_state.docs_processed:
        st.markdown('<div class="estate"><div class="ebox">✦</div><div class="etitle">Corpus Indexed.<br>Begin Your Inquiry.</div><div class="esub">Ask anything about your documents below.</div></div>', unsafe_allow_html=True)
    else:
        st.markdown("""<div class="estate">
<div class="ebox">✦✦</div>
<div class="etitle">How Can I Assist Your<br>Inquiry Today?</div>
<div class="esub">Synthesize complex datasets, extract critical insights from academic papers,<br>or generate technical summaries in real-time.</div>
</div>
<div class="srow">
<div class="sc"><div class="sn">Step 01</div><div class="si">🔑</div><div class="sh">Configure API</div><div class="sb2">Establish connection to the Groq inference engine via your secure API key.</div></div>
<div class="sc"><div class="sn">Step 02</div><div class="si">☁</div><div class="sh">Upload Documents</div><div class="sb2">Ingest academic PDFs or technical manuals for the assistant to index.</div></div>
<div class="sc"><div class="sn">Step 03</div><div class="si">⚡</div><div class="sh">Index &amp; Inquiry</div><div class="sb2">Query the local knowledge base and receive precise, sourced responses.</div></div>
</div>""", unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg['role']=='user':
        st.markdown(f'<div class="mwrap muser"><div><div class="mbub">{msg["content"]}</div><div class="mmeta">You</div></div></div>', unsafe_allow_html=True)
    else:
        srcs=msg.get('sources',[])
        chips="".join(f'<span class="srcc">Source {i+1}</span>' for i,_ in enumerate(srcs))
        src_html=f'<div class="srcrow"><span class="srclbl">◦ {len(srcs)} citation(s)</span>{chips}</div>' if srcs else ""
        st.markdown(f'<div class="mwrap"><div class="atag">⬡ Academic Synthesis</div><div class="abub">{msg["content"]}{src_html}</div></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

prompt = st.chat_input("Ask a question..." if st.session_state.docs_processed else "Index a document first...", disabled=not st.session_state.docs_processed)
if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.spinner("Synthesizing..."):
        try:
            r,s=st.session_state.rag_engine.query(prompt)
            st.session_state.messages.append({"role":"assistant","content":r,"sources":s})
        except Exception as e:
            st.session_state.messages.append({"role":"assistant","content":f"Error: {e}","sources":[]})
    st.rerun()

st.markdown('<div class="foot"><div><div class="fmade">Made by</div><div class="fname">Mariam Noorani</div></div><div class="flinks"><div class="flink">Documentation</div><div class="flink">License</div></div></div>', unsafe_allow_html=True)
