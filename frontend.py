# import streamlit as st
# from rag_qa import rag
# from langchain_core.messages import HumanMessage, AIMessage

# from guardrails import validate_input,validate_output,pii


# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# rag=rag()

# question = st.text_input("Ask a question from your documents")

# if question:
#     if validate_input(question):
#         response = ""
        
#         with st.chat_message("AI"):
#             answer = st.empty() 
            
#             for chunk in rag.stream({
#                     "input": question, 
#                     "chat_history": st.session_state.chat_history
#                 }):
#                 if "answer" in chunk:
#                     response += chunk["answer"]
#                     answer.write(response) 

#         if validate_output(response):
#                st.session_state.chat_history.append(HumanMessage(content=question))
#                st.session_state.chat_history.append(AIMessage(content=response))
              
#         else:
#             st.error("output validation error")

# import streamlit as st
# from rag_qa import rag

# st.set_page_config(page_title="Hospital Bot", page_icon="🏥", layout="wide")

# # ---------- SIDEBAR ----------
# st.sidebar.title("🏥 Hospital Assistant")
# st.sidebar.markdown("---")
# st.sidebar.write("### 📌 Ask about:")
# st.sidebar.write("- Patient Admission")
# st.sidebar.write("- ICU Protocol")
# st.sidebar.write("- Billing Process")
# st.sidebar.write("- Emergency Workflow")
# st.sidebar.write("- OPD Process")

# st.sidebar.markdown("---")
# st.sidebar.write("👨‍⚕️ Developed for Hospital Operations Knowledge")

# # ---------- MAIN UI ----------
# st.title("🏥 Hospital Operations Knowledge Bot")
# st.info("💡 Example: 'Explain ICU workflow' or 'How hospital billing works?'")
# st.markdown("Ask anything related to hospital workflows and operations")

# # ---------- CHAT HISTORY ----------
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # ---------- INPUT ----------
# user_input = st.chat_input("Ask your question...")

# if user_input:
#     # Show user message
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # Get bot response
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             response = rag(user_input)
#             st.markdown(response)

#     st.session_state.messages.append({"role": "assistant", "content": response})
import streamlit as st
from rag_qa import rag

# ─── PAGE CONFIG ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MedCore AI · Hospital Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── GLOBAL CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap');

/* ── Root Variables ── */
:root {
    --bg:          #0a0f1e;
    --surface:     #111827;
    --surface-2:   #1a2235;
    --border:      rgba(99,179,237,0.12);
    --accent:      #38bdf8;
    --accent-glow: rgba(56,189,248,0.18);
    --accent-2:    #34d399;
    --text:        #e2e8f0;
    --text-muted:  #64748b;
    --user-bubble: #1e3a5f;
    --bot-bubble:  #162032;
    --danger:      #f87171;
    --gold:        #fbbf24;
    --font-head:   'DM Serif Display', Georgia, serif;
    --font-body:   'DM Sans', system-ui, sans-serif;
}

/* ── Global Reset ── */
html, body, [class*="css"] {
    font-family: var(--font-body) !important;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 4rem !important;
    max-width: 900px !important;
}

