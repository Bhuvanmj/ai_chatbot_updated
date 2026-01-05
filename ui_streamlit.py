import streamlit as st
import requests

st.set_page_config(page_title="Chatbot", layout="centered")
st.title("🤖 AI ChatBot - CharMinds")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # prepare messages for backend
    api_messages = [
        {"role": msg["role"], "content": msg["content"]}
        for msg in st.session_state.messages
        if msg["role"] in ["user", "assistant"]
    ]

    with st.spinner("Thinking..."):
        res = requests.post(
            "http://localhost:8000/chat",
            json={"messages": api_messages}
        )
        bot_reply = res.json().get("response", "")
        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply}
        )

# display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
