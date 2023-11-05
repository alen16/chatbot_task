import openai
import os
import streamlit as st
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

st.title("Ubiquiti chatbot demo")
openai.api_key = st.secrets["OPENAI_API_KEY"]

documents = SimpleDirectoryReader('docs').load_data()
index = GPTVectorStoreIndex.from_documents(documents)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
max_messages = (
    100  # Counting both user and assistant messages, so 10 iterations of conversation
)

if len(st.session_state.messages) > max_messages:
    st.info("Notice: You reached the limit for the demo version. Please refresh the website and try again!")

else:
    if prompt := st.chat_input("Say something"):
        st.session_state.messages.append({"role": 'user', "content": prompt})
        with st.chat_message("user"):
                st.markdown(prompt)
        
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            query_engine = index.as_query_engine()
            response = query_engine.query(prompt)
            full_response += response.response
            message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response) 
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )