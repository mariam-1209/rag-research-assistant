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
  --bg:         #000000;
  --bg-main:    #0a0a0a;
  --card:       #0d0d0d;
  --card2:      #111111;
  --border:     rgba(255,51,51,0.25);
  --border-hi:  #ff3333;
  --red:        #ff3333;
  --red-dim:    rgba(255,51,51,0.08);
  --red-glow:   rgba(255,51,51,0.18);
  --white:      #ffffff;
  --gray:       #999999;
  --gray-dim:   #444444;
  --font:       'JetBrains Mono', monospace;
}

/* ── RESET ── */
#MainMenu, footer, header { visibility: hidden; }
*, *::before, *::after { box-sizing: border-box; }
html, body { font-family: var(--font); background: var(--bg); color: var(--white); }
.stApp { background: var(--bg) !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
  background: var(--bg) !important;
  border-right: 1px solid rgba(255,255,255,0.06) !important;
}
[data-testid="stSidebar"] > div:first-child { padding: 0 !important; }
section.main > div { padding: 0 !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── BRAND ── */
.brand {
  padding: 1.75rem 1.5rem 1.5rem;
  border-bottom: 1px solid rgba(255,255,255,0.06);
  display: flex;
  align-items: center;
  gap: 0.85rem;
}
.brand-hex {
  width: 40px; height: 40px;
  background: var(--red-dim);
  border: 1px solid var(--border);
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.1rem;
  flex-shrink: 0;
}
.brand-name {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--white);
  letter-spacing: -0.01em;
  line-height: 1.1;
}
.brand-sub {
  font-size: 0.58rem;
  letter-spacing: 0.16em;
  color: var(--gray-dim);
  margin-top: 0.2rem;
  text-transform: uppercase;
}

/* ── SIDEBAR CARD ── */
.sb-card {
  margin: 1.25rem 1.25rem 0;
  border: 1px solid var(--border-hi);
  border-radius: 8px;
  padding: 1rem;
  background: var(--card);
}
.sb-card-label {
  font-size: 0.55rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--gray);
  margin-bottom: 0.6rem;
}

/* ── NAV ── */
.nav-section { padding: 1.25rem 0 0; }
.nav-label {
  font-size: 0.55rem;
  letter-spacing: 0.16em;
  color: var(--gray-dim);
  text-transform: uppercase;
  padding: 0 1.25rem;
  margin-bottom: 0.35rem;
}
.nav-item {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  padding: 0.55rem 1.25rem;
  font-size: 0.75rem;
  color: var(--gray);
  cursor: pointer;
  border-left: 2px solid transparent;
  letter-spacing: 0.04em;
  transition: all 0.2s;
}
.nav-item:hover { color: var(--white); background: var(--red-dim); }
.nav-item.active { color: var(--white); background: var(--red-dim); border-left-color: var(--red); }

/* ── STATUS ── */
.status-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.58rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 0.25rem 0.7rem;
  border-radius: 99px;
  margin: 0.75rem 1.25rem 0;
  border: 1px solid var(--border);
  color: var(--red);
  background: var(--red-dim);
}
.status-pill.ready { color: #3ecf8e; background: rgba(62,207,142,0.08); border-color: rgba(62,207,142,0.3); }
.dot { width: 5px; height: 5px; border-radius: 50%; background: currentColor; animation: blink 1.8s infinite; }
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.2} }

/* ── AUTH SECTION ── */
.auth-section { padding: 1rem 1.25rem 0; }
.auth-label {
  font-size: 0.55rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--gray);
  margin-bottom: 0.5rem;
}

/* ── PROFILE ── */
.profile {
  padding: 1rem 1.25rem;
  border-top: 1px solid rgba(255,255,255,0.06);
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-top: auto;
}
.profile-avatar {
  width: 36px; height: 36px;
  border-radius: 50%;
  background: var(--red);
  display: flex; align-items: center; justify-content: center;
  font-size: 0.7rem;
  font-weight: 700;
  color: var(--white);
  flex-shrink: 0;
  letter-spacing: 0.04em;
}
.profile-name { font-size: 0.8rem; font-weight: 600; color: var(--white); letter-spacing: 0.02em; }
.profile-role { font-size: 0.6rem; color: var(--gray-dim); letter-spacing: 0.06em; margin-top: 0.1rem; }

/* ── TOPBAR ── */
.topbar {
  padding: 1rem 2rem;
  border-bottom: 1px solid rgba(255,255,255,0.06);
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--bg);
}
.topbar-title {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--white);
}
.topbar-badge {
  font-size: 0.6rem;
  letter-spacing: 0.1em;
  color: var(--gray);
  background: var(--card);
  border: 1px solid var(--border-hi);
  padding: 0.28rem 0.8rem;
  border-radius: 99px;
}

