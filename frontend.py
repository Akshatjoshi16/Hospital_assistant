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

import streamlit as st
from rag_qa import rag

st.set_page_config(page_title="Hospital Bot", page_icon="🏥", layout="wide")

# ---------- SIDEBAR ----------
st.sidebar.title("🏥 Hospital Assistant")
st.sidebar.markdown("---")
st.sidebar.write("### 📌 Ask about:")
st.sidebar.write("- Patient Admission")
st.sidebar.write("- ICU Protocol")
st.sidebar.write("- Billing Process")
st.sidebar.write("- Emergency Workflow")
st.sidebar.write("- OPD Process")

st.sidebar.markdown("---")
st.sidebar.write("👨‍⚕️ Developed for Hospital Operations Knowledge")

# ---------- MAIN UI ----------
st.title("🏥 Hospital Operations Knowledge Bot")
st.info("💡 Example: 'Explain ICU workflow' or 'How hospital billing works?'")
st.markdown("Ask anything related to hospital workflows and operations")

# ---------- CHAT HISTORY ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------- INPUT ----------
user_input = st.chat_input("Ask your question...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = rag(user_input)
            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})