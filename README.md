# Chatbots:

# for the app.py:

# Simple Chatbot using LLaMA 3.2 Model

## Overview
This is a simple chatbot built using the **Streamlit** framework and **LangChain Ollama**. The chatbot leverages the **LLaMA 3.2 1B model** to provide responses based on user queries. The chatbot maintains a chat history and generates responses dynamically.

## Features
- Uses **LLaMA 3.2 1B** as the underlying AI model.
- Built using **Streamlit** for an interactive UI.
- Maintains a chat history for contextual conversations.
- Simple and lightweight, does not require input files.

## Installation
To run this chatbot, ensure you have the required dependencies installed. You can install them using:

pip install streamlit langchain-core langchain-ollama

Additionally, you need to have **Ollama** installed and running locally. Download and set it up from [Ollama's official site](https://ollama.ai/).

## Running the Chatbot
1. Start the Ollama server:
   ollama run llama3.2:1b

2. Run the chatbot script:
   streamlit run chatbot.py

## How It Works
- The chatbot takes user input from a text area.
- It processes the input through a **LangChain prompt template**.
- The **Ollama model** generates a response.
- The chat history is stored and displayed for better context.

## Example Output
```
👤 You: What is AI?
🧠 AI Cutie: AI stands for Artificial Intelligence. It refers to the simulation of human intelligence in machines.
```

## Future Enhancements
- Add support for external knowledge sources (e.g., PDFs, databases).
- Improve response quality with fine-tuned models.
- Deploy the chatbot as a web app using cloud services.


############################################################################################################################################################################################################################################

## For demp.py file:

# Chatbot with Deep Learning and JSON Dataset

## Overview

This chatbot is built using **Streamlit** and **LangChain Ollama**, incorporating a **JSON dataset (data.json)** to provide relevant answers before falling back on the **LLaMA 3.2 1B model**. The chatbot maintains a chat history and generates responses dynamically.

## Features

- Uses **LLaMA 3.2 1B** as the AI model.
- Supports **predefined responses** using a JSON dataset.
- Built using **Streamlit** for an interactive UI.
- Maintains a chat history for contextual conversations.

## Installation

Ensure you have the required dependencies installed by running:
pip install streamlit langchain-core langchain-ollama

Additionally, install and run **Ollama** from [Ollama's official site](https://ollama.ai/).

## Running the Chatbot

1. Start the Ollama server:
   ollama run llama3.2:1b

2. Run the chatbot script:
   streamlit run chatbot.py
  

## How It Works

- The chatbot first searches for an answer in **data.json**.
- If no match is found, it queries the **LLaMA model**.
- Chat history is maintained and displayed.

## JSON Dataset Format (data.json)

```json
[
    {"question": "What is AI?", "answer": "AI stands for Artificial Intelligence..."},
    {"question": "Who invented AI?", "answer": "The concept of AI was introduced by..."}
]
```

## Example Output

```
👤 You: What is AI?
🧠 AI Cutie: AI stands for Artificial Intelligence. It refers to the simulation of human intelligence in machines.
```

## Future Enhancements

- Expand dataset for better accuracy.
- Implement real-time data updates.
- Deploy as a cloud-hosted chatbot.



