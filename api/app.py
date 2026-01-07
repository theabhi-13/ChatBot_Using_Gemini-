from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn 
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="LangChain API",
    description="LangChain API",
    version="0.0.1",
)
@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse(url="/docs")

Gemini_model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)
add_routes(
    app,
    Gemini_model,
    path="/geminiai"
)

prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic}"
)
prompt2 = ChatPromptTemplate.from_template(
    "Write me an poem about {topic}"
)

add_routes(
    app,
    prompt1|Gemini_model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000) 