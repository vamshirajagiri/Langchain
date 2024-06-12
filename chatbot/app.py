# from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")  
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

#prompt template
prompt= ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant please respond to user quries in very seduce and flirting way, be more stylish and talk like a alpha men."),
        ("user", "Question:{question}")
     ]
)

#streamlit framework
st.title("Flirting Assistant")
input_text = st.text_input("Please go ahead & shoot your doubts")

#llm model
model = ChatGroq(model="llama3-8b-8192" , temperature=0.5)
output_parser = StrOutputParser()
chain= prompt | model | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))