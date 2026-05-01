import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Research Studio",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,600;1,300&family=Syne:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>
:root {
  --bg:         #0b0f14;
  --sidebar-bg: #0d1219;
  --card:       #111820;
  --card2:      #151e28;
  --border:     rgba(0,188,212,0.1);
  --border-hi:  rgba(0,188,212,0.35);
  --cyan:       #00bcd4;
  --cyan-dim:   rgba(0,188,212,0.08);
  --cyan-glow:  rgba(0,188,212,0.2);
  --text:       #c8d8e8;
  --text-mid:   #6a8099;
  --text-dim:   #3a4f62;
  --green:      #00e5a0;
  --font-mono:  'JetBrains Mono', monospace;
  --font-head:  'Syne', sans-serif;
}

#MainMenu, footer, header { visibility: hidden; }
*, *::before, *::after { box-sizing: border-box; }
html, body, .stApp { background: var(--bg) !important; font-family: var(--font-mono); }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
  background: var(--sidebar-bg) !important;
  border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] > div:first-child { padding: 0 !important; }
section.main > div { padding: 0 !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── BRAND ── */
.brand {
  padding: 1.75rem 1.5rem 1.5rem;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
}
.brand-icon {
  width: 36px; height: 36px;
  background: var(--cyan-dim);
  border: 1px solid var(--border-hi);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  flex-shrink: 0;
  color: var(--cyan);
}
.brand-text {}
.brand-name {
  font-family: var(--font-head);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--cyan);
  line-height: 1.1;
  letter-spacing: -0.01em;
}
.brand-sub {
  font-size: 0.55rem;
  letter-spacing: 0.18em;
  color: var(--text-dim);
  margin-top: 0.2rem;
  text-transform: uppercase;
}

/* ── UPLOAD BOX ── */
.upload-box {
  margin: 1.25rem 1.25rem 0;
  border: 1px dashed var(--border-hi);
  border-radius: 10px;
  padding: 1.25rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.25s;
  background: var(--cyan-dim);
}
.upload-box:hover { border-color: var(--cyan); background: rgba(0,188,212,0.12); }
.upload-icon { font-size: 1.4rem; color: var(--cyan); opacity: 0.7; margin-bottom: 0.4rem; }
.upload-title { font-size: 0.65rem; font-weight: 600; letter-spacing: 0.12em; color: var(--text); text-transform: uppercase; }
.upload-sub   { font-size: 0.58rem; color: var(--text-dim); margin-top: 0.15rem; letter-spacing: 0.06em; }

/* ── NAV ── */
.nav-section { padding: 1.25rem 0 0; }
.nav-label {
  font-size: 0.55rem;
  letter-spacing: 0.15em;
  color: var(--text-dim);
  text-transform: uppercase;
  padding: 0 1.25rem;
  margin-bottom: 0.4rem;
}
.nav-item {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.6rem 1.25rem;
  font-size: 0.75rem;
  color: var(--text-mid);
  cursor: pointer;
  transition: all 0.2s;
  border-left: 2px solid transparent;
  letter-spacing: 0.04em;
}
.nav-item:hover { color: var(--text); background: var(--cyan-dim); }
.nav-item.active {
  color: var(--cyan);
  background: var(--cyan-dim);
  border-left-color: var(--cyan);
}
.nav-icon { font-size: 0.85rem; width: 18px; text-align: center; }

/* ── STATUS ── */
.status-wrap { padding: 0.75rem 1.25rem; }
.status-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.58rem;
  letter-spacing: 0.1em;
  padding: 0.25rem 0.7rem;
  border-radius: 99px;
}
.status-pill.ready   { background: rgba(0,229,160,0.08); color: var(--green); border: 1px solid rgba(0,229,160,0.2); }
.status-pill.idle    { background: var(--cyan-dim); color: var(--cyan); border: 1px solid var(--border-hi); }
.dot { width:5px; height:5px; border-radius:50%; background:currentColor; animation: blink 1.8s infinite; }
@keyframes blink { 0%,100%{opacity:1}50%{opacity:0.2} }

/* ── PROFILE ── */
.profile {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  padding: 1rem 1.25rem;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 0.7rem;
}
.profile-avatar {
  width: 32px; height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--cyan), #006080);
  display: flex; align-items: center; justify-content: center;
  font-size: 0.75rem; font-weight: 600; color: #0b0f14;
  flex-shrink: 0;
}
.profile-name { font-size: 0.72rem; font-weight: 500; color: var(--text); letter-spacing: 0.02em; }
.profile-role { font-size: 0.58rem; color: var(--text-dim); letter-spacing: 0.06em; margin-top: 0.1rem; }

