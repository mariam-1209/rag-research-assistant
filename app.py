import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Research Studio", page_icon="⬡", layout="wide", initial_sidebar_state="expanded")

# ── CSS CHUNK 1: base + sidebar ──
st.markdown("""<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#0a0a0a;--sb:#000;--card:#111;--card2:#0d0d0d;--red:#ff3333;--rdim:rgba(255,51,51,0.08);--rglow:rgba(255,51,51,0.22);--bdr:rgba(255,51,51,0.35);--bdlo:rgba(255,255,255,0.06);--w:#fff;--gr:#888;--gd:#444;--fn:'JetBrains Mono',monospace}
#MainMenu,footer,header{visibility:hidden}
*{box-sizing:border-box}
html,body{font-family:var(--fn);background:var(--bg);color:var(--w);margin:0;padding:0}
.stApp{background:var(--bg)!important}
[data-testid="stSidebar"]{background:var(--sb)!important;border-right:1px solid var(--bdr)!important}
[data-testid="stSidebar"]>div:first-child{padding:0!important}
section.main>div{padding:0!important}
.block-container{padding:0!important;max-width:100%!important}
</style>""", unsafe_allow_html=True)

# ── CSS CHUNK 2: components ──
st.markdown("""<style>
.brand{display:flex;align-items:center;gap:.75rem;padding:1.2rem 1.25rem;border-bottom:1px solid var(--bdr)}
.brand-hex{width:38px;height:38px;border:1px solid var(--bdr);border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;color:var(--red);background:var(--rdim)}
.brand-name{font-size:.8rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--w)}
.brand-sub{font-size:.55rem;letter-spacing:.16em;text-transform:uppercase;color:var(--gd);margin-top:.15rem}
.upload-card{margin:1rem 1rem 0;border:1px solid var(--red);border-radius:6px;padding:1.1rem;text-align:center;background:transparent;transition:all .25s}
.upload-card:hover{background:var(--rdim);box-shadow:0 0 18px var(--rglow)}
.upload-icon{font-size:1.4rem;color:var(--red);margin-bottom:.4rem}
.upload-title{font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--w)}
.upload-sub{font-size:.58rem;letter-spacing:.08em;text-transform:uppercase;color:var(--gr);margin-top:.12rem}
.upload-limit{font-size:.56rem;color:var(--gd);margin-top:.5rem;border-top:1px solid var(--bdlo);padding-top:.45rem;letter-spacing:.06em}
.api-card{margin:.75rem 1rem 0;border:1px solid var(--red);border-radius:6px;padding:.85rem 1rem}
.api-label{font-size:.55rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--red);margin-bottom:.4rem}
</style>""", unsafe_allow_html=True)

# ── CSS CHUNK 3: nav, status, profile, topbar ──
st.markdown("""<style>
.status-pill{display:inline-flex;align-items:center;gap:.4rem;font-size:.58rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;padding:.28rem .75rem;border-radius:3px;margin:.75rem 1rem 0;border:1px solid var(--bdr);color:var(--gr);background:transparent}
.status-pill.ready{color:var(--red);border-color:var(--red);background:var(--rdim)}
.dot{width:5px;height:5px;border-radius:50%;background:currentColor;animation:blink 1.8s infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.15}}
.nav-item{display:flex;align-items:center;gap:.65rem;padding:.6rem 1.25rem;font-size:.65rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--gr);cursor:pointer;border-left:2px solid transparent;transition:all .18s}
.nav-item:hover{color:var(--w);background:var(--rdim)}
.nav-item.active{color:var(--w);background:rgba(255,51,51,.06);border-left-color:var(--red)}
.profile{display:flex;align-items:center;gap:.7rem;padding:1rem 1.25rem;border-top:1px solid var(--bdlo)}
.profile-avatar{width:34px;height:34px;border-radius:3px;background:var(--red);display:flex;align-items:center;justify-content:center;font-size:.68rem;font-weight:700;color:var(--w);flex-shrink:0}
.profile-name{font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--w)}
.profile-role{font-size:.56rem;letter-spacing:.1em;text-transform:uppercase;color:var(--gd);margin-top:.1rem}
.topbar{display:flex;align-items:center;justify-content:space-between;padding:.9rem 1.75rem;border-bottom:1px solid var(--bdr);background:var(--sb)}
.topbar-left{display:flex;align-items:center;gap:1.25rem}
.topbar-title{font-size:.72rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--w)}
.topbar-div{width:1px;height:16px;background:var(--bdlo)}
.topbar-status{font-size:.6rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gr)}
.topbar-status span{color:var(--red);font-weight:600}
.topbar-badge{font-size:.6rem;letter-spacing:.12em;text-transform:uppercase;color:var(--w);border:1px solid var(--red);padding:.3rem .85rem;border-radius:3px}
</style>""", unsafe_allow_html=True)

