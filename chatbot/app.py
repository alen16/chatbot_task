from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import gradio as gr
import sys
import os
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
st.session_state["openai_model"] = "gpt-4"

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 4096
    max_chunk_overlap = 0.1
    chunk_size_limit = 8192

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="gpt-4", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(directory_path).load_data()

    index = GPTVectorStoreIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index.save_to_disk('index.json')

    return index

def chatbot(input_text):
    index = GPTVectorStoreIndex.load_from_disk('index.json')
    response = index.query(input_text, response_mode="compact")
    return response.response

iface = gr.Interface(fn=chatbot,
                     inputs=gr.inputs.Textbox(lines=7, label="Enter your text"),
                     outputs="text",
                     title="My AI Chatbot")

index = construct_index("docs")
iface.launch(share=True)