/* ── TOPBAR ── */
.topbar {
  padding: 1.1rem 2rem;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--sidebar-bg);
}
.topbar-title {
  font-family: var(--font-head);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--cyan);
}
.topbar-right { display: flex; align-items: center; gap: 0.75rem; }
.topbar-badge {
  font-size: 0.6rem;
  letter-spacing: 0.1em;
  color: var(--text-mid);
  background: var(--card2);
  border: 1px solid var(--border);
  padding: 0.28rem 0.75rem;
  border-radius: 99px;
}

/* ── CHAT ── */
.chat-wrap {
  max-width: 820px;
  margin: 0 auto;
  padding: 2.5rem 1.5rem 1rem;
}
.empty-state {
  text-align: center;
  padding: 5rem 2rem;
  animation: fadeUp 0.6s ease both;
}
.empty-sparkle { font-size: 2.5rem; opacity: 0.25; margin-bottom: 1.25rem; }
.empty-q {
  font-family: var(--font-head);
  font-size: 1.15rem;
  font-weight: 500;
  color: var(--text-mid);
  margin-bottom: 0.5rem;
}
.empty-hint { font-size: 0.72rem; color: var(--text-dim); line-height: 1.8; letter-spacing: 0.03em; }

/* ── USER MESSAGE ── */
.msg-user-wrap {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 1.5rem;
  animation: fadeUp 0.3s ease both;
}
.msg-user-bubble {
  max-width: 65%;
  background: var(--card2);
  border: 1px solid var(--border);
  border-radius: 10px 10px 2px 10px;
  padding: 0.85rem 1.1rem;
  font-size: 0.82rem;
  line-height: 1.7;
  color: var(--text);
}
.msg-time {
  font-size: 0.55rem;
  letter-spacing: 0.1em;
  color: var(--text-dim);
  text-align: right;
  margin-top: 0.3rem;
  text-transform: uppercase;
}

/* ── AI MESSAGE ── */
.msg-ai-wrap {
  margin-bottom: 1.5rem;
  animation: fadeUp 0.4s ease both;
}
.msg-ai-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.6rem;
}
.msg-ai-icon {
  width: 20px; height: 20px;
  border-radius: 50%;
  background: var(--cyan-dim);
  border: 1px solid var(--border-hi);
  display: flex; align-items: center; justify-content: center;
  font-size: 0.6rem;
  color: var(--cyan);
}
.msg-ai-tag {
  font-size: 0.58rem;
  letter-spacing: 0.16em;
  color: var(--cyan);
  text-transform: uppercase;
  font-weight: 600;
}
.msg-ai-bubble {
  background: var(--card);
  border: 1px solid var(--border);
  border-left: 3px solid var(--cyan);
  border-radius: 0 10px 10px 10px;
  padding: 1.1rem 1.4rem;
  font-size: 0.82rem;
  line-height: 1.85;
  color: var(--text);
  font-weight: 300;
}
.citations-row {
  margin-top: 0.85rem;
  padding-top: 0.75rem;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.cite-label {
  font-size: 0.58rem;
  letter-spacing: 0.1em;
  color: var(--text-dim);
  text-transform: uppercase;
}
.cite-chip {
  font-size: 0.58rem;
  letter-spacing: 0.06em;
  color: var(--cyan);
  background: var(--cyan-dim);
  border: 1px solid var(--border-hi);
  padding: 0.18rem 0.55rem;
  border-radius: 4px;
}

/* ── THINKING ── */
.thinking {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.65rem;
  letter-spacing: 0.12em;
  color: var(--cyan);
  text-transform: uppercase;
  padding: 0.5rem 0 1rem;
}
.think-dots span {
  display: inline-block;
  width: 4px; height: 4px;
  border-radius: 50%;
  background: var(--cyan);
  margin: 0 1px;
  animation: bounce 1.2s ease infinite;
}
.think-dots span:nth-child(2) { animation-delay: 0.15s; }
.think-dots span:nth-child(3) { animation-delay: 0.3s; }
@keyframes bounce { 0%,80%,100%{transform:translateY(0)}40%{transform:translateY(-5px)} }

/* ── FOOTER ── */
.main-footer {
  border-top: 1px solid var(--border);
  padding: 0.85rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--sidebar-bg);
}
.footer-credit {
  font-size: 0.6rem;
  letter-spacing: 0.1em;
  color: var(--text-dim);
  text-transform: uppercase;
}
.footer-credit span { color: var(--cyan); }
.footer-links { display: flex; gap: 1.5rem; }
.footer-link {
  font-size: 0.58rem;
  letter-spacing: 0.1em;
  color: var(--text-dim);
  text-transform: uppercase;
  cursor: pointer;
  transition: color 0.2s;
}
.footer-link:hover { color: var(--cyan); }