# ── CSS CHUNK 4: chat, messages, footer ──
st.markdown("""<style>
.chat-wrap{max-width:900px;margin:0 auto;padding:2rem 1.5rem .5rem}
.empty-state{text-align:center;padding:1.5rem 2rem 1rem;animation:fadeUp .6s ease both}
.empty-icon-box{width:78px;height:78px;border:1px solid var(--red);border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:1.7rem;margin:0 auto 1.5rem;background:var(--rdim)}
.empty-title{font-size:1.4rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:var(--w);margin-bottom:.65rem;line-height:1.2}
.empty-sub{font-size:.65rem;letter-spacing:.1em;text-transform:uppercase;color:var(--gr);line-height:2}
.step-row{display:flex;gap:0;margin-top:2rem}
.step-card{flex:1;border:1px solid var(--bdr);border-right:none;padding:1.25rem;background:var(--card2);transition:all .25s;position:relative}
.step-card:last-child{border-right:1px solid var(--bdr)}
.step-card.hot,.step-card:hover{background:var(--rdim);border-color:var(--red);box-shadow:0 0 22px var(--rglow);z-index:1}
.step-num{position:absolute;top:-1px;left:-1px;font-size:.55rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--red);background:var(--card2);border:1px solid var(--red);padding:.15rem .5rem;border-radius:0 0 4px 0}
.step-card.hot .step-num,.step-card:hover .step-num{background:var(--red);color:var(--w)}
.step-icon{font-size:1.1rem;color:var(--red);margin:1.5rem 0 .65rem}
.step-heading{font-size:.72rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--w);margin-bottom:.5rem}
.step-card.hot .step-heading,.step-card:hover .step-heading{color:var(--red)}
.step-body{font-size:.62rem;letter-spacing:.06em;text-transform:uppercase;color:var(--gr);line-height:1.9;font-weight:300}
.step-card.hot .step-body,.step-card:hover .step-body{color:var(--w)}
.msg-wrap{animation:fadeUp .3s ease both;margin-bottom:1.25rem}
.msg-user{display:flex;justify-content:flex-end}
.msg-user-bubble{max-width:65%;background:var(--card);border:1px solid var(--bdlo);border-radius:4px 4px 0 4px;padding:.85rem 1.1rem;font-size:.8rem;line-height:1.75;color:var(--w)}
.msg-meta{font-size:.52rem;letter-spacing:.1em;color:var(--gd);text-align:right;margin-top:.25rem;text-transform:uppercase}
.msg-ai-tag{display:flex;align-items:center;gap:.5rem;font-size:.55rem;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--red);margin-bottom:.5rem}
.msg-ai-bubble{background:var(--card);border:1px solid var(--bdlo);border-left:2px solid var(--red);border-radius:0 4px 4px 4px;padding:1rem 1.25rem;font-size:.8rem;line-height:1.85;color:var(--w);font-weight:300}
.src-row{margin-top:.7rem;padding-top:.65rem;border-top:1px solid var(--bdlo);display:flex;flex-wrap:wrap;gap:.35rem;align-items:center}
.src-label{font-size:.55rem;letter-spacing:.1em;color:var(--gd);text-transform:uppercase}
.src-chip{font-size:.55rem;color:var(--red);background:var(--rdim);border:1px solid var(--bdr);padding:.15rem .5rem;border-radius:3px}
.main-footer{border-top:1px solid var(--bdr);padding:1rem 1.75rem;display:flex;align-items:center;justify-content:space-between;background:var(--sb)}
.footer-made{font-size:.56rem;letter-spacing:.1em;text-transform:uppercase;color:var(--gr);margin-bottom:.12rem}
.footer-name{font-size:.78rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--w)}
.footer-right{display:flex;gap:2rem;align-items:center}
.footer-status{font-size:.56rem;letter-spacing:.1em;text-transform:uppercase;color:var(--gd)}
.footer-status span{color:var(--red)}
.footer-link{font-size:.56rem;letter-spacing:.1em;text-transform:uppercase;color:var(--gd);cursor:pointer}
@keyframes fadeUp{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
</style>""", unsafe_allow_html=True)

# ── CSS CHUNK 5: widget overrides ──
st.markdown("""<style>
.stTextInput>div>div{background:#0d0d0d!important;border:1px solid rgba(255,51,51,.35)!important;border-radius:3px!important}
.stTextInput>div>div:focus-within{border-color:#ff3333!important;box-shadow:0 0 0 2px rgba(255,51,51,.08)!important}
.stTextInput input{font-family:'JetBrains Mono',monospace!important;font-size:.8rem!important;color:#fff!important;background:transparent!important;letter-spacing:.05em!important}
.stTextInput input::placeholder{color:#333!important}
.stTextInput label{display:none!important}
[data-testid="stFileUploader"]{background:transparent!important;border:none!important}
[data-testid="stFileUploader"] section{background:transparent!important;border:none!important;padding:0!important}
[data-testid="stFileUploader"] label,[data-testid="stFileUploader"] span,[data-testid="stFileUploader"] p,[data-testid="stFileUploader"] small{font-family:'JetBrains Mono',monospace!important;color:#888!important;font-size:.65rem!important}
.stButton>button{background:transparent!important;color:#fff!important;border:1px solid #ff3333!important;font-family:'JetBrains Mono',monospace!important;font-size:.6rem!important;font-weight:700!important;letter-spacing:.16em!important;text-transform:uppercase!important;border-radius:3px!important;padding:.55rem .75rem!important;transition:all .2s!important;width:100%!important}
.stButton>button:hover{background:#ff3333!important;box-shadow:0 0 16px rgba(255,51,51,.22)!important}
[data-testid="stChatInput"]{background:#0d0d0d!important;border:1px solid rgba(255,51,51,.35)!important;border-radius:3px!important}
[data-testid="stChatInput"]:focus-within{border-color:#ff3333!important}
[data-testid="stChatInput"] textarea{font-family:'JetBrains Mono',monospace!important;font-size:.8rem!important;color:#fff!important;background:transparent!important}
[data-testid="stChatInput"] textarea::placeholder{color:#333!important;font-style:italic!important}
[data-testid="stChatInput"] button{background:#ff3333!important;border-radius:2px!important}
.stAlert{border-radius:3px!important;font-family:'JetBrains Mono',monospace!important;font-size:.68rem!important}
[data-testid="metric-container"]{background:#111!important;border:1px solid rgba(255,255,255,.06)!important;border-radius:3px!important;padding:.65rem 1rem!important}
[data-testid="stMetricLabel"]{font-family:'JetBrains Mono',monospace!important;font-size:.52rem!important;letter-spacing:.14em!important;color:#444!important;text-transform:uppercase!important}
[data-testid="stMetricValue"]{font-family:'JetBrains Mono',monospace!important;font-size:1.2rem!important;font-weight:700!important;color:#fff!important}
::-webkit-scrollbar{width:2px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:#1a1a1a;border-radius:1px}
::-webkit-scrollbar-thumb:hover{background:#ff3333}
</style>""", unsafe_allow_html=True)

# ── SESSION STATE ──
if 'messages'       not in st.session_state: st.session_state.messages       = []
if 'docs_processed' not in st.session_state: st.session_state.docs_processed = False
if 'rag_engine'     not in st.session_state: st.session_state.rag_engine     = None

