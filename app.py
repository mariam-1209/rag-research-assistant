import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Research Studio",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300&display=swap" rel="stylesheet">
<style>
:root {
  --bg:        #0a0a0a;
  --sidebar:   #000000;
  --card:      #111111;
  --card2:     #0d0d0d;
  --red:       #ff3333;
  --red-dim:   rgba(255,51,51,0.08);
  --red-glow:  rgba(255,51,51,0.22);
  --border:    rgba(255,51,51,0.35);
  --border-lo: rgba(255,255,255,0.06);
  --white:     #ffffff;
  --gray:      #888888;
  --gray-dim:  #444444;
  --font:      'JetBrains Mono', monospace;
}

#MainMenu, footer, header { visibility: hidden; }
*, *::before, *::after { box-sizing: border-box; }
html, body { font-family: var(--font); background: var(--bg); color: var(--white); margin: 0; padding: 0; }
.stApp { background: var(--bg) !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
  background: var(--sidebar) !important;
  border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] > div:first-child { padding: 0 !important; }
section.main > div { padding: 0 !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── BRAND ── */
.brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1.2rem 1.25rem;
  border-bottom: 1px solid var(--border);
}
.brand-hex {
  width: 38px; height: 38px;
  border: 1px solid var(--border);
  border-radius: 6px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.1rem;
  color: var(--red);
  flex-shrink: 0;
  background: var(--red-dim);
}
.brand-name {
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--white);
  line-height: 1.1;
}
.brand-sub {
  font-size: 0.55rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--gray-dim);
  margin-top: 0.15rem;
}

/* ── UPLOAD CARD ── */
.upload-card {
  margin: 1rem 1rem 0;
  border: 1px solid var(--red);
  border-radius: 6px;
  padding: 1.1rem;
  text-align: center;
  background: transparent;
  transition: all 0.25s;
  cursor: pointer;
}
.upload-card:hover { background: var(--red-dim); box-shadow: 0 0 18px var(--red-glow); }
.upload-icon { font-size: 1.5rem; color: var(--red); margin-bottom: 0.5rem; }
.upload-title { font-size: 0.68rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--white); }
.upload-sub   { font-size: 0.58rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--gray); margin-top: 0.15rem; }
.upload-limit { font-size: 0.56rem; color: var(--gray-dim); margin-top: 0.6rem; letter-spacing: 0.08em; border-top: 1px solid var(--border-lo); padding-top: 0.5rem; }

/* ── API CARD ── */
.api-card {
  margin: 0.75rem 1rem 0;
  border: 1px solid var(--red);
  border-radius: 6px;
  padding: 0.85rem 1rem;
  background: transparent;
}
.api-label {
  font-size: 0.55rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--red);
  margin-bottom: 0.5rem;
}

/* ── BUTTONS ROW ── */
.btn-row { display: flex; gap: 0.5rem; padding: 0.75rem 1rem 0; }

/* ── STATUS ── */
.status-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.58rem;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  padding: 0.28rem 0.75rem;
  border-radius: 3px;
  margin: 0.75rem 1rem 0;
  border: 1px solid var(--border);
  color: var(--gray);
  background: transparent;
}
.status-pill.ready { color: var(--red); border-color: var(--red); background: var(--red-dim); }
.dot { width: 5px; height: 5px; border-radius: 50%; background: currentColor; animation: blink 1.8s infinite; }
@keyframes blink { 0%,100%{opacity:1}50%{opacity:0.15} }

/* ── NAV ── */
.nav-item {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  padding: 0.6rem 1.25rem;
  font-size: 0.65rem;
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--gray);
  cursor: pointer;
  border-left: 2px solid transparent;
  transition: all 0.18s;
}
.nav-item:hover { color: var(--white); background: var(--red-dim); }
.nav-item.active { color: var(--white); background: rgba(255,51,51,0.06); border-left-color: var(--red); }
.nav-icon { font-size: 0.8rem; width: 16px; text-align: center; }

