import streamlit as st
from utils.gemini_client import ask_gemini


def chatbot_page():

    st.title("💬 Knowledge Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                f"<div style='background:#1e293b;padding:10px;border-radius:10px;color:white'>{msg['content']}</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div style='background:#0ea5e9;padding:10px;border-radius:10px;color:black'>{msg['content']}</div>",
                unsafe_allow_html=True
            )

    user_input = st.chat_input("Ask anything...")

    if user_input:

        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        context = ""

        for msg in st.session_state.messages:
            context += f"{msg['role']} : {msg['content']}\n"

        response = ask_gemini(context)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        st.rerun()