/* ─────────────────────────────────────────────────
   SIDEBAR
───────────────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] > div {
    padding: 1.5rem 1.2rem !important;
}

/* Sidebar logo block */
.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 1.4rem;
}
.sidebar-logo .cross {
    width: 40px; height: 40px;
    background: var(--accent);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px;
    box-shadow: 0 0 18px var(--accent-glow);
    flex-shrink: 0;
}
.sidebar-logo .brand { line-height: 1.1; }
.sidebar-logo .brand-name {
    font-family: var(--font-head) !important;
    font-size: 1.15rem;
    color: var(--text);
    letter-spacing: .5px;
}
.sidebar-logo .brand-sub {
    font-size: 0.7rem;
    color: var(--accent);
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* Sidebar divider */
.s-divider {
    height: 1px;
    background: var(--border);
    margin: 1rem 0;
}

/* Sidebar section label */
.s-label {
    font-size: 0.65rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: .6rem;
    margin-top: .2rem;
}

/* Topic pills */
.topic-pill {
    display: flex;
    align-items: center;
    gap: 9px;
    padding: 9px 12px;
    border-radius: 10px;
    background: var(--surface-2);
    border: 1px solid var(--border);
    margin-bottom: 7px;
    cursor: pointer;
    transition: all .2s;
}
.topic-pill:hover {
    border-color: var(--accent);
    background: var(--accent-glow);
}
.topic-pill .pill-icon {
    font-size: 1rem;
    width: 22px;
    text-align: center;
}
.topic-pill .pill-text {
    font-size: 0.82rem;
    color: var(--text);
    font-weight: 500;
}

/* Sidebar badge */
.sidebar-badge {
    margin-top: 1.2rem;
    padding: 12px 14px;
    background: linear-gradient(135deg, rgba(56,189,248,.08), rgba(52,211,153,.06));
    border: 1px solid rgba(56,189,248,.2);
    border-radius: 12px;
    font-size: 0.78rem;
    color: var(--text-muted);
    line-height: 1.5;
}
.sidebar-badge .badge-head {
    font-weight: 600;
    color: var(--accent-2);
    font-size: 0.8rem;
    margin-bottom: 4px;
}

/* ─────────────────────────────────────────────────
   MAIN HEADER
───────────────────────────────────────────────── */
.main-header {
    text-align: center;
    padding: 1.2rem 0 1rem;
    position: relative;
}
.main-header::before {
    content: '';
    position: absolute;
    top: 0; left: 50%;
    transform: translateX(-50%);
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(56,189,248,0.08) 0%, transparent 70%);
    pointer-events: none;
}
.main-header h1 {
    font-family: var(--font-head) !important;
    font-size: 2.4rem !important;
    font-weight: 400 !important;
    color: var(--text) !important;
    letter-spacing: -.5px;
    margin: 0 0 .2rem !important;
}
.main-header h1 span { color: var(--accent); }
.main-header .subtitle {
    font-size: 0.88rem;
    color: var(--text-muted);
    letter-spacing: .5px;
}
.status-dot {
    display: inline-block;
    width: 7px; height: 7px;
    border-radius: 50%;
    background: var(--accent-2);
    margin-right: 6px;
    box-shadow: 0 0 8px var(--accent-2);
    animation: pulse-dot 2s infinite;
}
@keyframes pulse-dot {
    0%,100% { opacity:1; transform:scale(1); }
    50%      { opacity:.6; transform:scale(1.3); }
}

/* ── Info banner ── */
.info-banner {
    display: flex;
    align-items: center;
    gap: 10px;
    background: linear-gradient(90deg, rgba(56,189,248,.06), rgba(52,211,153,.04));
    border: 1px solid rgba(56,189,248,.18);
    border-left: 3px solid var(--accent);
    border-radius: 10px;
    padding: 10px 14px;
    margin-bottom: 1.2rem;
    font-size: 0.82rem;
    color: var(--text-muted);
}
.info-banner .ib-icon { font-size: 1rem; flex-shrink: 0; }
.info-banner strong { color: var(--accent); }

/* ─────────────────────────────────────────────────
   CHAT MESSAGES
───────────────────────────────────────────────── */
/* Override Streamlit chat containers */
[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
    padding: .25rem 0 !important;
}

/* User message */
[data-testid="stChatMessage"][data-testid*="user"],
div[data-testid="stChatMessageContent"] {
    border-radius: 14px !important;
}

/* Chat bubbles via custom markdown */
.bubble-user {
    background: var(--user-bubble);
    border: 1px solid rgba(99,179,237,.2);
    border-radius: 18px 18px 4px 18px;
    padding: 12px 16px;
    margin-left: auto;
    max-width: 85%;
    font-size: .9rem;
    line-height: 1.6;
    color: var(--text);
    position: relative;
    box-shadow: 0 4px 20px rgba(0,0,0,.3);
}
.bubble-bot {
    background: var(--bot-bubble);
    border: 1px solid var(--border);
    border-radius: 18px 18px 18px 4px;
    padding: 14px 18px;
    max-width: 90%;
    font-size: .9rem;
    line-height: 1.7;
    color: var(--text);
    box-shadow: 0 4px 20px rgba(0,0,0,.3);
}
.bubble-bot p:last-child, .bubble-user p:last-child { margin-bottom: 0; }

/* Avatars */
.avatar {
    width: 32px; height: 32px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: .95rem;
    flex-shrink: 0;
}
.avatar-user { background: var(--user-bubble); border: 1px solid rgba(99,179,237,.3); }
.avatar-bot  {
    background: var(--accent);
    box-shadow: 0 0 12px var(--accent-glow);
}

.msg-row {
    display: flex;
    align-items: flex-end;
    gap: 10px;
    margin-bottom: 16px;
}
.msg-row.user-row { flex-direction: row-reverse; }

/* Timestamp */
.msg-time {
    font-size: .65rem;
    color: var(--text-muted);
    margin-top: 4px;
    letter-spacing: .5px;
}
.user-row .msg-time { text-align: right; }

