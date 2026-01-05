import streamlit as st
import asyncio
from groq_chat import ask_groq

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

    with st.spinner("Thinking..."):
        # Directly call OpenRouter (NO FastAPI, NO localhost)
        reply = asyncio.run(
            ask_groq(st.session_state.messages)
        )

        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