/* ── CHAT AREA ── */
.chat-wrap {
  max-width: 860px;
  margin: 0 auto;
  padding: 2.5rem 1.5rem 1rem;
}

/* ── EMPTY STATE ── */
.empty-state { text-align: center; padding: 3rem 2rem 2rem; animation: fadeUp 0.6s ease both; }
.empty-sparkle { font-size: 2.2rem; margin-bottom: 1.25rem; opacity: 0.5; }
.empty-title { font-size: 1.3rem; font-weight: 600; color: var(--white); margin-bottom: 0.5rem; letter-spacing: -0.02em; line-height: 1.3; }
.empty-sub { font-size: 0.78rem; color: var(--gray); line-height: 1.8; letter-spacing: 0.03em; }

/* ── STEP CARDS ── */
.step-cards { display: flex; gap: 1rem; margin-top: 2rem; }
.step-card {
  flex: 1;
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1.1rem;
  background: var(--card);
  transition: all 0.25s;
  cursor: default;
}
.step-card:hover, .step-card.active {
  border-color: var(--border-hi);
  background: var(--red-dim);
  box-shadow: 0 0 20px var(--red-glow);
}
.step-card:hover .step-num, .step-card.active .step-num { color: var(--red); }
.step-num {
  font-size: 0.6rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--gray-dim);
  margin-bottom: 0.6rem;
  font-weight: 600;
}
.step-text {
  font-size: 0.72rem;
  color: var(--gray);
  line-height: 1.75;
  letter-spacing: 0.02em;
}

/* ── MESSAGES ── */
.msg-wrap { animation: fadeUp 0.35s ease both; margin-bottom: 1.5rem; }
.msg-user { display: flex; justify-content: flex-end; }
.msg-user-inner { max-width: 65%; }
.msg-user-bubble {
  background: var(--card2);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 8px 8px 2px 8px;
  padding: 0.85rem 1.1rem;
  font-size: 0.82rem;
  line-height: 1.7;
  color: var(--white);
}
.msg-meta { font-size: 0.55rem; color: var(--gray-dim); letter-spacing: 0.08em; text-align: right; margin-top: 0.3rem; text-transform: uppercase; }

.msg-ai-tag {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.58rem;
  letter-spacing: 0.16em;
  color: var(--red);
  text-transform: uppercase;
  margin-bottom: 0.5rem;
}
.msg-ai-tag-icon {
  width: 18px; height: 18px;
  border-radius: 50%;
  background: var(--red-dim);
  border: 1px solid var(--border);
  display: flex; align-items: center; justify-content: center;
  font-size: 0.55rem;
}
.msg-ai-bubble {
  background: var(--card);
  border: 1px solid rgba(255,255,255,0.06);
  border-left: 3px solid var(--red);
  border-radius: 0 8px 8px 8px;
  padding: 1rem 1.25rem;
  font-size: 0.82rem;
  line-height: 1.8;
  color: var(--white);
  font-weight: 300;
}
.source-row { margin-top: 0.75rem; padding-top: 0.7rem; border-top: 1px solid rgba(255,255,255,0.06); display: flex; flex-wrap: wrap; gap: 0.4rem; align-items: center; }
.src-label { font-size: 0.58rem; letter-spacing: 0.08em; color: var(--gray-dim); text-transform: uppercase; }
.src-chip { font-size: 0.58rem; letter-spacing: 0.06em; color: var(--red); background: var(--red-dim); border: 1px solid var(--border); padding: 0.18rem 0.55rem; border-radius: 4px; }

/* ── MAIN FOOTER ── */
.main-footer {
  border-top: 1px solid rgba(255,255,255,0.06);
  padding: 0.85rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--bg);
}
.footer-credit { font-size: 0.65rem; letter-spacing: 0.1em; color: var(--gray-dim); }
.footer-credit span { color: var(--white); font-weight: 600; }
.footer-links { display: flex; gap: 1.5rem; }
.footer-link { font-size: 0.58rem; letter-spacing: 0.1em; color: var(--gray-dim); text-transform: uppercase; }

/* ── ANIMATIONS ── */
@keyframes fadeUp { from{opacity:0;transform:translateY(12px)} to{opacity:1;transform:translateY(0)} }

/* ── STREAMLIT OVERRIDES ── */
.stTextInput > div > div {
  background: var(--card2) !important;
  border: 1px solid var(--border-hi) !important;
  border-radius: 6px !important;
}
.stTextInput > div > div:focus-within {
  border-color: var(--red) !important;
  box-shadow: 0 0 0 3px var(--red-dim) !important;
}
.stTextInput input {
  font-family: var(--font) !important;
  font-size: 0.82rem !important;
  color: var(--white) !important;
  background: transparent !important;
  letter-spacing: 0.04em !important;
}
.stTextInput input::placeholder { color: var(--gray-dim) !important; }
.stTextInput label {
  font-family: var(--font) !important;
  font-size: 0.58rem !important;
  letter-spacing: 0.14em !important;
  color: var(--gray) !important;
  text-transform: uppercase !important;
}

