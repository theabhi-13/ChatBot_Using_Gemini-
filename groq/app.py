import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain.emmbeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core import ChatPromptTemplate
from langchian.chains import create_retrieval_chain 

from dotenv import load_dotenv
load_dotenv()


#load the groq api key
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