# ── SIDEBAR ──
with st.sidebar:
    st.markdown("""<div class="brand"><div class="brand-hex">⬡</div><div><div class="brand-name">Research Studio</div><div class="brand-sub">Academic Intelligence</div></div></div>""", unsafe_allow_html=True)
    st.markdown("""<div class="upload-card"><div class="upload-icon">☁</div><div class="upload-title">Drag &amp; Drop your PDF here</div><div class="upload-sub">or click to browse</div><div class="upload-limit">200MB per file · PDF</div></div>""", unsafe_allow_html=True)
    st.markdown("<div style='padding:0 1rem'>", unsafe_allow_html=True)
    uploaded_files = st.file_uploader("PDF", type=['pdf'], accept_multiple_files=True, label_visibility="collapsed")
    if uploaded_files:
        total_mb = sum(f.size for f in uploaded_files)/(1024*1024)
        st.markdown(f"<div style='font-size:.56rem;color:#444;padding:.2rem 0;letter-spacing:.06em'>{len(uploaded_files)} file(s) · {total_mb:.2f} MB</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("""<div class="api-card"><div class="api-label">API Key Config</div></div>""", unsafe_allow_html=True)
    st.markdown("<div style='padding:0 1rem'>", unsafe_allow_html=True)
    groq_key = st.text_input("key", type="password", placeholder="gsk_••••••••••••", label_visibility="collapsed")
    if groq_key: os.environ["GROQ_API_KEY"] = groq_key
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div style='padding:.65rem 1rem 0'>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("Index Documents", key="idx"):
            if not groq_key: st.error("API key required")
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
        if st.button("Clear Session", key="clr"):
            st.session_state.messages=[]; st.session_state.docs_processed=False; st.session_state.rag_engine=None
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    if st.session_state.docs_processed:
        st.markdown('<div class="status-pill ready"><span class="dot"></span>Corpus Ready</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-pill"><span class="dot"></span>Awaiting Input</div>', unsafe_allow_html=True)
    st.markdown("""<div style="margin-top:.5rem">
    <div class="nav-item active"><span>☁</span> Upload Documents</div>
    <div class="nav-item"><span>⬡</span> API Configuration</div>
    <div class="nav-item"><span>◫</span> Session Index</div>
    <div class="nav-item"><span>⚡</span> Live Research</div>
    </div>""", unsafe_allow_html=True)
    if st.session_state.messages:
        st.markdown("<div style='padding:.5rem 1rem 0'>", unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        with c1: st.metric("Queries",   len([m for m in st.session_state.messages if m['role']=='user']))
        with c2: st.metric("Responses", len([m for m in st.session_state.messages if m['role']=='assistant']))
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("""<div style="height:1.5rem"></div>
    <div class="profile"><div class="profile-avatar">MN</div><div><div class="profile-name">Mariam Noorani</div><div class="profile-role">Research Assistant</div></div></div>""", unsafe_allow_html=True)

# ── MAIN ──
status_txt = "ONLINE" if st.session_state.docs_processed else "STANDBY"
st.markdown(f"""<div class="topbar"><div class="topbar-left"><div class="topbar-title">Personal Research Assistant</div><div class="topbar-div"></div><div class="topbar-status">System Status: <span>{status_txt}</span></div></div><div class="topbar-badge">Powered by Groq + LLaMA</div></div>""", unsafe_allow_html=True)
st.markdown('<div class="chat-wrap">', unsafe_allow_html=True)

if not st.session_state.messages:
    if st.session_state.docs_processed:
        st.markdown("""<div class="empty-state"><div class="empty-icon-box">✦</div><div class="empty-title">Corpus Indexed.<br>Begin Your Inquiry.</div><div class="empty-sub">Ask anything about your documents below.</div></div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div class="empty-state"><div class="empty-icon-box">✦✦</div><div class="empty-title">How Can I Assist Your<br>Inquiry Today?</div><div class="empty-sub">Synthesize complex datasets, extract critical insights from academic papers,<br>or generate technical summaries in real-time.</div></div>
<div class="step-row">
  <div class="step-card"><div class="step-num">Step 01</div><div class="step-icon">🔑</div><div class="step-heading">Configure API</div><div class="step-body">Establish connection to the Groq inference engine via your secure API key.</div></div>
  <div class="step-card hot"><div class="step-num">Step 02</div><div class="step-icon">☁</div><div class="step-heading">Upload Documents</div><div class="step-body">Ingest academic PDFs or technical manuals for the assistant to index.</div></div>
  <div class="step-card"><div class="step-num">Step 03</div><div class="step-icon">⚡</div><div class="step-heading">Index &amp; Inquiry</div><div class="step-body">Query the local knowledge base and receive precise, sourced responses.</div></div>
</div>""", unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg['role']=='user':
        st.markdown(f"""<div class="msg-wrap msg-user"><div><div class="msg-user-bubble">{msg['content']}</div><div class="msg-meta">You</div></div></div>""", unsafe_allow_html=True)
    else:
        srcs=msg.get('sources',[])
        chips="".join(f"<span class='src-chip'>Source {i+1}</span>" for i,_ in enumerate(srcs))
        src_html=f"<div class='src-row'><span class='src-label'>◦ {len(srcs)} citation(s)</span>{chips}</div>" if srcs else ""
        st.markdown(f"""<div class="msg-wrap"><div class="msg-ai-tag">⬡ Academic Synthesis</div><div class="msg-ai-bubble">{msg['content']}{src_html}</div></div>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

prompt = st.chat_input("Ask a question about your documents..." if st.session_state.docs_processed else "Index a document first...", disabled=not st.session_state.docs_processed)
if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.spinner("Synthesizing..."):
        try:
            response,sources=st.session_state.rag_engine.query(prompt)
            st.session_state.messages.append({"role":"assistant","content":response,"sources":sources})
        except Exception as e:
            st.session_state.messages.append({"role":"assistant","content":f"Error: {str(e)}","sources":[]})
    st.rerun()

st.markdown(f"""<div class="main-footer"><div><div class="footer-made">Made by</div><div class="footer-name">Mariam Noorani</div></div><div class="footer-right"><div class="footer-status">System Status: <span>{status_txt}</span></div><div class="footer-link">Documentation</div><div class="footer-link">License</div></div></div>""", unsafe_allow_html=True)
