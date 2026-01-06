from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Safely set environment variables only if present (avoid assigning None)
gemini_key = os.getenv("GEMINI_API_KEY")
if gemini_key is not None:
    os.environ["GEMINI_API_KEY"] = gemini_key

# LangSmith Tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"
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
st.title("ChatBot using Gemini Pro")
user_input=st.text_input("How can we assist you?")

#Gemini Pro Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

chain = prompt | llm | StrOutputParser()
if user_input:
    response = chain.invoke({"question": user_input})
    st.write(response)
    st.success("Response Generated Successfully!")