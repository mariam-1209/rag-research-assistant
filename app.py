import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Lexis — Research Intelligence",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── INJECT CUSTOM CSS ──────────────────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Fira+Code:wght@300;400;500&family=Outfit:wght@200;300;400;500&display=swap" rel="stylesheet">

<style>
:root {
  --bg:        #07080a;
  --bg2:       #0d0f12;
  --bg3:       #12151a;
  --border:    #1e2330;
  --gold:      #c9a84c;
  --gold2:     #e8c97a;
  --gold-dim:  rgba(201,168,76,0.12);
  --gold-glow: rgba(201,168,76,0.25);
  --text:      #d4cfc8;
  --text-dim:  #6b6560;
  --text-mid:  #9e9890;
  --red:       #c0392b;
  --green:     #27ae60;
}

/* ── WIPE STREAMLIT DEFAULTS ── */
#MainMenu, footer, header { visibility: hidden; }
.stApp { background: var(--bg); }
[data-testid="stSidebar"] {
  background: var(--bg2) !important;
  border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] > div { padding-top: 0 !important; }
section.main > div { padding: 0 !important; max-width: 100% !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── GLOBAL FONT ── */
html, body, * { font-family: 'Outfit', sans-serif; color: var(--text); box-sizing: border-box; }

/* ── SIDEBAR BRAND ── */
.brand {
  padding: 2rem 1.5rem 1.5rem;
  border-bottom: 1px solid var(--border);
  margin-bottom: 1rem;
}
.brand-mark {
  font-family: 'Cormorant Garamond', serif;
  font-size: 2rem;
  font-weight: 300;
  letter-spacing: 0.08em;
  color: var(--gold);
  line-height: 1;
}
.brand-sub {
  font-family: 'Fira Code', monospace;
  font-size: 0.6rem;
  letter-spacing: 0.25em;
  color: var(--text-dim);
  text-transform: uppercase;
  margin-top: 0.3rem;
}

/* ── SIDEBAR SECTION LABEL ── */
.s-label {
  font-family: 'Fira Code', monospace;
  font-size: 0.6rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--text-dim);
  padding: 0 1.5rem;
  margin-bottom: 0.5rem;
}

/* ── STATUS PILL ── */
.status-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-family: 'Fira Code', monospace;
  font-size: 0.65rem;
  letter-spacing: 0.1em;
  padding: 0.25rem 0.75rem;
  border-radius: 99px;
  margin: 0 1.5rem 1rem;
}
.status-pill.ready   { background: rgba(39,174,96,0.12);  color: #27ae60; border: 1px solid rgba(39,174,96,0.3); }
.status-pill.waiting { background: rgba(201,168,76,0.1);  color: var(--gold); border: 1px solid var(--gold-glow); }
.status-pill.dot { width:6px; height:6px; border-radius:50%; background:currentColor; animation: pulse-dot 1.5s infinite; }
@keyframes pulse-dot { 0%,100%{opacity:1} 50%{opacity:0.3} }

/* ── MAIN HEADER ── */
.main-header {
  padding: 1.5rem 2.5rem;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: linear-gradient(180deg, rgba(201,168,76,0.04) 0%, transparent 100%);
}
.main-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.5rem;
  font-weight: 300;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--gold);
}
.powered-badge {
  font-family: 'Fira Code', monospace;
  font-size: 0.6rem;
  letter-spacing: 0.15em;
  color: var(--text-dim);
  border: 1px solid var(--border);
  padding: 0.3rem 0.8rem;
  border-radius: 4px;
}

/* ── CHAT AREA ── */
.chat-area {
  padding: 2rem 3rem;
  min-height: 60vh;
  max-width: 900px;
  margin: 0 auto;
}

/* ── EMPTY STATE ── */
.empty-state {
  text-align: center;
  padding: 5rem 2rem;
  animation: fadeUp 0.8s ease both;
}
.empty-glyph {
  font-family: 'Cormorant Garamond', serif;
  font-size: 4rem;
  color: var(--gold-dim);
  color: var(--gold);
  opacity: 0.3;
  margin-bottom: 1.5rem;
}
.empty-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.8rem;
  font-weight: 300;
  font-style: italic;
  color: var(--text-mid);
  margin-bottom: 0.5rem;
}
.empty-sub {
  font-size: 0.8rem;
  color: var(--text-dim);
  letter-spacing: 0.05em;
  line-height: 1.7;
}

