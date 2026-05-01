"""All CSS styles for Research Studio UI."""

MAIN_CSS = """
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,600;1,300&family=Syne:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>
/* ── VARIABLES ── */
:root {
  --bg:         #080c12;
  --sidebar-bg: #0a0f16;
  --card:       #0f1520;
  --card2:      #131b28;
  --card3:      #182333;
  --border:     rgba(0,188,212,0.08);
  --border-hi:  rgba(0,188,212,0.28);
  --cyan:       #00bcd4;
  --cyan-dim:   rgba(0,188,212,0.06);
  --cyan-glow:  rgba(0,188,212,0.18);
  --text:       #c8d8e8;
  --text-mid:   #6a8099;
  --text-dim:   #3a4f62;
  --green:      #00e5a0;
  --red:        #ff5370;
  --purple:     #c792ea;
  --font-mono:  'JetBrains Mono', monospace;
  --font-head:  'Syne', sans-serif;
}

/* ── RESET ── */
#MainMenu, footer, header { visibility: hidden !important; display: none !important; }
*, *::before, *::after { box-sizing: border-box; }
html, body, .stApp {
  background: var(--bg) !important;
  font-family: var(--font-mono) !important;
  color: var(--text) !important;
}

/* ── LAYOUT FIX — No overlapping ── */
section.main > div { padding: 0 !important; }
.block-container {
  padding: 0 !important;
  max-width: 100% !important;
  overflow-x: hidden;
}
.stApp > header { display: none !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
  background: var(--sidebar-bg) !important;
  border-right: 1px solid var(--border) !important;
  z-index: 100;
}
[data-testid="stSidebar"] > div:first-child {
  padding: 0 !important;
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow-y: auto;
  overflow-x: hidden;
}
[data-testid="stSidebar"] .block-container { padding: 0 !important; }
[data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] { gap: 0 !important; }

/* ── BRAND ── */
.brand-wrap {
  padding: 1.6rem 1.4rem 1.3rem;
  border-bottom: 1px solid var(--border);
  background: linear-gradient(180deg, rgba(0,188,212,0.03) 0%, transparent 100%);
}
.brand-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
.brand-icon {
  width: 38px; height: 38px;
  background: linear-gradient(135deg, rgba(0,188,212,0.12), rgba(0,188,212,0.04));
  border: 1px solid var(--border-hi);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  color: var(--cyan);
  animation: iconPulse 3s ease-in-out infinite;
}
@keyframes iconPulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(0,188,212,0); }
  50% { box-shadow: 0 0 12px 2px rgba(0,188,212,0.15); }
}
.brand-name {
  font-family: var(--font-head);
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--cyan);
  line-height: 1.2;
  letter-spacing: -0.01em;
}
.brand-sub {
  font-size: 0.52rem;
  letter-spacing: 0.2em;
  color: var(--text-dim);
  margin-top: 0.15rem;
  text-transform: uppercase;
}

/* ── SIDEBAR SECTIONS ── */
.sb-section {
  padding: 1rem 1.3rem 0;
}
.sb-label {
  font-size: 0.52rem;
  letter-spacing: 0.16em;
  color: var(--text-dim);
  text-transform: uppercase;
  margin-bottom: 0.6rem;
  font-weight: 500;
}
.sb-divider {
  height: 1px;
  background: var(--border);
  margin: 0.8rem 0;
}

/* ── NAV ITEMS ── */
.nav-list { padding: 0; }
.nav-item {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  padding: 0.55rem 1.3rem;
  font-size: 0.72rem;
  color: var(--text-mid);
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  border-left: 2px solid transparent;
  letter-spacing: 0.04em;
  position: relative;
  overflow: hidden;
}
.nav-item::before {
  content: '';
  position: absolute;
  left: 0; top: 0;
  width: 0; height: 100%;
  background: linear-gradient(90deg, rgba(0,188,212,0.08), transparent);
  transition: width 0.3s ease;
}
.nav-item:hover::before { width: 100%; }
.nav-item:hover { color: var(--text); }
.nav-item.active {
  color: var(--cyan);
  border-left-color: var(--cyan);
  background: linear-gradient(90deg, rgba(0,188,212,0.06), transparent);
}
.nav-icon { font-size: 0.85rem; width: 20px; text-align: center; flex-shrink: 0; }

/* ── STATUS ── */
.status-wrap { padding: 0.6rem 1.3rem; }
.status-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.56rem;
  letter-spacing: 0.1em;
  padding: 0.25rem 0.7rem;
  border-radius: 99px;
  font-weight: 500;
  text-transform: uppercase;
}
.status-pill.ready {
  background: rgba(0,229,160,0.06);
  color: var(--green);
  border: 1px solid rgba(0,229,160,0.18);
}
.status-pill.idle {
  background: var(--cyan-dim);
  color: var(--cyan);
  border: 1px solid rgba(0,188,212,0.15);
}
.dot {
  width: 5px; height: 5px;
  border-radius: 50%;
  background: currentColor;
  animation: blink 1.8s ease-in-out infinite;
}
@keyframes blink { 0%,100%{opacity:1}50%{opacity:0.15} }

/* ── PROFILE ── */
.profile-card {
  padding: 1rem 1.3rem;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 0.7rem;
  margin-top: auto;
}
.profile-avatar {
  width: 34px; height: 34px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--cyan), #006878);
  display: flex; align-items: center; justify-content: center;
  font-size: 0.7rem; font-weight: 700; color: var(--bg);
  flex-shrink: 0;
  box-shadow: 0 0 10px rgba(0,188,212,0.15);
}
.profile-name { font-size: 0.7rem; font-weight: 500; color: var(--text); letter-spacing: 0.02em; }
.profile-role { font-size: 0.55rem; color: var(--text-dim); letter-spacing: 0.06em; margin-top: 0.1rem; }

/* ── TOPBAR ── */
.topbar {
  padding: 1rem 2rem;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: linear-gradient(180deg, rgba(0,188,212,0.02), transparent);
  position: sticky;
  top: 0;
  z-index: 50;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}
.topbar-title {
  font-family: var(--font-head);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--cyan);
}
.topbar-badge {
  font-size: 0.56rem;
  letter-spacing: 0.1em;
  color: var(--text-mid);
  background: var(--card2);
  border: 1px solid var(--border);
  padding: 0.3rem 0.8rem;
  border-radius: 99px;
  text-transform: uppercase;
}

/* ── CHAT CONTAINER ── */
.chat-area {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 1.5rem 6rem;
  min-height: calc(100vh - 140px);
}

/* ── EMPTY STATE ── */
.empty-state {
  text-align: center;
  padding: 4rem 2rem;
  animation: fadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
}
.empty-icon {
  font-size: 3rem;
  opacity: 0.2;
  margin-bottom: 1.5rem;
  animation: float 4s ease-in-out infinite;
}
@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}
.empty-title {
  font-family: var(--font-head);
  font-size: 1.2rem;
  font-weight: 500;
  color: var(--text-mid);
  margin-bottom: 0.6rem;
  letter-spacing: 0.02em;
}
.empty-desc {
  font-size: 0.72rem;
  color: var(--text-dim);
  line-height: 2;
  letter-spacing: 0.03em;
  max-width: 400px;
  margin: 0 auto;
}

/* ── QUICK TIPS CARDS ── */
.tips-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.8rem;
  margin-top: 2rem;
  max-width: 560px;
  margin-left: auto;
  margin-right: auto;
}
.tip-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 1rem;
  text-align: left;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  animation: fadeUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) both;
}
.tip-card:nth-child(1) { animation-delay: 0.1s; }
.tip-card:nth-child(2) { animation-delay: 0.2s; }
.tip-card:nth-child(3) { animation-delay: 0.3s; }
.tip-card:hover {
  border-color: var(--border-hi);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.3), 0 0 0 1px rgba(0,188,212,0.1);
}
.tip-step {
  font-size: 0.5rem;
  letter-spacing: 0.15em;
  color: var(--cyan);
  text-transform: uppercase;
  margin-bottom: 0.4rem;
  font-weight: 600;
}
.tip-text {
  font-size: 0.62rem;
  color: var(--text-mid);
  line-height: 1.6;
  letter-spacing: 0.03em;
}

/* ── USER MESSAGE ── */
.msg-user {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 1.5rem;
  animation: slideInRight 0.4s cubic-bezier(0.16, 1, 0.3, 1) both;
}
@keyframes slideInRight {
  from { opacity: 0; transform: translateX(20px); }
  to   { opacity: 1; transform: translateX(0); }
}
.msg-user-inner { max-width: 65%; }
.msg-user-bubble {
  background: linear-gradient(135deg, var(--card2), var(--card3));
  border: 1px solid var(--border);
  border-radius: 14px 14px 4px 14px;
  padding: 0.9rem 1.15rem;
  font-size: 0.8rem;
  line-height: 1.75;
  color: var(--text);
  position: relative;
  overflow: hidden;
}
.msg-user-bubble::before {
  content: '';
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: linear-gradient(135deg, rgba(0,188,212,0.02), transparent);
  pointer-events: none;
}
.msg-ts {
  font-size: 0.5rem;
  letter-spacing: 0.12em;
  color: var(--text-dim);
  text-align: right;
  margin-top: 0.35rem;
  text-transform: uppercase;
}

/* ── AI MESSAGE ── */
.msg-ai {
  margin-bottom: 1.8rem;
  animation: slideInLeft 0.5s cubic-bezier(0.16, 1, 0.3, 1) both;
}
@keyframes slideInLeft {
  from { opacity: 0; transform: translateX(-20px); }
  to   { opacity: 1; transform: translateX(0); }
}
.msg-ai-head {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}
.msg-ai-dot {
  width: 22px; height: 22px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(0,188,212,0.15), rgba(0,188,212,0.05));
  border: 1px solid var(--border-hi);
  display: flex; align-items: center; justify-content: center;
  font-size: 0.55rem;
  color: var(--cyan);
}
.msg-ai-label {
  font-size: 0.55rem;
  letter-spacing: 0.18em;
  color: var(--cyan);
  text-transform: uppercase;
  font-weight: 600;
}
.msg-ai-bubble {
  background: var(--card);
  border: 1px solid var(--border);
  border-left: 3px solid var(--cyan);
  border-radius: 0 12px 12px 12px;
  padding: 1.15rem 1.4rem;
  font-size: 0.8rem;
  line-height: 1.9;
  color: var(--text);
  font-weight: 300;
  position: relative;
  overflow: hidden;
}
.msg-ai-bubble::after {
  content: '';
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 2px;
  background: linear-gradient(90deg, var(--cyan), transparent);
  opacity: 0.3;
}

/* ── WORD HIGHLIGHT ANIMATION ── */
.ai-word {
  display: inline;
  opacity: 0;
  animation: wordReveal 0.3s ease forwards;
  color: var(--text);
}
@keyframes wordReveal {
  0%   { opacity: 0; color: var(--cyan); text-shadow: 0 0 8px rgba(0,188,212,0.4); }
  60%  { opacity: 1; color: var(--cyan); text-shadow: 0 0 4px rgba(0,188,212,0.2); }
  100% { opacity: 1; color: var(--text); text-shadow: none; }
}

/* ── CITATIONS ── */
.cite-row {
  margin-top: 0.9rem;
  padding-top: 0.75rem;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 0.45rem;
  flex-wrap: wrap;
}
.cite-label {
  font-size: 0.55rem;
  letter-spacing: 0.1em;
  color: var(--text-dim);
  text-transform: uppercase;
}
.cite-chip {
  font-size: 0.55rem;
  letter-spacing: 0.06em;
  color: var(--cyan);
  background: var(--cyan-dim);
  border: 1px solid rgba(0,188,212,0.15);
  padding: 0.2rem 0.55rem;
  border-radius: 5px;
  transition: all 0.2s;
  cursor: pointer;
}
.cite-chip:hover {
  background: rgba(0,188,212,0.12);
  border-color: var(--cyan);
  box-shadow: 0 0 8px rgba(0,188,212,0.15);
}

/* ── THINKING / LOADING ── */
.thinking-wrap {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.6rem 0 1rem;
  animation: fadeUp 0.3s ease both;
}
.thinking-text {
  font-size: 0.62rem;
  letter-spacing: 0.14em;
  color: var(--cyan);
  text-transform: uppercase;
}
.think-dots { display: flex; gap: 3px; }
.think-dots span {
  width: 4px; height: 4px;
  border-radius: 50%;
  background: var(--cyan);
  animation: dotBounce 1.4s ease-in-out infinite;
}
.think-dots span:nth-child(2) { animation-delay: 0.15s; }
.think-dots span:nth-child(3) { animation-delay: 0.3s; }
@keyframes dotBounce {
  0%, 80%, 100% { transform: translateY(0); opacity: 0.3; }
  40% { transform: translateY(-6px); opacity: 1; }
}

/* ── FOOTER ── */
.app-footer {
  border-top: 1px solid var(--border);
  padding: 0.8rem 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--sidebar-bg);
}
.footer-credit {
  font-size: 0.55rem;
  letter-spacing: 0.12em;
  color: var(--text-dim);
  text-transform: uppercase;
}
.footer-credit span { color: var(--cyan); }
.footer-links { display: flex; gap: 1.5rem; }
.footer-link {
  font-size: 0.55rem;
  letter-spacing: 0.1em;
  color: var(--text-dim);
  text-transform: uppercase;
  cursor: pointer;
  transition: color 0.2s;
}
.footer-link:hover { color: var(--cyan); }

/* ── ANIMATIONS ── */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes shimmer {
  0%   { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

/* ── AMBIENT GLOW ── */
.ambient-glow {
  position: fixed;
  top: -200px;
  right: -200px;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(0,188,212,0.04) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
  animation: ambientDrift 12s ease-in-out infinite alternate;
}
@keyframes ambientDrift {
  0%   { transform: translate(0, 0); }
  100% { transform: translate(-60px, 60px); }
}

/* ── STREAMLIT OVERRIDES ── */
.stTextInput > div > div {
  background: var(--card2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 8px !important;
  transition: all 0.25s !important;
}
.stTextInput > div > div:focus-within {
  border-color: var(--border-hi) !important;
  box-shadow: 0 0 0 3px var(--cyan-dim), 0 0 16px rgba(0,188,212,0.08) !important;
}
.stTextInput input {
  font-family: var(--font-mono) !important;
  font-size: 0.78rem !important;
  color: var(--text) !important;
  background: transparent !important;
  letter-spacing: 0.04em !important;
}
.stTextInput input::placeholder { color: var(--text-dim) !important; }
.stTextInput label {
  font-family: var(--font-mono) !important;
  font-size: 0.55rem !important;
  letter-spacing: 0.12em !important;
  color: var(--text-dim) !important;
  text-transform: uppercase !important;
}

[data-testid="stFileUploader"] {
  background: linear-gradient(135deg, rgba(0,188,212,0.04), rgba(0,188,212,0.02)) !important;
  border: 1px dashed var(--border-hi) !important;
  border-radius: 10px !important;
  transition: all 0.3s !important;
}
[data-testid="stFileUploader"]:hover {
  border-color: var(--cyan) !important;
  box-shadow: 0 0 20px rgba(0,188,212,0.08) !important;
}
[data-testid="stFileUploader"] label,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p {
  font-family: var(--font-mono) !important;
  font-size: 0.68rem !important;
  color: var(--text-mid) !important;
}

.stButton > button {
  width: 100% !important;
  background: linear-gradient(135deg, rgba(0,188,212,0.08), rgba(0,188,212,0.03)) !important;
  color: var(--cyan) !important;
  border: 1px solid var(--border-hi) !important;
  font-family: var(--font-mono) !important;
  font-size: 0.6rem !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  border-radius: 8px !important;
  padding: 0.6rem 1rem !important;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
  position: relative !important;
  overflow: hidden !important;
}
.stButton > button:hover {
  background: rgba(0,188,212,0.12) !important;
  border-color: var(--cyan) !important;
  box-shadow: 0 0 20px rgba(0,188,212,0.15), 0 4px 12px rgba(0,0,0,0.3) !important;
  transform: translateY(-1px) !important;
}
.stButton > button:active {
  transform: translateY(0) !important;
}

[data-testid="stChatInput"] {
  background: var(--card) !important;
  border: 1px solid var(--border) !important;
  border-radius: 12px !important;
  transition: all 0.3s !important;
}
[data-testid="stChatInput"]:focus-within {
  border-color: var(--border-hi) !important;
  box-shadow: 0 0 0 3px var(--cyan-dim), 0 -4px 20px rgba(0,188,212,0.06) !important;
}
[data-testid="stChatInput"] textarea {
  font-family: var(--font-mono) !important;
  font-size: 0.8rem !important;
  color: var(--text) !important;
  background: transparent !important;
  letter-spacing: 0.03em !important;
}
[data-testid="stChatInput"] textarea::placeholder {
  color: var(--text-dim) !important;
  font-style: italic !important;
}
[data-testid="stChatInput"] button {
  background: var(--cyan) !important;
  border-radius: 8px !important;
}

.stAlert {
  border-radius: 8px !important;
  font-family: var(--font-mono) !important;
  font-size: 0.68rem !important;
}

[data-testid="metric-container"] {
  background: var(--card2) !important;
  border: 1px solid var(--border) !important;
  border-radius: 8px !important;
  padding: 0.75rem !important;
}
[data-testid="stMetricLabel"] {
  font-family: var(--font-mono) !important;
  font-size: 0.52rem !important;
  letter-spacing: 0.1em !important;
  color: var(--text-dim) !important;
  text-transform: uppercase !important;
}
[data-testid="stMetricValue"] {
  font-family: var(--font-head) !important;
  font-size: 1.3rem !important;
  color: var(--text) !important;
}

[data-testid="stExpander"] {
  background: var(--card) !important;
  border: 1px solid var(--border) !important;
  border-radius: 8px !important;
}
[data-testid="stExpander"] summary {
  font-family: var(--font-mono) !important;
  font-size: 0.62rem !important;
  color: var(--text-mid) !important;
  letter-spacing: 0.08em !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 3px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(0,188,212,0.15); border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: var(--cyan); }

/* ── SCANLINE EFFECT ── */
.scanline {
  position: fixed;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--cyan), transparent);
  opacity: 0.06;
  animation: scanMove 8s linear infinite;
  pointer-events: none;
  z-index: 999;
}
@keyframes scanMove {
  0%   { top: 0; }
  100% { top: 100vh; }
}
</style>
"""
