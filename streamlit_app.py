import streamlit as st
from openai import OpenAI 
import PyPDF2
import io

def read_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Show title and description.
st.title("Leytisha's HW 1 App")
st.write(
    "Upload a PDF or a TXT document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)

# Create an OpenAI Client
client = OpenAI(api_key=openai_api_key)