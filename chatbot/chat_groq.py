from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Safely set environment variables only if present (avoid assigning None)
groq_key = os.getenv("GROQ_API_KEY")
if groq_key:
    os.environ["GROQ_API_KEY"] = groq_key
else:
    st.info("Please add your GROQ_API_KEY to the .env file")
    st.stop()

# LangSmith Tracing
trace_key = os.getenv("LANGCHAIN_TRACING_V2")
if trace_key is not None:
    os.environ["LANGCHAIN_TRACING_V2"] = trace_key
langchain_key = os.getenv("LANGCHAIN_API_KEY")
if langchain_key is not None:
    os.environ["LANGCHAIN_API_KEY"] = langchain_key

#Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant that helps people find information."),
        ("user","Question: {question}"),  
    ]
)

#Steamlit Framework
st.title("ChatBot using Groq")
user_input=st.text_input("Search Here:")

#Groq Model
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

chain = prompt | llm | StrOutputParser()
if user_input:
    response = chain.invoke({"question": user_input})
    st.write(response)
    st.success("Response Generated Successfully!")