/* Welcome card */
.welcome-card {
    text-align: center;
    padding: 2.5rem 1.5rem;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 20px;
    margin: 1.5rem 0;
}
.welcome-icon {
    font-size: 3rem;
    margin-bottom: .8rem;
    filter: drop-shadow(0 0 16px rgba(56,189,248,.4));
}
.welcome-card h3 {
    font-family: var(--font-head) !important;
    font-size: 1.5rem !important;
    font-weight: 400 !important;
    color: var(--text) !important;
    margin-bottom: .5rem !important;
}
.welcome-card p {
    font-size: .85rem;
    color: var(--text-muted);
    max-width: 440px;
    margin: 0 auto .8rem;
    line-height: 1.6;
}
.chip-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
    margin-top: 1rem;
}
.chip {
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 5px 12px;
    font-size: .78rem;
    color: var(--text-muted);
    transition: all .2s;
}

/* ─────────────────────────────────────────────────
   CHAT INPUT AREA
───────────────────────────────────────────────── */
[data-testid="stChatInput"] {
    background: var(--surface) !important;
    border: 1px solid rgba(99,179,237,.25) !important;
    border-radius: 16px !important;
    box-shadow: 0 0 24px rgba(56,189,248,.06) !important;
    transition: border-color .2s, box-shadow .2s !important;
}
[data-testid="stChatInput"]:focus-within {
    border-color: var(--accent) !important;
    box-shadow: 0 0 32px rgba(56,189,248,.14) !important;
}
[data-testid="stChatInput"] textarea {
    background: transparent !important;
    color: var(--text) !important;
    font-family: var(--font-body) !important;
    font-size: .9rem !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: var(--text-muted) !important; }
[data-testid="stChatInput"] button {
    background: var(--accent) !important;
    border-radius: 10px !important;
    color: var(--bg) !important;
}

/* Spinner */
[data-testid="stSpinner"] > div { color: var(--accent) !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--surface-2); border-radius: 4px; }

/* Streamlit default chat avatar overrides */
[data-testid="chatAvatarIcon-user"] svg { fill: var(--accent) !important; }
[data-testid="chatAvatarIcon-assistant"] { background: var(--accent) !important; border-radius: 50% !important; }

</style>
""", unsafe_allow_html=True)


# ─── SIDEBAR ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="cross">🏥</div>
        <div class="brand">
            <div class="brand-name">MedCore AI</div>
            <div class="brand-sub">Hospital Assistant</div>
        </div>
    </div>
    <div class="s-divider"></div>
    <div class="s-label">Quick Topics</div>
    <div class="topic-pill"><span class="pill-icon">🛏️</span><span class="pill-text">Patient Admission</span></div>
    <div class="topic-pill"><span class="pill-icon">💊</span><span class="pill-text">ICU Protocol</span></div>
    <div class="topic-pill"><span class="pill-icon">🧾</span><span class="pill-text">Billing Process</span></div>
    <div class="topic-pill"><span class="pill-icon">🚨</span><span class="pill-text">Emergency Workflow</span></div>
    <div class="topic-pill"><span class="pill-icon">🏛️</span><span class="pill-text">OPD Process</span></div>
    <div class="topic-pill"><span class="pill-icon">🔬</span><span class="pill-text">Lab & Diagnostics</span></div>
    <div class="s-divider"></div>
    <div class="sidebar-badge">
        <div class="badge-head">⚡ Powered by RAG</div>
        Built for hospital staff to query internal SOPs, workflows, and operational knowledge in seconds.
    </div>
    """, unsafe_allow_html=True)


# ─── MAIN HEADER ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>Hospital <span>Knowledge</span> Bot</h1>
    <p class="subtitle"><span class="status-dot"></span>AI-Powered · Real-time · Always Available</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-banner">
    <span class="ib-icon">💡</span>
    <span>Try: <strong>"Explain ICU admission steps"</strong> · <strong>"What is the billing workflow?"</strong> · <strong>"OPD registration process"</strong></span>
</div>
""", unsafe_allow_html=True)


# ─── CHAT HISTORY STATE ───────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []


# ─── WELCOME SCREEN ───────────────────────────────────────────────────────────
if not st.session_state.messages:
    st.markdown("""
    <div class="welcome-card">
        <div class="welcome-icon">🏥</div>
        <h3>How can I assist you today?</h3>
        <p>I'm trained on your hospital's operational knowledge — workflows, protocols, billing, and more. Ask me anything.</p>
        <div class="chip-row">
            <span class="chip">🛏️ Admission</span>
            <span class="chip">💊 ICU Protocol</span>
            <span class="chip">🚨 Emergency</span>
            <span class="chip">🧾 Billing</span>
            <span class="chip">🏛️ OPD</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─── RENDER CHAT MESSAGES ────────────────────────────────────────────────────
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ─── CHAT INPUT ───────────────────────────────────────────────────────────────
user_input = st.chat_input("Ask about hospital workflows, protocols, billing…")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base…"):
            response = rag(user_input)
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})