[data-testid="stFileUploader"] {
  background: var(--card) !important;
  border: 1px solid var(--border-hi) !important;
  border-radius: 8px !important;
  transition: all 0.2s !important;
}
[data-testid="stFileUploader"]:hover {
  background: var(--red-dim) !important;
  box-shadow: 0 0 16px var(--red-glow) !important;
}
[data-testid="stFileUploader"] label,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p,
[data-testid="stFileUploader"] small {
  font-family: var(--font) !important;
  color: var(--gray) !important;
}

/* All buttons — red bordered ghost */
.stButton > button {
  background: transparent !important;
  color: var(--white) !important;
  border: 1px solid var(--border-hi) !important;
  font-family: var(--font) !important;
  font-size: 0.6rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.16em !important;
  text-transform: uppercase !important;
  border-radius: 6px !important;
  padding: 0.6rem 1rem !important;
  transition: all 0.2s !important;
  width: 100% !important;
}
.stButton > button:hover {
  background: var(--red-dim) !important;
  border-color: var(--red) !important;
  box-shadow: 0 0 16px var(--red-glow) !important;
  color: var(--red) !important;
}

[data-testid="stChatInput"] {
  background: var(--card) !important;
  border: 1px solid var(--border-hi) !important;
  border-radius: 8px !important;
}
[data-testid="stChatInput"]:focus-within {
  border-color: var(--red) !important;
  box-shadow: 0 0 0 3px var(--red-dim) !important;
}
[data-testid="stChatInput"] textarea {
  font-family: var(--font) !important;
  font-size: 0.82rem !important;
  color: var(--white) !important;
  background: transparent !important;
  letter-spacing: 0.03em !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: var(--gray-dim) !important; font-style: italic !important; }
[data-testid="stChatInput"] button { background: var(--red) !important; border-radius: 6px !important; }

.stAlert { border-radius: 6px !important; font-family: var(--font) !important; font-size: 0.7rem !important; }

[data-testid="metric-container"] {
  background: var(--card) !important;
  border: 1px solid var(--border) !important;
  border-radius: 6px !important;
  padding: 0.75rem !important;
}
[data-testid="stMetricLabel"] { font-family: var(--font) !important; font-size: 0.55rem !important; letter-spacing: 0.12em !important; color: var(--gray-dim) !important; text-transform: uppercase !important; }
[data-testid="stMetricValue"] { font-family: var(--font) !important; font-size: 1.3rem !important; font-weight: 700 !important; color: var(--white) !important; }

[data-testid="stExpander"] { background: var(--card) !important; border: 1px solid var(--border) !important; border-radius: 6px !important; }
[data-testid="stExpander"] summary { font-family: var(--font) !important; font-size: 0.65rem !important; color: var(--gray) !important; letter-spacing: 0.08em !important; }

div[data-testid="stVerticalBlock"] > div { gap: 0.4rem !important; }