/* ── ANIMATIONS ── */
@keyframes fadeUp {
  from { opacity:0; transform:translateY(14px); }
  to   { opacity:1; transform:translateY(0); }
}

/* ── STREAMLIT OVERRIDES ── */
.stTextInput > div > div {
  background: var(--card2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 6px !important;
}
.stTextInput > div > div:focus-within {
  border-color: var(--border-hi) !important;
  box-shadow: 0 0 0 3px var(--cyan-dim) !important;
}
.stTextInput input {
  font-family: var(--font-mono) !important;
  font-size: 0.8rem !important;
  color: var(--text) !important;
  background: transparent !important;
  letter-spacing: 0.04em !important;
}
.stTextInput input::placeholder { color: var(--text-dim) !important; }
.stTextInput label {
  font-family: var(--font-mono) !important;
  font-size: 0.58rem !important;
  letter-spacing: 0.12em !important;
  color: var(--text-dim) !important;
  text-transform: uppercase !important;
}

[data-testid="stFileUploader"] {
  background: var(--cyan-dim) !important;
  border: 1px dashed var(--border-hi) !important;
  border-radius: 10px !important;
  transition: all 0.2s !important;
}
[data-testid="stFileUploader"]:hover { border-color: var(--cyan) !important; }
[data-testid="stFileUploader"] label,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p {
  font-family: var(--font-mono) !important;
  font-size: 0.7rem !important;
  color: var(--text-mid) !important;
}

.stButton > button {
  width: 100% !important;
  background: transparent !important;
  color: var(--cyan) !important;
  border: 1px solid var(--border-hi) !important;
  font-family: var(--font-mono) !important;
  font-size: 0.62rem !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  border-radius: 6px !important;
  padding: 0.6rem 1rem !important;
  transition: all 0.2s !important;
}
.stButton > button:hover {
  background: var(--cyan-dim) !important;
  border-color: var(--cyan) !important;
  box-shadow: 0 0 16px var(--cyan-glow) !important;
}

[data-testid="stChatInput"] {
  background: var(--card) !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
}
[data-testid="stChatInput"]:focus-within {
  border-color: var(--border-hi) !important;
  box-shadow: 0 0 0 3px var(--cyan-dim) !important;
}
[data-testid="stChatInput"] textarea {
  font-family: var(--font-mono) !important;
  font-size: 0.82rem !important;
  color: var(--text) !important;
  background: transparent !important;
  letter-spacing: 0.03em !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: var(--text-dim) !important; font-style: italic !important; }
[data-testid="stChatInput"] button { background: var(--cyan) !important; border-radius: 6px !important; }

.stAlert { border-radius: 6px !important; font-family: var(--font-mono) !important; font-size: 0.7rem !important; }

[data-testid="metric-container"] {
  background: var(--card2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 6px !important;
  padding: 0.75rem !important;
}
[data-testid="stMetricLabel"] { font-family: var(--font-mono) !important; font-size: 0.55rem !important; letter-spacing: 0.1em !important; color: var(--text-dim) !important; text-transform: uppercase !important; }
[data-testid="stMetricValue"] { font-family: var(--font-head) !important; font-size: 1.4rem !important; color: var(--text) !important; }

[data-testid="stExpander"] {
  background: var(--card) !important;
  border: 1px solid var(--border) !important;
  border-radius: 6px !important;
}
[data-testid="stExpander"] summary { font-family: var(--font-mono) !important; font-size: 0.65rem !important; color: var(--text-mid) !important; letter-spacing: 0.08em !important; }

::-webkit-scrollbar { width: 3px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: var(--cyan); }
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ──────────────────────────────────────────────────────────────
if 'messages'       not in st.session_state: st.session_state.messages       = []
if 'docs_processed' not in st.session_state: st.session_state.docs_processed = False
if 'rag_engine'     not in st.session_state: st.session_state.rag_engine     = None

# ── SIDEBAR ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="brand">
      <div class="brand-icon">⬡</div>
      <div class="brand-text">
        <div class="brand-name">Research Studio</div>
        <div class="brand-sub">Academic Intelligence</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Upload box styling (rendered via Streamlit but styled to match)
    st.markdown("""
    <div style="padding: 1.25rem 1.25rem 0">
      <div class="nav-label">Document</div>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        uploaded_files = st.file_uploader(
            "Upload Document",
            type=['pdf'],
            accept_multiple_files=True,
            label_visibility="collapsed"
        )
        if uploaded_files:
            total_mb = sum(f.size for f in uploaded_files) / (1024*1024)
            st.markdown(
                f"<div style='font-family:var(--font-mono);font-size:0.58rem;color:var(--text-dim);"
                f"letter-spacing:0.06em;padding:0.3rem 0'>{len(uploaded_files)} FILE(S) · {total_mb:.2f} MB</div>",
                unsafe_allow_html=True
            )

    st.markdown("""
    <div class="nav-section">
      <div class="nav-label">Workspace</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="nav-item active"><span class="nav-icon">📚</span> Library</div>
    <div class="nav-item"><span class="nav-icon">⚗️</span> Active Research</div>
    <div class="nav-item"><span class="nav-icon">❝</span> Citations</div>
    <div class="nav-item"><span class="nav-icon">⚙️</span> Settings</div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='padding:0.75rem 1.25rem 0'>", unsafe_allow_html=True)

    groq_key = st.text_input("API Key", type="password", placeholder="gsk_••••••••", label_visibility="collapsed")
    if groq_key:
        os.environ["GROQ_API_KEY"] = groq_key

    st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)

    if st.button("⬡  Index Document"):
        if not groq_key:
            st.error("API key required")
        elif not uploaded_files:
            st.error("Upload a PDF first")
        else:
            os.makedirs("data", exist_ok=True)
            pdf_paths = []
            for f in uploaded_files:
                p = f"data/{f.name}"
                with open(p, "wb") as out:
                    out.write(f.getbuffer())
                pdf_paths.append(p)
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
                    st.error(str(e))

    st.markdown("<div style='height:0.35rem'></div>", unsafe_allow_html=True)

    if st.button("✕  Clear Session"):
        st.session_state.messages       = []
        st.session_state.docs_processed = False
        st.session_state.rag_engine     = None
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.docs_processed:
        st.markdown('<div class="status-wrap"><div class="status-pill ready"><span class="dot"></span>CORPUS READY</div></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-wrap"><div class="status-pill idle"><span class="dot"></span>AWAITING INPUT</div></div>', unsafe_allow_html=True)

    if st.session_state.messages:
        st.markdown("<div style='padding:0 1.25rem'>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: st.metric("Queries",   len([m for m in st.session_state.messages if m['role']=='user']))
        with c2: st.metric("Responses", len([m for m in st.session_state.messages if m['role']=='assistant']))
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
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
  <div class="topbar-right">
    <div class="topbar-badge">Powered by Groq + LLaMA</div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="chat-wrap">', unsafe_allow_html=True)

if not st.session_state.messages:
    if st.session_state.docs_processed:
        st.markdown("""
        <div class="empty-state">
          <div class="empty-sparkle">✦</div>
          <div class="empty-q">Corpus indexed. Begin your inquiry.</div>
          <div class="empty-hint">Ask anything about your documents below.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="empty-state">
          <div class="empty-sparkle">✦ ✦ ✦</div>
          <div class="empty-q">How can I assist your inquiry today?</div>
          <div class="empty-hint">
            Upload a document or select an existing research project<br>
            to begin an intelligent dialogue with your data.
          </div>
        </div>
        """, unsafe_allow_html=True)
        with st.expander("◦  Getting Started"):
            st.markdown("""
            **01** · Get a free key at [console.groq.com](https://console.groq.com)  
            **02** · Paste the API key in the sidebar  
            **03** · Upload a PDF document  
            **04** · Click **Index Document**  
            **05** · Ask questions in natural language
            """)

for msg in st.session_state.messages:
    if msg['role'] == 'user':
        st.markdown(f"""
        <div class="msg-user-wrap">
          <div>
            <div class="msg-user-bubble">{msg['content']}</div>
            <div class="msg-time">Sent just now</div>
          </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        srcs = msg.get('sources', [])
        chips = "".join(f"<span class='cite-chip'>Source {i+1}</span>" for i, _ in enumerate(srcs))
        cite_html = f"""
        <div class='citations-row'>
          <span class='cite-label'>◦ View {len(srcs)} source citation(s)</span>
          {chips}
        </div>""" if srcs else ""

        st.markdown(f"""
        <div class="msg-ai-wrap">
          <div class="msg-ai-header">
            <div class="msg-ai-icon">⬡</div>
            <div class="msg-ai-tag">Academic Synthesis</div>
          </div>
          <div class="msg-ai-bubble">
            {msg['content']}
            {cite_html}
          </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── CHAT INPUT ──────────────────────────────────────────────────────────────────
prompt = st.chat_input(
    "Ask a technical question about your documents..." if st.session_state.docs_processed else "Index a document first...",
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

# ── FOOTER ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-footer">
  <div class="footer-credit">Built by <span>Mariam Noorani</span></div>
</div>
""", unsafe_allow_html=True)
