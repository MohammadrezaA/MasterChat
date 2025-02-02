import streamlit as st
from io import BytesIO
import fitz # PyMuPDF
from openai import OpenAI
from huggingface_hub import InferenceClient

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise EnvironmentError("The OPENAI_API_KEY environment variable is not set.")

client = OpenAI(api_key=api_key)

st.title('Translator')

uploaded_file = st.file_uploader("Upload your PFD", type="pdf")
bt = st.button('Translate')
if uploaded_file and bt:
    pdfdocument = fitz.open(stream = uploaded_file.read(), filetype='pdf')
    for page_num in range(len(pdfdocument)):
        page = pdfdocument[page_num]
        st.markdown(page.get_text('text'))