::-webkit-scrollbar { width: 2px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #222; border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: var(--red); }
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

    # Document Upload card
    st.markdown("""
    <div style="padding:1.1rem 1.25rem 0">
      <div class="sb-card-label">Document Upload</div>
    </div>
    """, unsafe_allow_html=True)
    with st.container():
        st.markdown("<div style='padding:0 1.25rem'>", unsafe_allow_html=True)
        uploaded_files = st.file_uploader(
            "PDF",
            type=['pdf'],
            accept_multiple_files=True,
            label_visibility="collapsed"
        )
        if uploaded_files:
            total_mb = sum(f.size for f in uploaded_files) / (1024*1024)
            st.markdown(
                f"<div style='font-family:var(--font);font-size:0.58rem;color:#555;"
                f"letter-spacing:0.06em;padding:0.25rem 0'>{len(uploaded_files)} file(s) · {total_mb:.2f} MB</div>",
                unsafe_allow_html=True
            )
        st.markdown("</div>", unsafe_allow_html=True)

    # Nav
    st.markdown("""
    <div class="nav-section">
      <div class="nav-label">Workspace</div>
      <div class="nav-item active"><span>📚</span> Library</div>
      <div class="nav-item"><span>⚗️</span> Active Research</div>
      <div class="nav-item"><span>❝</span> Citations</div>
      <div class="nav-item"><span>⚙️</span> Settings</div>
    </div>
    """, unsafe_allow_html=True)

    # API Key
    st.markdown("""
    <div style="padding:1.1rem 1.25rem 0">
      <div class="sb-card-label">Authentication</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='padding:0 1.25rem'>", unsafe_allow_html=True)
    groq_key = st.text_input("API Key", type="password", placeholder="gsk_••••••••••••", label_visibility="collapsed")
    if groq_key:
        os.environ["GROQ_API_KEY"] = groq_key
    st.markdown("</div>", unsafe_allow_html=True)

    # Buttons side by side
    st.markdown("<div style='padding:0.6rem 1.25rem 0'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬡ Index", key="index_btn"):
            if not groq_key:
                st.error("API key required")
            elif not uploaded_files:
                st.error("Upload a PDF")
            else:
                os.makedirs("data", exist_ok=True)
                pdf_paths = []
                for f in uploaded_files:
                    p = f"data/{f.name}"
                    with open(p, "wb") as out:
                        out.write(f.getbuffer())
                    pdf_paths.append(p)
                with st.spinner("Indexing..."):
                    try:
                        from rag_engine import RAGEngine
                        if not st.session_state.rag_engine:
                            st.session_state.rag_engine = RAGEngine()
                        chunks = st.session_state.rag_engine.process_documents(pdf_paths)
                        st.session_state.docs_processed = True
                        st.success(f"✓ {chunks} chunks")
                        st.rerun()
                    except Exception as e:
                        st.error(str(e))
    with col2:
        if st.button("✕ Clear", key="clear_btn"):
            st.session_state.messages       = []
            st.session_state.docs_processed = False
            st.session_state.rag_engine     = None
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # Status
    if st.session_state.docs_processed:
        st.markdown('<div class="status-pill ready"><span class="dot"></span>CORPUS READY</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-pill"><span class="dot"></span>AWAITING INPUT</div>', unsafe_allow_html=True)

    # Stats
    if st.session_state.messages:
        st.markdown("<div style='padding:0.75rem 1.25rem 0'>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: st.metric("Queries",   len([m for m in st.session_state.messages if m['role']=='user']))
        with c2: st.metric("Responses", len([m for m in st.session_state.messages if m['role']=='assistant']))
        st.markdown("</div>", unsafe_allow_html=True)

    # Profile
    st.markdown("""
    <div style="height:1rem"></div>
    <div class="profile">
      <div class="profile-avatar">MN</div>
      <div>
        <div class="profile-name">Mariam Noorani</div>
        <div class="profile-role">Research Assistant</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ── MAIN ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="topbar">
  <div class="topbar-title">Personal Research Assistant</div>
  <div class="topbar-badge">Powered by Groq + LLaMA</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="chat-wrap">', unsafe_allow_html=True)

# Empty state
if not st.session_state.messages:
    if st.session_state.docs_processed:
        st.markdown("""
        <div class="empty-state">
          <div class="empty-sparkle">✦</div>
          <div class="empty-title">Corpus indexed.<br>Begin your inquiry.</div>
          <div class="empty-sub">Ask anything about your documents below.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="empty-state">
          <div class="empty-sparkle">✦</div>
          <div class="empty-title">How can I assist your<br>inquiry today?</div>
          <div class="empty-sub">Upload a document and index it to begin<br>an intelligent dialogue with your data.</div>
        </div>
        <div class="step-cards">
          <div class="step-card">
            <div class="step-num">Step 01</div>
            <div class="step-text">Get a free key at console.groq.com and paste it in the sidebar</div>
          </div>
          <div class="step-card active">
            <div class="step-num">Step 02</div>
            <div class="step-text">Upload a PDF document using the file uploader above</div>
          </div>
          <div class="step-card">
            <div class="step-num">Step 03</div>
            <div class="step-text">Click Index Documents, then ask questions below</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

# Messages
for msg in st.session_state.messages:
    if msg['role'] == 'user':
        st.markdown(f"""
        <div class="msg-wrap msg-user">
          <div class="msg-user-inner">
            <div class="msg-user-bubble">{msg['content']}</div>
            <div class="msg-meta">You</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        srcs = msg.get('sources', [])
        chips = "".join(f"<span class='src-chip'>Source {i+1}</span>" for i, _ in enumerate(srcs))
        src_html = f"<div class='source-row'><span class='src-label'>◦ {len(srcs)} citation(s)</span>{chips}</div>" if srcs else ""
        st.markdown(f"""
        <div class="msg-wrap">
          <div class="msg-ai-tag">
            <div class="msg-ai-tag-icon">⬡</div>
            Academic Synthesis
          </div>
          <div class="msg-ai-bubble">
            {msg['content']}
            {src_html}
          </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Input
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

# Footer
st.markdown("""
<div class="main-footer">
  <div class="footer-credit">Built by <span>MARIAM NOORANI</span></div>
  <div class="footer-links">
    <div class="footer-link">Documentation</div>
    <div class="footer-link">API Access</div>
  </div>
</div>
""", unsafe_allow_html=True)
