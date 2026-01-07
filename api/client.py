import requests
import streamlit as st


def get_essay(input_text):
    response = requests.post(
        "http://localhost:8000/essay/invoke", json={"input": {"topic": input_text}}
    )
    return response.json()['output']['content']


def get_poem(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke", json={"input": {"topic": input_text}}
    )
    return response.json()['output']['content']

st.title("ChatBot using Gemini Pro")
input_text=st.text_input("Enter Your Essay Topic : ")
input_text2=st.text_input("Enter Your Poem Topic : ")      

if input_text:
    st.write(get_essay(input_text))
    st.success("Response Generated Successfully!")
    
if input_text2:
    st.write(get_poem(input_text2))
    st.success("Response Generated Successfully!")