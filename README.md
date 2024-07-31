# chatbot_task

# Naive QA Chatbot

## Project Goal
The goal of this project is to create a naive QA (Question-Answering) chatbot using various NLP libraries and tools.

## Installation

### Requirements
To get started, ensure you have the following installed:

1. Python 3.10.11 or higher
2. The required libraries specified in `requirements.txt`

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. Install the required libraries:

   ```bash
   pip install -r requirements.txt

3.Create a secrets.toml file under /cache/chatbot_task/chatbot/.streamlit/ and add your OpenAI API key:

   ```bash
   [secrets]
   OPENAI_API_KEY="sk-XXX"
Replace "sk-XXX" with your actual OpenAI API key.

##Required Libraries
The following libraries are required for the project:

beautifulsoup4==4.12.2
fastapi==0.104.1
gradio==3.24.1
huggingface-hub==0.18.0
langchain==0.0.330
llama-index==0.8.59
nltk==3.8.1
numpy==1.26.1
openai==0.28.1
pandas==2.1.2
streamlit==1.28.1

##Usage
To start the chatbot, run the following command in your terminal:

   ```bash
   streamlit run streamlit_chatbot.py
Make sure to follow the instructions in the app to interact with the QA chatbot.

##Contributing
We welcome contributions! Please submit a pull request or open an issue to discuss your ideas.