/* ── MESSAGE BUBBLES ── */
.msg-user {
  display: flex;
  justify-content: flex-end;
  margin: 1.5rem 0;
  animation: fadeUp 0.4s ease both;
}
.msg-user-bubble {
  background: var(--gold-dim);
  border: 1px solid rgba(201,168,76,0.2);
  border-radius: 12px 12px 2px 12px;
  padding: 0.9rem 1.2rem;
  max-width: 65%;
  font-size: 0.9rem;
  line-height: 1.6;
  color: var(--text);
}
.msg-time {
  font-family: 'Fira Code', monospace;
  font-size: 0.55rem;
  color: var(--text-dim);
  text-align: right;
  margin-top: 0.3rem;
  letter-spacing: 0.1em;
}

.msg-ai {
  margin: 1.5rem 0;
  animation: fadeUp 0.5s ease both;
}
.msg-ai-label {
  font-family: 'Fira Code', monospace;
  font-size: 0.58rem;
  letter-spacing: 0.2em;
  color: var(--gold);
  text-transform: uppercase;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.6rem;
}
.msg-ai-label::before {
  content: '';
  display: inline-block;
  width: 16px;
  height: 1px;
  background: var(--gold);
  opacity: 0.5;
}
.msg-ai-bubble {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-left: 3px solid var(--gold);
  border-radius: 0 12px 12px 12px;
  padding: 1.2rem 1.5rem;
  font-size: 0.875rem;
  line-height: 1.8;
  color: var(--text);
  font-family: 'Outfit', sans-serif;
  font-weight: 300;
}
.msg-ai-bubble p { margin: 0; }

/* ── SOURCE PILLS ── */
.source-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-top: 0.8rem;
}
.source-pill {
  font-family: 'Fira Code', monospace;
  font-size: 0.58rem;
  letter-spacing: 0.08em;
  padding: 0.2rem 0.6rem;
  border: 1px solid var(--border);
  border-radius: 4px;
  color: var(--text-dim);
  cursor: pointer;
  transition: all 0.2s;
}
.source-pill:hover { border-color: var(--gold); color: var(--gold); }

/* ── INPUT BAR ── */
.input-bar {
  position: sticky;
  bottom: 0;
  background: linear-gradient(0deg, var(--bg) 80%, transparent);
  padding: 1.5rem 3rem 2rem;
  max-width: 900px;
  margin: 0 auto;
}

/* ── ANIMATIONS ── */
@keyframes fadeUp {
  from { opacity:0; transform: translateY(16px); }
  to   { opacity:1; transform: translateY(0); }
}
@keyframes shimmer {
  0%   { background-position: -200% center; }
  100% { background-position: 200% center; }
}

