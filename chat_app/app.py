import streamlit as st
from reply import reply

if "history" not in st.session_state:
    st.session_state["history"] = []

def append_msg(msg,sender,chunks=None):
    st.session_state["history"].append({
        "name": sender,
        "text": msg,
        "chunks": chunks
    })

avatar = {
    "user": "🤓",
    "assistant": "🦜"
}


history = st.session_state["history"]
message = st.chat_input("say something...")
if message:
    append_msg(message,"user")
    text,chunks = reply(history)
    append_msg(text, "assistant", chunks)

for msg in history:
    with st.chat_message(msg["name"], avatar=avatar[msg["name"]]):
        st.write(msg["text"])

    

