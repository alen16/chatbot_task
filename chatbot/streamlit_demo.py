import openai
import os
import streamlit as st
import numpy as np

st.title("Fist chatbot demo")
openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4"

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "system", "content": "You are a helpful Named Entities assistant."})
    st.session_state.messages.append({"role": "user", "content": "I'll give you a sentence in the following. Please extract entities from the given paragraph without any numbers or amount. Please note that this output contains an array of the extracted entities without any key entity specified."})
    st.session_state.messages.append({"role": "system", "content": "Sure, I can extract entities for you. Please provide the sentence."})


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
max_messages = (
    20  # Counting both user and assistant messages, so 10 iterations of conversation
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
            for response in openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            ):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response) 
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )