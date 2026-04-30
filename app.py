import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Personal Research Assistant",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&family=DM+Mono:wght@300;400;500&display=swap" rel="stylesheet">

<style>
/* ── VARIABLES ── */
:root {
  --bg:          #0a0a0b;
  --sidebar-bg:  #0f0f10;
  --card:        #111113;
  --card2:       #161618;
  --border:      rgba(255,255,255,0.07);
  --border-gold: rgba(201,168,76,0.35);
  --gold:        #C9A84C;
  --gold-hover:  #dbbe6a;
  --gold-muted:  rgba(201,168,76,0.08);
  --text:        #e8e8e8;
  --text-mid:    #888;
  --text-dim:    #444;
  --green:       #3ecf8e;
  --red:         #f87171;
  --radius:      10px;
  --radius-sm:   6px;
  --font:        'DM Sans', sans-serif;
  --mono:        'DM Mono', monospace;
}

/* ── RESET ── */
#MainMenu, footer, header { visibility: hidden; }
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body { font-family: var(--font); background: var(--bg); color: var(--text); }
.stApp { background: var(--bg) !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
  background: var(--sidebar-bg) !important;
  border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] > div:first-child {
  padding: 0 !important;
  display: flex;
  flex-direction: column;
  height: 100vh;
}

/* ── MAIN ── */
section.main > div { padding: 0 !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── SIDEBAR BRAND ── */
.sb-brand {
  padding: 1.75rem 1.5rem 1.5rem;
  border-bottom: 1px solid var(--border);
}
.sb-brand-name {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text);
  letter-spacing: -0.02em;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.sb-brand-dot {
  width: 7px; height: 7px;
  border-radius: 50%;
  background: var(--gold);
  display: inline-block;
  flex-shrink: 0;
}
.sb-brand-sub {
  font-family: var(--mono);
  font-size: 0.62rem;
  color: var(--text-dim);
  letter-spacing: 0.06em;
  margin-top: 0.25rem;
  padding-left: 1.1rem;
}

/* ── STATUS BADGE ── */
.sb-status {
  margin: 1rem 1.5rem 0;
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  font-family: var(--mono);
  font-size: 0.6rem;
  letter-spacing: 0.08em;
  padding: 0.3rem 0.7rem;
  border-radius: 99px;
}
.sb-status.ready   { background: rgba(62,207,142,0.1); color: var(--green); border: 1px solid rgba(62,207,142,0.25); }
.sb-status.idle    { background: rgba(201,168,76,0.08); color: var(--gold);  border: 1px solid rgba(201,168,76,0.2); }
.sb-status .dot { width:5px; height:5px; border-radius:50%; background:currentColor; animation: blink 1.8s ease infinite; }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.2} }

/* ── SIDEBAR SECTION ── */
.sb-section {
  padding: 1.25rem 1.5rem 0;
}
.sb-label {
  font-family: var(--mono);
  font-size: 0.58rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text-dim);
  margin-bottom: 0.6rem;
}

/* ── SIDEBAR FOOTER ── */
.sb-footer {
  margin-top: auto;
  padding: 1.25rem 1.5rem;
  border-top: 1px solid var(--border);
}
.sb-footer-credit {
  font-family: var(--mono);
  font-size: 0.58rem;
  color: var(--text-dim);
  line-height: 1.8;
  letter-spacing: 0.04em;
}
.sb-footer-credit span { color: var(--gold); }

/* ── MAIN TOPBAR ── */
.topbar {
  padding: 1.25rem 2rem;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--sidebar-bg);
}
.topbar-title {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--text);
  letter-spacing: -0.01em;
}
.topbar-badge {
  font-family: var(--mono);
  font-size: 0.58rem;
  letter-spacing: 0.1em;
  color: var(--text-dim);
  background: var(--card2);
  border: 1px solid var(--border);
  padding: 0.25rem 0.7rem;
  border-radius: var(--radius-sm);
}

/* ── CHAT CONTAINER ── */
.chat-wrap {
  max-width: 780px;
  margin: 0 auto;
  padding: 2rem 1.5rem 1rem;
}

/* ── EMPTY STATE ── */
.empty-state {
  text-align: center;
  padding: 5rem 2rem;
  animation: fadeUp 0.6s ease both;
}
.empty-icon {
  font-size: 2rem;
  margin-bottom: 1rem;
  opacity: 0.4;
}
.empty-title {
  font-size: 1.1rem;
  font-weight: 500;
  color: var(--text-mid);
  margin-bottom: 0.4rem;
}
.empty-sub {
  font-size: 0.8rem;
  color: var(--text-dim);
  line-height: 1.7;
}

/* ── MESSAGES ── */
.msg-wrap { animation: fadeUp 0.35s ease both; margin-bottom: 1.25rem; }

.msg-user {
  display: flex;
  justify-content: flex-end;
}
.msg-user-inner {
  max-width: 68%;
}
.msg-user-bubble {
  background: var(--card2);
  border: 1px solid var(--border);
  border-radius: var(--radius) var(--radius) 2px var(--radius);
  padding: 0.8rem 1.1rem;
  font-size: 0.875rem;
  line-height: 1.65;
  color: var(--text);
}
.msg-meta {
  font-family: var(--mono);
  font-size: 0.55rem;
  color: var(--text-dim);
  letter-spacing: 0.06em;
  margin-top: 0.3rem;
  text-align: right;
}

.msg-ai {}
.msg-ai-tag {
  font-family: var(--mono);
  font-size: 0.58rem;
  letter-spacing: 0.12em;
  color: var(--gold);
  text-transform: uppercase;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.msg-ai-tag::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--border);
}
.msg-ai-bubble {
  background: var(--card);
  border: 1px solid var(--border);
  border-left: 3px solid var(--gold);
  border-radius: 0 var(--radius) var(--radius) var(--radius);
  padding: 1rem 1.25rem;
  font-size: 0.875rem;
  line-height: 1.75;
  color: var(--text);
  font-weight: 300;
}
.source-strip {
  margin-top: 0.75rem;
  padding-top: 0.75rem;
  border-top: 1px solid var(--border);
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
}
.src-chip {
  font-family: var(--mono);
  font-size: 0.58rem;
  letter-spacing: 0.06em;
  color: var(--text-dim);
  background: var(--card2);
  border: 1px solid var(--border);
  padding: 0.2rem 0.55rem;
  border-radius: 4px;
}

/* ── INPUT BAR ── */
.input-wrap {
  position: sticky;
  bottom: 0;
  background: linear-gradient(to top, var(--bg) 75%, transparent);
  padding: 1rem 1.5rem 1.5rem;
  max-width: 780px;
  margin: 0 auto;
}

/* ── ANIMATIONS ── */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}

/* ── STREAMLIT WIDGET OVERRIDES ── */

/* Text inputs */
.stTextInput > div > div {
  background: var(--card2) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
}
.stTextInput > div > div:focus-within {
  border-color: var(--border-gold) !important;
  box-shadow: 0 0 0 3px rgba(201,168,76,0.06) !important;
}
.stTextInput input {
  font-family: var(--font) !important;
  font-size: 0.85rem !important;
  color: var(--text) !important;
  background: transparent !important;
}
.stTextInput input::placeholder { color: var(--text-dim) !important; }
.stTextInput label {
  font-family: var(--mono) !important;
  font-size: 0.6rem !important;
  letter-spacing: 0.1em !important;
  color: var(--text-dim) !important;
  text-transform: uppercase !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
  background: var(--card2) !important;
  border: 1px dashed rgba(255,255,255,0.1) !important;
  border-radius: var(--radius) !important;
  transition: border-color 0.2s !important;
}
[data-testid="stFileUploader"]:hover { border-color: var(--border-gold) !important; }
[data-testid="stFileUploader"] label,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p {
  font-family: var(--font) !important;
  font-size: 0.78rem !important;
  color: var(--text-mid) !important;
}
[data-testid="stFileUploader"] small { color: var(--text-dim) !important; }

/* Buttons — all filled gold style */
.stButton > button {
  width: 100% !important;
  background: var(--gold) !important;
  color: #0a0a0b !important;
  font-family: var(--mono) !important;
  font-size: 0.65rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  border: none !important;
  border-radius: var(--radius-sm) !important;
  padding: 0.6rem 1rem !important;
  transition: background 0.2s, transform 0.15s, box-shadow 0.2s !important;
  cursor: pointer !important;
}
.stButton > button:hover {
  background: var(--gold-hover) !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 4px 16px rgba(201,168,76,0.2) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* Secondary button — ghost style for "Clear" */
.stButton > button[kind="secondary"] {
  background: transparent !important;
  color: var(--text-dim) !important;
  border: 1px solid var(--border) !important;
}
.stButton > button[kind="secondary"]:hover {
  border-color: var(--red) !important;
  color: var(--red) !important;
  background: rgba(248,113,113,0.05) !important;
  box-shadow: none !important;
}

/* Chat input */
[data-testid="stChatInput"] {
  background: var(--card) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius) !important;
  transition: border-color 0.2s !important;
}
[data-testid="stChatInput"]:focus-within {
  border-color: var(--border-gold) !important;
  box-shadow: 0 0 0 3px rgba(201,168,76,0.06) !important;
}
[data-testid="stChatInput"] textarea {
  font-family: var(--font) !important;
  font-size: 0.875rem !important;
  color: var(--text) !important;
  background: transparent !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: var(--text-dim) !important; }
[data-testid="stChatInput"] button {
  background: var(--gold) !important;
  border-radius: var(--radius-sm) !important;
  color: #0a0a0b !important;
}

/* Alerts */
.stAlert {
  border-radius: var(--radius-sm) !important;
  font-family: var(--mono) !important;
  font-size: 0.72rem !important;
  border: none !important;
}

/* Spinner */
.stSpinner > div { border-top-color: var(--gold) !important; }

/* Metrics */
[data-testid="metric-container"] {
  background: var(--card2) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
  padding: 0.75rem 1rem !important;
}
[data-testid="stMetricLabel"] {
  font-family: var(--mono) !important;
  font-size: 0.58rem !important;
  letter-spacing: 0.08em !important;
  color: var(--text-dim) !important;
  text-transform: uppercase !important;
}
[data-testid="stMetricValue"] {
  font-family: var(--font) !important;
  font-size: 1.4rem !important;
  font-weight: 600 !important;
  color: var(--text) !important;
}

/* Expander */
[data-testid="stExpander"] {
  background: var(--card) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-sm) !important;
}
[data-testid="stExpander"] summary {
  font-family: var(--mono) !important;
  font-size: 0.65rem !important;
  color: var(--text-mid) !important;
  letter-spacing: 0.06em !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 3px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: var(--gold); }