/* ── PROFILE ── */
.profile {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  padding: 1rem 1.25rem;
  border-top: 1px solid var(--border-lo);
}
.profile-avatar {
  width: 34px; height: 34px;
  border-radius: 3px;
  background: var(--red);
  display: flex; align-items: center; justify-content: center;
  font-size: 0.68rem;
  font-weight: 700;
  color: var(--white);
  flex-shrink: 0;
  letter-spacing: 0.05em;
}
.profile-name { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: var(--white); }
.profile-role { font-size: 0.56rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--gray-dim); margin-top: 0.1rem; }

/* ── TOPBAR ── */
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.9rem 1.75rem;
  border-bottom: 1px solid var(--border);
  background: var(--sidebar);
}
.topbar-left { display: flex; align-items: center; gap: 1.25rem; }
.topbar-title {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--white);
}
.topbar-divider { width: 1px; height: 18px; background: var(--border-lo); }
.topbar-status {
  font-size: 0.6rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--gray);
}
.topbar-status span { color: var(--red); font-weight: 600; }
.topbar-badge {
  font-size: 0.6rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--white);
  border: 1px solid var(--red);
  padding: 0.3rem 0.85rem;
  border-radius: 3px;
}

/* ── CHAT AREA ── */
.chat-wrap { max-width: 900px; margin: 0 auto; padding: 2rem 1.5rem 0.5rem; }

/* ── WATERMARK ── */
.watermark {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 4rem;
  font-weight: 700;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.02);
  white-space: nowrap;
  pointer-events: none;
  user-select: none;
}

/* ── EMPTY STATE ── */
.empty-state { text-align: center; padding: 1.5rem 2rem 1rem; animation: fadeUp 0.6s ease both; }
.empty-icon-box {
  width: 80px; height: 80px;
  border: 1px solid var(--red);
  border-radius: 6px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.8rem;
  margin: 0 auto 1.5rem;
  background: var(--red-dim);
}
.empty-title {
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--white);
  margin-bottom: 0.75rem;
  line-height: 1.2;
}
.empty-sub {
  font-size: 0.65rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--gray);
  line-height: 2;
}

/* ── STEP CARDS ── */
.step-row { display: flex; gap: 0; margin-top: 2rem; }
.step-card {
  flex: 1;
  border: 1px solid var(--border);
  border-right: none;
  padding: 1.25rem;
  background: var(--card2);
  transition: all 0.25s;
  position: relative;
}
.step-card:last-child { border-right: 1px solid var(--border); }
.step-card:hover, .step-card.hot {
  background: var(--red-dim);
  border-color: var(--red);
  box-shadow: 0 0 22px var(--red-glow);
  z-index: 1;
}
.step-card:hover .step-num, .step-card.hot .step-num { color: var(--white); background: var(--red); }
.step-card:hover .step-heading, .step-card.hot .step-heading { color: var(--red); }
.step-card:hover .step-body, .step-card.hot .step-body { color: var(--white); }
.step-num {
  position: absolute;
  top: -1px; left: -1px;
  font-size: 0.55rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--red);
  background: var(--card);
  border: 1px solid var(--red);
  padding: 0.15rem 0.5rem;
  border-radius: 0 0 4px 0;
}
.step-icon { font-size: 1.1rem; color: var(--red); margin: 1.5rem 0 0.75rem; }
.step-heading {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--white);
  margin-bottom: 0.6rem;
  transition: color 0.2s;
}
.step-body {
  font-size: 0.62rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--gray);
  line-height: 1.9;
  font-weight: 300;
  transition: color 0.2s;
}

/* ── MESSAGES ── */
.msg-wrap { animation: fadeUp 0.3s ease both; margin-bottom: 1.25rem; }
.msg-user { display: flex; justify-content: flex-end; }
.msg-user-bubble {
  max-width: 65%;
  background: var(--card);
  border: 1px solid var(--border-lo);
  border-radius: 4px 4px 0 4px;
  padding: 0.85rem 1.1rem;
  font-size: 0.8rem;
  line-height: 1.75;
  color: var(--white);
  letter-spacing: 0.02em;
}
.msg-meta { font-size: 0.52rem; letter-spacing: 0.1em; color: var(--gray-dim); text-align: right; margin-top: 0.25rem; text-transform: uppercase; }

