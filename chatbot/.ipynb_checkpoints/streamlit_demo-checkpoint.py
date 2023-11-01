import openai
import os
import streamlit as st
import numpy as np

openai.api_key = "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"

messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "I'll give you a sentence in the following. Please extract entities from the given paragraph without any numbers or amount. Please note that this output contains an array of the extracted entities without any key entity specified."},
            {"role": "system", "content": "Sure, I can extract entities for you. Please provide the sentence."}
] 

def update_messages(messages=[], role='user', content=''):
    messages.append({"role": role, "content": content})
    return messages

def call_chat_gpt(messages=[]):
    if messages:
        #print(messages)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=True
        )
    return response

st.title("ChatGPT demo")

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

        messages = update_messages(messages, 'user', prompt)
        response = call_chat_gpt(messages)

        if 'choices' in response:
            with st.chat_message(response['choices'][0]['message']['role']):
                st.write(response['choices'][0]['message']['content'])

            messages = update_messages(messages, response['choices'][0]['message']['role'], response['choices'][0]['message']['content'])