/* Hide Streamlit padding artifacts */
.css-1d391kg, .css-18e3th9 { padding: 0 !important; }
div[data-testid="stVerticalBlock"] > div { gap: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ──────────────────────────────────────────────────────────────
if 'messages'       not in st.session_state: st.session_state.messages       = []
if 'docs_processed' not in st.session_state: st.session_state.docs_processed = False
if 'rag_engine'     not in st.session_state: st.session_state.rag_engine     = None

# ── SIDEBAR ────────────────────────────────────────────────────────────────────
with st.sidebar:

    # Brand
    st.markdown("""
    <div class="sb-brand">
      <div class="sb-brand-name">
        <span class="sb-brand-dot"></span>Personal Research Assistant
      </div>
      <div class="sb-brand-sub">DOCUMENT INTELLIGENCE</div>
    </div>
    """, unsafe_allow_html=True)

    # Status
    if st.session_state.docs_processed:
        st.markdown('<div class="sb-status ready"><span class="dot"></span>CORPUS READY</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="sb-status idle"><span class="dot"></span>AWAITING DOCUMENT</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:0.25rem'></div>", unsafe_allow_html=True)

    # ── API Key ──
    st.markdown('<div class="sb-section"><div class="sb-label">API Configuration</div>', unsafe_allow_html=True)
    groq_key = st.text_input("Groq API Key", type="password", placeholder="gsk_••••••••••••", label_visibility="collapsed")
    if groq_key:
        os.environ["GROQ_API_KEY"] = groq_key
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:0.25rem'></div>", unsafe_allow_html=True)

    # ── Upload ──
    st.markdown('<div class="sb-section"><div class="sb-label">Document Upload</div>', unsafe_allow_html=True)
    uploaded_files = st.file_uploader(
        "PDF files",
        type=['pdf'],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )
    if uploaded_files:
        total_mb = sum(f.size for f in uploaded_files) / (1024 * 1024)
        st.markdown(
            f"<div style='font-family:var(--mono,monospace);font-size:0.6rem;"
            f"color:#555;margin-top:0.4rem;letter-spacing:0.06em'>"
            f"{len(uploaded_files)} file(s) · {total_mb:.2f} MB</div>",
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    # ── Actions ──
    st.markdown('<div class="sb-section"><div class="sb-label">Actions</div>', unsafe_allow_html=True)

    if st.button("Index Corpus", key="index_btn"):
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
            with st.spinner("Indexing..."):
                try:
                    from rag_engine import RAGEngine
                    if not st.session_state.rag_engine:
                        st.session_state.rag_engine = RAGEngine()
                    chunks = st.session_state.rag_engine.process_documents(pdf_paths)
                    st.session_state.docs_processed = True
                    st.success(f"✓ {chunks} chunks indexed")
                    st.rerun()
                except Exception as e:
                    st.error(str(e))

    st.markdown("<div style='height:0.35rem'></div>", unsafe_allow_html=True)

    if st.button("Clear Session", key="clear_btn"):
        st.session_state.messages       = []
        st.session_state.docs_processed = False
        st.session_state.rag_engine     = None
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # ── Stats ──
    if st.session_state.messages:
        st.markdown("<div style='height:0.75rem'></div>", unsafe_allow_html=True)
        st.markdown('<div class="sb-section"><div class="sb-label">Session Stats</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        user_msgs = len([m for m in st.session_state.messages if m['role'] == 'user'])
        ai_msgs   = len([m for m in st.session_state.messages if m['role'] == 'assistant'])
        with c1: st.metric("Queries",    user_msgs)
        with c2: st.metric("Responses",  ai_msgs)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── Footer credit (always at bottom, never overlapping) ──
    st.markdown("""
    <div class="sb-footer">
      <div class="sb-footer-credit">
        Built by <span>Mariam Noorani</span><br>
        Groq · LLaMA-3.3 · FAISS
      </div>
    </div>
    """, unsafe_allow_html=True)


# ── MAIN ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="topbar">
  <div class="topbar-title">Personal Research Assistant</div>
  <div class="topbar-badge">GROQ + LLaMA-3.3-70B</div>
</div>
""", unsafe_allow_html=True)

# Chat messages
st.markdown('<div class="chat-wrap">', unsafe_allow_html=True)

if not st.session_state.messages:
    if st.session_state.docs_processed:
        st.markdown("""
        <div class="empty-state">
          <div class="empty-icon">📄</div>
          <div class="empty-title">Corpus indexed. Ready for queries.</div>
          <div class="empty-sub">Ask anything about your documents below.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="empty-state">
          <div class="empty-icon">📂</div>
          <div class="empty-title">No document loaded yet.</div>
          <div class="empty-sub">Upload a PDF and click Index Corpus<br>to start asking questions.</div>
        </div>
        """, unsafe_allow_html=True)
        with st.expander("How to get started"):
            st.markdown("""
            1. Get a free API key at [console.groq.com](https://console.groq.com)  
            2. Paste it in the sidebar  
            3. Upload one or more PDF files  
            4. Click **Index Corpus**  
            5. Ask questions in the input below
            """)

for msg in st.session_state.messages:
    if msg['role'] == 'user':
        st.markdown(f"""
        <div class="msg-wrap msg-user">
          <div class="msg-user-inner">
            <div class="msg-user-bubble">{msg['content']}</div>
            <div class="msg-meta">YOU</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        srcs = msg.get('sources', [])
        chips = "".join(f"<span class='src-chip'>Source {i+1}</span>" for i, _ in enumerate(srcs))
        source_html = f"<div class='source-strip'>{chips}</div>" if chips else ""
        st.markdown(f"""
        <div class="msg-wrap msg-ai">
          <div class="msg-ai-tag">Synthesis</div>
          <div class="msg-ai-bubble">
            {msg['content']}
            {source_html}
          </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── INPUT ──────────────────────────────────────────────────────────────────────
prompt = st.chat_input(
    "Ask a question about your documents..." if st.session_state.docs_processed else "Index a corpus first to begin...",
    disabled=not st.session_state.docs_processed
)

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.spinner("Synthesizing response..."):
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