/* ── STREAMLIT WIDGET OVERRIDES ── */
.stTextInput > div > div {
  background: var(--bg2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 8px !important;
  color: var(--text) !important;
}
.stTextInput > div > div:focus-within {
  border-color: var(--gold) !important;
  box-shadow: 0 0 0 2px var(--gold-dim) !important;
}
.stTextInput input {
  font-family: 'Outfit', sans-serif !important;
  font-size: 0.9rem !important;
  color: var(--text) !important;
  background: transparent !important;
}
.stTextInput input::placeholder { color: var(--text-dim) !important; }
.stTextInput label { color: var(--text-dim) !important; font-size: 0.7rem !important; letter-spacing: 0.1em !important; font-family: 'Fira Code', monospace !important; }

/* File uploader */
[data-testid="stFileUploader"] {
  background: var(--bg3) !important;
  border: 1px dashed var(--border) !important;
  border-radius: 10px !important;
  padding: 1rem !important;
  transition: border-color 0.3s !important;
}
[data-testid="stFileUploader"]:hover { border-color: var(--gold) !important; }
[data-testid="stFileUploader"] label { color: var(--text-mid) !important; font-size: 0.75rem !important; }

/* Buttons */
.stButton > button {
  background: linear-gradient(135deg, var(--gold), #a07828) !important;
  color: #07080a !important;
  font-family: 'Fira Code', monospace !important;
  font-size: 0.65rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.2em !important;
  text-transform: uppercase !important;
  border: none !important;
  border-radius: 6px !important;
  padding: 0.6rem 1.5rem !important;
  transition: all 0.3s !important;
  width: 100% !important;
}
.stButton > button:hover {
  transform: translateY(-1px) !important;
  box-shadow: 0 4px 20px var(--gold-glow) !important;
}

/* Chat input */
[data-testid="stChatInput"] {
  background: var(--bg2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
}
[data-testid="stChatInput"]:focus-within { border-color: var(--gold) !important; }
[data-testid="stChatInput"] textarea {
  font-family: 'Outfit', sans-serif !important;
  color: var(--text) !important;
  background: transparent !important;
  font-size: 0.9rem !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: var(--text-dim) !important; }
[data-testid="stChatInput"] button { background: var(--gold) !important; border-radius: 6px !important; }

/* Spinner */
[data-testid="stSpinner"] { color: var(--gold) !important; }

/* Error/success */
.stAlert { border-radius: 8px !important; font-family: 'Fira Code', monospace !important; font-size: 0.75rem !important; }

/* Divider */
hr { border-color: var(--border) !important; margin: 1rem 0 !important; }

/* Metrics */
[data-testid="metric-container"] {
  background: var(--bg2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 8px !important;
  padding: 0.8rem !important;
}
[data-testid="stMetricLabel"] { font-family: 'Fira Code', monospace !important; font-size: 0.6rem !important; letter-spacing: 0.1em !important; color: var(--text-dim) !important; }
[data-testid="stMetricValue"] { font-family: 'Cormorant Garamond', serif !important; font-size: 1.6rem !important; color: var(--gold) !important; }

/* Expander */
[data-testid="stExpander"] {
  background: var(--bg3) !important;
  border: 1px solid var(--border) !important;
  border-radius: 8px !important;
}
[data-testid="stExpander"] summary { font-family: 'Fira Code', monospace !important; font-size: 0.7rem !important; color: var(--text-dim) !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: var(--gold); }
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ──────────────────────────────────────────────────────────────
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'docs_processed' not in st.session_state:
    st.session_state.docs_processed = False
if 'rag_engine' not in st.session_state:
    st.session_state.rag_engine = None

# ── SIDEBAR ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="brand">
      <div class="brand-mark">◈ Lexis</div>
      <div class="brand-sub">Document Intelligence System</div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.docs_processed:
        st.markdown('<div class="status-pill ready"><span class="dot"></span> CORPUS INDEXED</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-pill waiting"><span class="dot"></span> AWAITING DOCUMENT</div>', unsafe_allow_html=True)

    st.markdown('<div class="s-label">API Configuration</div>', unsafe_allow_html=True)
    groq_key = st.text_input("Groq API Key", type="password", placeholder="gsk_...", label_visibility="collapsed")
    if groq_key:
        os.environ["GROQ_API_KEY"] = groq_key

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    st.markdown('<div class="s-label">Document Upload</div>', unsafe_allow_html=True)

    uploaded_files = st.file_uploader(
        "Upload PDF",
        type=['pdf'],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )

    if uploaded_files:
        total_mb = sum([f.size for f in uploaded_files]) / (1024 * 1024)
        st.markdown(f"<div style='font-family:Fira Code,monospace;font-size:0.6rem;color:var(--text-dim);padding:0.3rem 0;letter-spacing:0.1em'>{len(uploaded_files)} FILE(S) · {total_mb:.2f} MB</div>", unsafe_allow_html=True)

    if st.button("◈ INDEX CORPUS"):
        if not groq_key:
            st.error("API key required")
        elif not uploaded_files:
            st.error("Upload at least one PDF")
        else:
            os.makedirs("data", exist_ok=True)
            pdf_paths = []
            for f in uploaded_files:
                path = f"data/{f.name}"
                with open(path, "wb") as out:
                    out.write(f.getbuffer())
                pdf_paths.append(path)

            with st.spinner("Indexing corpus..."):
                try:
                    from rag_engine import RAGEngine
                    if not st.session_state.rag_engine:
                        st.session_state.rag_engine = RAGEngine()
                    chunks = st.session_state.rag_engine.process_documents(pdf_paths)
                    st.session_state.docs_processed = True
                    st.success(f"✓ {chunks} vectors indexed")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    if st.button("⌫ Clear Session"):
        st.session_state.messages = []
        st.session_state.docs_processed = False
        st.session_state.rag_engine = None
        st.rerun()

    # Stats
    if st.session_state.messages:
        st.markdown("<hr>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Queries", len([m for m in st.session_state.messages if m['role'] == 'user']))
        with col2:
            st.metric("Responses", len([m for m in st.session_state.messages if m['role'] == 'assistant']))

    # Footer
    st.markdown("""
    <div style='position:absolute;bottom:1.5rem;left:1.5rem;right:1.5rem'>
      <div style='font-family:Fira Code,monospace;font-size:0.55rem;letter-spacing:0.1em;color:var(--text-dim);text-align:center'>
        BUILT BY <span style='color:var(--gold)'>MARIAM NOORANI</span><br>
        <span style='opacity:0.5'>GROQ · LLAMA-3.3 · FAISS</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── MAIN AREA ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
  <div class="main-title">Personal Research Assistant</div>
  <div class="powered-badge">POWERED BY GROQ + LLaMA-3.3</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="chat-area">', unsafe_allow_html=True)

# Empty state
if not st.session_state.messages:
    if st.session_state.docs_processed:
        st.markdown("""
        <div class="empty-state">
          <div class="empty-glyph">◈</div>
          <div class="empty-title">Corpus is ready.</div>
          <div class="empty-sub">Begin your inquiry below.<br>Ask anything about your documents.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="empty-state">
          <div class="empty-glyph">◈</div>
          <div class="empty-title">Upload a document to begin.</div>
          <div class="empty-sub">
            Index your PDFs using the sidebar.<br>
            Then ask questions in natural language.
          </div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("◦ How to use Lexis"):
            st.markdown("""
            <div style='font-family:Fira Code,monospace;font-size:0.7rem;line-height:2;color:var(--text-mid)'>
            01 · Get a free API key at <a href='https://console.groq.com' style='color:var(--gold)'>console.groq.com</a><br>
            02 · Paste key in the sidebar<br>
            03 · Upload one or more PDFs<br>
            04 · Click "Index Corpus"<br>
            05 · Ask anything about your documents
            </div>
            """, unsafe_allow_html=True)

# Render messages
for msg in st.session_state.messages:
    if msg['role'] == 'user':
        st.markdown(f"""
        <div class="msg-user">
          <div>
            <div class="msg-user-bubble">{msg['content']}</div>
            <div class="msg-time">SENT JUST NOW</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        sources_html = ""
        if msg.get('sources'):
            pills = "".join([f"<span class='source-pill'>◦ SOURCE {i+1}</span>" for i, _ in enumerate(msg['sources'])])
            sources_html = f"<div class='source-row'>{pills}</div>"

        st.markdown(f"""
        <div class="msg-ai">
          <div class="msg-ai-label">SYNTHESIS</div>
          <div class="msg-ai-bubble">
            <p>{msg['content']}</p>
            {sources_html}
          </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── CHAT INPUT ──────────────────────────────────────────────────────────────────
if prompt := st.chat_input(
    "Ask a question about your documents..." if st.session_state.docs_processed else "Index a corpus first...",
    disabled=not st.session_state.docs_processed
):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Synthesizing..."):
        try:
            response, sources = st.session_state.rag_engine.query(prompt)
            st.session_state.messages.append({
                "role": "assistant",
                "content": response,
                "sources": sources
            })
        except Exception as e:
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"Error: {str(e)}",
                "sources": []
            })

    st.rerun()
