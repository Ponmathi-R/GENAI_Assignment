import streamlit as st
import requests

st.title("🧠 Dhiya AI")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
prompt = st.chat_input("Ask something...")

if prompt:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Send request to Ollama
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen:0.5b",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]

    # Show assistant response
    st.session_state.messages.append({"role": "assistant", "content": result})
    with st.chat_message("assistant"):
        st.write(result)