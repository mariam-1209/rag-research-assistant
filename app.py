import streamlit as st, os
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Research Studio", layout="wide", initial_sidebar_state="expanded")

# ONE single CSS block, minified and clean
CSS = """
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600;700&display=swap" rel="stylesheet">
<style>
#MainMenu,footer,header,[data-testid="stHeader"],[data-testid="stToolbar"]{display:none!important}
html,body,.stApp,[data-testid="stAppViewContainer"],[data-testid="stMain"]{background:#000!important;font-family:'JetBrains Mono',monospace!important;color:#fff!important}
section.main>div,.block-container{padding:0!important;max-width:100%!important}
[data-testid="stSidebar"]{background:#000!important;border-right:1px solid rgba(255,51,51,0.4)!important}
[data-testid="stSidebar"]>div:first-child{padding:0!important}
div[data-testid="stVerticalBlock"]>div{gap:0!important}
[data-testid="stBottom"],[data-testid="stBottom"]>div{background:#000!important;border-top:none!important}

/* uploader */
[data-testid="stFileUploader"]{padding:0 1rem!important;background:transparent!important}
[data-testid="stFileUploaderDropzone"]{background:transparent!important;border:1px solid #ff3333!important;border-radius:6px!important;padding:1.5rem!important}
[data-testid="stFileUploaderDropzone"]:hover{background:rgba(255,51,51,0.08)!important;box-shadow:0 0 20px rgba(255,51,51,0.25)!important}
[data-testid="stFileUploaderDropzoneInstructions"] span{font-family:'JetBrains Mono',monospace!important;font-size:.7rem!important;font-weight:700!important;letter-spacing:.1em!important;text-transform:uppercase!important;color:#fff!important}
[data-testid="stFileUploaderDropzoneInstructions"] small{font-family:'JetBrains Mono',monospace!important;font-size:.58rem!important;color:#888!important}
[data-testid="stFileUploaderDropzone"] svg{color:#ff3333!important}
[data-testid="stFileUploaderDropzone"] button,[data-testid="stBaseButton-secondary"]{background:transparent!important;border:1px solid #ff3333!important;color:#fff!important;font-family:'JetBrains Mono',monospace!important;font-size:.6rem!important;border-radius:3px!important}
[data-testid="stFileUploaderFileName"]{font-family:'JetBrains Mono',monospace!important;font-size:.6rem!important;color:#888!important;background:transparent!important}

/* inputs */
.stTextInput>div>div{background:#0d0d0d!important;border:1px solid rgba(255,51,51,0.5)!important;border-radius:4px!important}
.stTextInput>div>div:focus-within{border-color:#ff3333!important;box-shadow:0 0 0 2px rgba(255,51,51,0.08)!important}
.stTextInput input{font-family:'JetBrains Mono',monospace!important;font-size:.82rem!important;color:#fff!important;background:transparent!important}
.stTextInput input::placeholder{color:#333!important}
.stTextInput label{display:none!important}

/* buttons */
.stButton>button{background:transparent!important;color:#fff!important;border:1px solid #ff3333!important;font-family:'JetBrains Mono',monospace!important;font-size:.6rem!important;font-weight:700!important;letter-spacing:.12em!important;text-transform:uppercase!important;border-radius:3px!important;width:100%!important;padding:.55rem!important;transition:all .2s!important}
.stButton>button:hover{background:#ff3333!important;box-shadow:0 0 16px rgba(255,51,51,0.28)!important}

/* chat input */
[data-testid="stChatInput"]{background:#0d0d0d!important;border:1px solid rgba(255,51,51,0.5)!important;border-radius:4px!important;box-shadow:none!important}
[data-testid="stChatInput"] textarea{font-family:'JetBrains Mono',monospace!important;color:#fff!important;background:transparent!important}
[data-testid="stChatInput"] textarea::placeholder{color:#444!important}
[data-testid="stChatInput"] button{background:#ff3333!important;border-radius:2px!important}

/* alerts */
.stAlert{background:#111!important;border-radius:3px!important;font-family:'JetBrains Mono',monospace!important;font-size:.7rem!important}

/* metrics */
[data-testid="metric-container"]{background:#111!important;border:1px solid rgba(255,255,255,0.06)!important;border-radius:3px!important;padding:.65rem!important}
[data-testid="stMetricLabel"]{font-family:'JetBrains Mono',monospace!important;font-size:.52rem!important;color:#444!important;text-transform:uppercase!important;letter-spacing:.12em!important}
[data-testid="stMetricValue"]{font-family:'JetBrains Mono',monospace!important;font-size:1.2rem!important;font-weight:700!important;color:#fff!important}

/* scrollbar */
::-webkit-scrollbar{width:2px}
::-webkit-scrollbar-thumb{background:#222;border-radius:1px}
::-webkit-scrollbar-thumb:hover{background:#ff3333}

/* layout elements */
.brand{display:flex;align-items:center;gap:.75rem;padding:1.2rem 1.25rem;border-bottom:1px solid rgba(255,51,51,0.4)}
.bhex{width:38px;height:38px;border:1px solid rgba(255,51,51,0.4);border-radius:6px;display:flex;align-items:center;justify-content:center;color:#ff3333;background:rgba(255,51,51,0.08);font-size:1.1rem;flex-shrink:0}
.bname{font-size:.8rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase}
.bsub{font-size:.55rem;letter-spacing:.16em;text-transform:uppercase;color:#444;margin-top:.15rem}
.slabel{font-size:.55rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:#ff3333;padding:.75rem 1rem .35rem}
.spill{display:inline-flex;align-items:center;gap:.4rem;font-size:.58rem;font-weight:600;letter-spacing:.14em;text-transform:uppercase;padding:.28rem .75rem;border-radius:3px;border:1px solid rgba(255,51,51,0.5);color:#888;margin:.5rem 1rem 0}
.spill.on{color:#ff3333;border-color:#ff3333;background:rgba(255,51,51,0.08)}
.dot{width:5px;height:5px;border-radius:50%;background:currentColor;animation:blink 1.8s infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.15}}
.nitem{display:flex;align-items:center;gap:.65rem;padding:.6rem 1.25rem;font-size:.65rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:#888;border-left:2px solid transparent;transition:all .18s}
.nitem:hover{color:#fff;background:rgba(255,51,51,0.08)}
.nitem.on{color:#fff;background:rgba(255,51,51,0.07);border-left-color:#ff3333}
.prof{display:flex;align-items:center;gap:.7rem;padding:1rem 1.25rem;border-top:1px solid rgba(255,255,255,0.06);margin-top:.5rem}
.pav{width:34px;height:34px;border-radius:3px;background:#ff3333;display:flex;align-items:center;justify-content:center;font-size:.68rem;font-weight:700;flex-shrink:0}
.pname{font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
.prole{font-size:.56rem;letter-spacing:.1em;text-transform:uppercase;color:#444;margin-top:.1rem}
.topbar{display:flex;align-items:center;justify-content:center;padding:1.1rem;border-bottom:1px solid rgba(255,51,51,0.4);background:#000}
.ttitle{font-size:1.1rem;font-weight:700;letter-spacing:.22em;text-transform:uppercase}
.cwrap{max-width:900px;margin:0 auto;padding:2rem 1.5rem .5rem}
.estate{text-align:center;padding:1rem 2rem 1.5rem;animation:fu .6s ease both}
.ebox{width:78px;height:78px;border:1px solid #ff3333;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:1.7rem;margin:0 auto 1.5rem;background:rgba(255,51,51,0.08)}
.etitle{font-size:1.35rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;margin-bottom:.65rem;line-height:1.25}
.esub{font-size:.65rem;letter-spacing:.1em;text-transform:uppercase;color:#888;line-height:2}
.srow{display:flex;margin-top:2rem}
.sc{flex:1;border:1px solid rgba(255,51,51,0.4);border-right:none;padding:1.25rem;background:#0d0d0d;transition:all .25s;position:relative}
.sc:last-child{border-right:1px solid rgba(255,51,51,0.4)}
.sc:hover{background:rgba(255,51,51,0.08);border-color:#ff3333;box-shadow:0 0 24px rgba(255,51,51,0.28);z-index:1}
.sn{position:absolute;top:-1px;left:-1px;font-size:.55rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#ff3333;background:#0d0d0d;border:1px solid #ff3333;padding:.15rem .5rem;border-radius:0 0 4px 0;transition:all .25s}
.sc:hover .sn{background:#ff3333;color:#fff}
.si{font-size:1.1rem;color:#ff3333;margin:1.5rem 0 .65rem}
.sh{font-size:.72rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;margin-bottom:.5rem;transition:color .25s}
.sc:hover .sh{color:#ff3333}
.sb2{font-size:.62rem;letter-spacing:.06em;text-transform:uppercase;color:#888;line-height:1.9;font-weight:300;transition:color .25s}
.sc:hover .sb2{color:#fff}
.mwrap{animation:fu .3s ease both;margin-bottom:1.25rem}
.muser{display:flex;justify-content:flex-end}
.mbub{max-width:65%;background:#111;border:1px solid rgba(255,255,255,0.06);border-radius:4px 4px 0 4px;padding:.85rem 1.1rem;font-size:.8rem;line-height:1.75}
.mmeta{font-size:.52rem;letter-spacing:.1em;color:#444;text-align:right;margin-top:.25rem;text-transform:uppercase}
.atag{display:flex;align-items:center;gap:.5rem;font-size:.55rem;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:#ff3333;margin-bottom:.5rem}
.abub{background:#111;border:1px solid rgba(255,255,255,0.06);border-left:2px solid #ff3333;border-radius:0 4px 4px 4px;padding:1rem 1.25rem;font-size:.8rem;line-height:1.85;font-weight:300}
.srcrow{margin-top:.7rem;padding-top:.65rem;border-top:1px solid rgba(255,255,255,0.06);display:flex;flex-wrap:wrap;gap:.35rem;align-items:center}
.srclbl{font-size:.55rem;letter-spacing:.1em;color:#444;text-transform:uppercase}
.srcc{font-size:.55rem;color:#ff3333;background:rgba(255,51,51,0.08);border:1px solid rgba(255,51,51,0.4);padding:.15rem .5rem;border-radius:3px}
.foot{border-top:1px solid rgba(255,51,51,0.4);padding:1rem 1.75rem;display:flex;align-items:center;justify-content:space-between;background:#000}
.fmade{font-size:.56rem;letter-spacing:.1em;text-transform:uppercase;color:#888;margin-bottom:.1rem}
.fname{font-size:.78rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.flinks{display:flex;gap:2rem}
.flink{font-size:.56rem;letter-spacing:.1em;text-transform:uppercase;color:#444;cursor:pointer}
.flink:hover{color:#fff}
@keyframes fu{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# session
if 'messages'       not in st.session_state: st.session_state.messages       = []
if 'docs_processed' not in st.session_state: st.session_state.docs_processed = False
if 'rag_engine'     not in st.session_state: st.session_state.rag_engine     = None

# ── SIDEBAR ──────────────────────────────────────────────────────────────────
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

# ── MAIN ─────────────────────────────────────────────────────────────────────
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