.msg-ai-tag {
  display: flex; align-items: center; gap: 0.5rem;
  font-size: 0.55rem; font-weight: 600; letter-spacing: 0.2em;
  text-transform: uppercase; color: var(--red);
  margin-bottom: 0.5rem;
}
.msg-ai-bubble {
  background: var(--card);
  border: 1px solid var(--border-lo);
  border-left: 2px solid var(--red);
  border-radius: 0 4px 4px 4px;
  padding: 1rem 1.25rem;
  font-size: 0.8rem; line-height: 1.85; color: var(--white); font-weight: 300;
}
.src-row { margin-top: 0.7rem; padding-top: 0.65rem; border-top: 1px solid var(--border-lo); display: flex; flex-wrap: wrap; gap: 0.35rem; align-items: center; }
.src-label { font-size: 0.55rem; letter-spacing: 0.1em; color: var(--gray-dim); text-transform: uppercase; }
.src-chip { font-size: 0.55rem; letter-spacing: 0.06em; color: var(--red); background: var(--red-dim); border: 1px solid var(--border); padding: 0.15rem 0.5rem; border-radius: 3px; }

/* ── CHAT INPUT WRAPPER ── */
.input-section {
  border: 1px solid var(--border);
  border-radius: 4px;
  margin: 1rem 0;
  background: var(--card2);
  padding: 0 0.5rem;
}

/* ── FOOTER ── */
.main-footer {
  border-top: 1px solid var(--border);
  padding: 1rem 1.75rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--sidebar);
}
.footer-left {}
.footer-made { font-size: 0.58rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--gray); margin-bottom: 0.15rem; }
.footer-name { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--white); }
.footer-right { display: flex; gap: 2rem; align-items: center; }
.footer-link { font-size: 0.58rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--gray-dim); cursor: pointer; }
.footer-link:hover { color: var(--white); }
.footer-status { font-size: 0.58rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--gray-dim); }
.footer-status span { color: var(--red); }

/* ── ANIMATIONS ── */
@keyframes fadeUp { from{opacity:0;transform:translateY(10px)} to{opacity:1;transform:translateY(0)} }

