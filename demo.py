# Working properly as expected
# input file : Dnn (data.json)

import streamlit as st
import json
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate,
    ChatPromptTemplate
)

# Streamlit App Title and Description
st.title("Chatbot with Deep learning")
st.write("More info : https://www.youtube.com/kgptalkie")

# Load JSON Dataset Function
def load_dataset(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)

# Load the dataset
dataset = load_dataset("data.json")  

# Initialize LLaMA Model
model = ChatOllama(model="llama3.2:1b", base_url="http://localhost:11434/")
system_message = SystemMessagePromptTemplate.from_template("You are a helpful AI Assistant.")

# Initialize chat history if not present in session state
if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

# Chat form
with st.form("llm-form"):
    text = st.text_area("Enter your question here.")
    submit = st.form_submit_button("Submit")

# Function to generate response based on dataset or model

def generate_response(user_input, chat_history):
    # Check dataset for a match
    for entry in dataset:
        if user_input.lower() in entry["question"].lower():
            return entry["answer"]
    
    # If no match, use LLaMA model
    chat_template = ChatPromptTemplate.from_messages(chat_history)
    chain = chat_template | model | StrOutputParser()
    raw_response = chain.invoke({})
    
    # Ensure response is a string and filter out metadata if present
    if isinstance(raw_response, dict) and 'content' in raw_response:
        response = raw_response['content']
    else:
        # Fallback in case 'content' is not found
        response = str(raw_response)
        
    return response


# Function to retrieve and format chat history
def get_history():
    chat_history = [system_message]
    
    for chat in st.session_state['chat_history']:
        prompt = HumanMessagePromptTemplate.from_template(chat['user'])
        chat_history.append(prompt)

        ai_message = AIMessagePromptTemplate.from_template(chat['assistant'])
        chat_history.append(ai_message)

    return chat_history

# Process user input and generate response
if submit and text:
    with st.spinner("Generating response..."):
        
        # Add user message to history
        prompt = HumanMessagePromptTemplate.from_template(text)
        chat_history = get_history()
        chat_history.append(prompt)

        # Generate and store response
        response = generate_response(text, chat_history)
        st.session_state['chat_history'].append({'user': text, 'assistant': response})

# Display chat history
st.write('## Chat History')
for chat in reversed(st.session_state['chat_history']):
    st.write(f"**:adult: You**: {chat['user']}")
    st.write(f"**:brain: AI Cutie**: {chat['assistant']}")
    st.write("---")
