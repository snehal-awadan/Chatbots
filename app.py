# working properly
# simple chatbot
# without any input file

import streamlit as st

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate

st.title("Simple chatbot using Llama3.2 model")
st.write("More info : https://www.youtube.com/kgptalkie")

model = ChatOllama(model="llama3.2:1b", 
                   base_url="http://localhost:11434/")

system_message = SystemMessagePromptTemplate.from_template("You are a helpful AI Assistant.")

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

with st.form("llm-form"):
    text = st.text_area("Enter your question here.")
    submit = st.form_submit_button("Submit")

def generate_response(chat_histroy):
    chat_template = ChatPromptTemplate.from_messages(chat_histroy)

    chain = chat_template|model|StrOutputParser()

    response = chain.invoke({})

    return response


def get_history():
    chat_history = [system_message]
    
    for chat in st.session_state['chat_history']:
        prompt = HumanMessagePromptTemplate.from_template(chat['user'])
        chat_history.append(prompt)

        ai_message = AIMessagePromptTemplate.from_template(chat['assistant'])
        chat_history.append(ai_message)

    return chat_history


if submit and text:
    with st.spinner("Generating response..."):
        
        prompt = HumanMessagePromptTemplate.from_template(text)

        chat_history = get_history()

        chat_history.append(prompt)

        response = generate_response(chat_history)

        st.session_state['chat_history'].append({'user': text, 'assistant': response})


st.write('## Chat History')
for chat in reversed(st.session_state['chat_history']):
       st.write(f"**:adult: You**: {chat['user']}")
       st.write(f"**:brain: AI Cutie**: {chat['assistant']}")
       st.write("---")