/* ── STREAMLIT OVERRIDES ── */
.stTextInput > div > div {
  background: #0d0d0d !important;
  border: 1px solid var(--border) !important;
  border-radius: 3px !important;
}
.stTextInput > div > div:focus-within { border-color: var(--red) !important; box-shadow: 0 0 0 2px var(--red-dim) !important; }
.stTextInput input { font-family: var(--font) !important; font-size: 0.8rem !important; color: var(--white) !important; background: transparent !important; letter-spacing: 0.05em !important; }
.stTextInput input::placeholder { color: #333 !important; }
.stTextInput label { display: none !important; }

[data-testid="stFileUploader"] {
  background: transparent !important;
  border: none !important;
}
[data-testid="stFileUploader"] section {
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
}
[data-testid="stFileUploader"] label,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p,
[data-testid="stFileUploader"] small {
  font-family: var(--font) !important; color: var(--gray) !important; font-size: 0.65rem !important; letter-spacing: 0.06em !important;
}

.stButton > button {
  background: transparent !important;
  color: var(--white) !important;
  border: 1px solid var(--red) !important;
  font-family: var(--font) !important;
  font-size: 0.6rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.16em !important;
  text-transform: uppercase !important;
  border-radius: 3px !important;
  padding: 0.55rem 0.75rem !important;
  transition: all 0.2s !important;
  width: 100% !important;
}
.stButton > button:hover {
  background: var(--red) !important;
  color: var(--white) !important;
  box-shadow: 0 0 16px var(--red-glow) !important;
}

[data-testid="stChatInput"] {
  background: var(--card2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 3px !important;
}
[data-testid="stChatInput"]:focus-within { border-color: var(--red) !important; }
[data-testid="stChatInput"] textarea { font-family: var(--font) !important; font-size: 0.8rem !important; color: var(--white) !important; background: transparent !important; letter-spacing: 0.04em !important; }
[data-testid="stChatInput"] textarea::placeholder { color: #333 !important; font-style: italic !important; }
[data-testid="stChatInput"] button { background: var(--red) !important; border-radius: 2px !important; }

.stAlert { border-radius: 3px !important; font-family: var(--font) !important; font-size: 0.68rem !important; letter-spacing: 0.04em !important; }

[data-testid="metric-container"] { background: var(--card) !important; border: 1px solid var(--border-lo) !important; border-radius: 3px !important; padding: 0.65rem 1rem !important; }
[data-testid="stMetricLabel"] { font-family: var(--font) !important; font-size: 0.52rem !important; letter-spacing: 0.14em !important; color: var(--gray-dim) !important; text-transform: uppercase !important; }
[data-testid="stMetricValue"] { font-family: var(--font) !important; font-size: 1.2rem !important; font-weight: 700 !important; color: var(--white) !important; }

div[data-testid="stVerticalBlock"] > div { gap: 0.35rem !important; }

::-webkit-scrollbar { width: 2px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #1a1a1a; border-radius: 1px; }
::-webkit-scrollbar-thumb:hover { background: var(--red); }

/* Resize handle */
[data-testid="stSidebar"] [data-testid="stSidebarResizeHandle"] {
  background: var(--border) !important;
  width: 3px !important;
}
[data-testid="stSidebarResizeHandle"]:hover { background: var(--red) !important; }
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
    <div class="brand">
      <div class="brand-hex">⬡</div>
      <div>
        <div class="brand-name">Research Studio</div>
        <div class="brand-sub">Academic Intelligence</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Upload card
    st.markdown("""
    <div class="upload-card">
      <div class="upload-icon">☁️</div>
      <div class="upload-title">Drag &amp; Drop your PDF here</div>
      <div class="upload-sub">or click to browse</div>
      <div class="upload-limit">200MB per file · PDF</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='padding:0 1rem'>", unsafe_allow_html=True)
    uploaded_files = st.file_uploader("PDF", type=['pdf'], accept_multiple_files=True, label_visibility="collapsed")
    if uploaded_files:
        total_mb = sum(f.size for f in uploaded_files) / (1024*1024)
        st.markdown(f"<div style='font-size:0.56rem;letter-spacing:0.08em;color:#444;padding:0.2rem 0'>{len(uploaded_files)} file(s) · {total_mb:.2f} MB</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # API card
    st.markdown("""
    <div class="api-card">
      <div class="api-label">API Key Config</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='padding:0 1rem'>", unsafe_allow_html=True)
    groq_key = st.text_input("key", type="password", placeholder="gsk_••••••••••••", label_visibility="collapsed")
    if groq_key:
        os.environ["GROQ_API_KEY"] = groq_key
    st.markdown("</div>", unsafe_allow_html=True)

    # Buttons — side by side
    st.markdown("<div style='padding:0.65rem 1rem 0'>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Index Documents", key="idx"):
            if not groq_key:
                st.error("API key required")
            elif not uploaded_files:
                st.error("Upload a PDF first")
            else:
                os.makedirs("data", exist_ok=True)
                paths = []
                for f in uploaded_files:
                    p = f"data/{f.name}"
                    with open(p, "wb") as o: o.write(f.getbuffer())
                    paths.append(p)
                with st.spinner("Indexing..."):
                    try:
                        from rag_engine import RAGEngine
                        if not st.session_state.rag_engine:
                            st.session_state.rag_engine = RAGEngine()
                        chunks = st.session_state.rag_engine.process_documents(paths)
                        st.session_state.docs_processed = True
                        st.success(f"✓ {chunks} chunks indexed")
                        st.rerun()
                    except Exception as e:
                        st.error(str(e))
    with c2:
        if st.button("Clear Session", key="clr"):
            st.session_state.messages       = []
            st.session_state.docs_processed = False
            st.session_state.rag_engine     = None
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # Status
    if st.session_state.docs_processed:
        st.markdown('<div class="status-pill ready"><span class="dot"></span>Corpus Ready</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-pill"><span class="dot"></span>Awaiting Input</div>', unsafe_allow_html=True)

    # Nav
    st.markdown("""
    <div style="margin-top:0.5rem">
      <div class="nav-item active"><span class="nav-icon">☁</span> Upload Documents</div>
      <div class="nav-item"><span class="nav-icon">⬡</span> API Configuration</div>
      <div class="nav-item"><span class="nav-icon">◫</span> Session Index</div>
      <div class="nav-item"><span class="nav-icon">⚡</span> Live Research</div>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    if st.session_state.messages:
        st.markdown("<div style='padding:0.5rem 1rem 0'>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: st.metric("Queries",   len([m for m in st.session_state.messages if m['role']=='user']))
        with c2: st.metric("Responses", len([m for m in st.session_state.messages if m['role']=='assistant']))
        st.markdown("</div>", unsafe_allow_html=True)

    # Profile
    st.markdown("""
    <div style="height:1.5rem"></div>
    <div class="profile">
      <div class="profile-avatar">MN</div>
      <div>
        <div class="profile-name">Mariam Noorani</div>
        <div class="profile-role">Research Assistant</div>
      </div>
      <div style="margin-left:auto;font-size:0.9rem;color:#333;cursor:pointer">⚙</div>
    </div>
    """, unsafe_allow_html=True)

# ── MAIN ───────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="topbar">
  <div class="topbar-left">
    <div class="topbar-title">Personal Research Assistant</div>
    <div class="topbar-divider"></div>
    <div class="topbar-status">System Status: <span>{'ONLINE' if st.session_state.docs_processed else 'STANDBY'}</span></div>
  </div>
  <div class="topbar-badge">Powered by Groq + LLaMA</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="chat-wrap">', unsafe_allow_html=True)

if not st.session_state.messages:
    if st.session_state.docs_processed:
        st.markdown("""
        <div class="empty-state">
          <div class="empty-icon-box">✦</div>
          <div class="empty-title">Corpus Indexed.<br>Begin Your Inquiry.</div>
          <div class="empty-sub">Ask anything about your documents below.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="empty-state">
          <div class="empty-icon-box">✦✦</div>
          <div class="empty-title">How Can I Assist Your<br>Inquiry Today?</div>
          <div class="empty-sub">
            Synthesize complex datasets, extract critical insights from academic papers,<br>
            or generate technical summaries in real-time.
          </div>
        </div>
        <div class="step-row">
          <div class="step-card">
            <div class="step-num">Step 01</div>
            <div class="step-icon">🔑</div>
            <div class="step-heading">Configure API</div>
            <div class="step-body">Establish connection to the Groq inference engine via your secure API key.</div>
          </div>
          <div class="step-card hot">
            <div class="step-num">Step 02</div>
            <div class="step-icon">☁️</div>
            <div class="step-heading">Upload Documents</div>
            <div class="step-body">Ingest academic PDFs or technical manuals for the assistant to index.</div>
          </div>
          <div class="step-card">
            <div class="step-num">Step 03</div>
            <div class="step-icon">⚡</div>
            <div class="step-heading">Index &amp; Inquiry</div>
            <div class="step-body">Query the local knowledge base and receive precise, sourced responses.</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg['role'] == 'user':
        st.markdown(f"""
        <div class="msg-wrap msg-user">
          <div>
            <div class="msg-user-bubble">{msg['content']}</div>
            <div class="msg-meta">You</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        srcs = msg.get('sources', [])
        chips = "".join(f"<span class='src-chip'>Source {i+1}</span>" for i, _ in enumerate(srcs))
        src_html = f"<div class='src-row'><span class='src-label'>◦ {len(srcs)} citation(s)</span>{chips}</div>" if srcs else ""
        st.markdown(f"""
        <div class="msg-wrap">
          <div class="msg-ai-tag">⬡ Academic Synthesis</div>
          <div class="msg-ai-bubble">{msg['content']}{src_html}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

prompt = st.chat_input(
    "Ask a question about your documents..." if st.session_state.docs_processed else "Index a document first...",
    disabled=not st.session_state.docs_processed
)
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.spinner("Synthesizing..."):
        try:
            response, sources = st.session_state.rag_engine.query(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response, "sources": sources})
        except Exception as e:
            st.session_state.messages.append({"role": "assistant", "content": f"Error: {str(e)}", "sources": []})
    st.rerun()

# ── FOOTER ─────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="main-footer">
  <div class="footer-left">
    <div class="footer-made">Made by</div>
    <div class="footer-name">Mariam Noorani</div>
  </div>
  <div class="footer-right">
    <div class="footer-status">System Status: <span>{'ONLINE' if st.session_state.docs_processed else 'STANDBY'}</span></div>
    <div class="footer-link">Documentation</div>
    <div class="footer-link">License</div>
  </div>
</div>
""", unsafe_allow_html=True)
