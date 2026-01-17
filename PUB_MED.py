from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

from env import GOOGLE_API_KEY
from langchain_classic.chains import RetrievalQA
API_KEY = GOOGLE_API_KEY

llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash',google_api_key=API_KEY,temperature=0.3)

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
## Front End Streamlit App

st.title("BioCure Intelligence")

desease = st.text_input("Deases: ")

urls = ['https://pubmed.ncbi.nlm.nih.gov/',f"https://pubmed.ncbi.nlm.nih.gov/?term={desease}"]

loader = UnstructuredURLLoader(urls=urls)
data = loader.load()

spliter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=150)
docs = spliter.split_documents(data)

vectors = Chroma.from_documents(documents=docs,embedding=embedding)

retriver = vectors.as_retriever(search_type ='similarity' ,search_kwargs={'k':6})

response = RetrievalQA.from_chain_type(llm=llm,chain_type='stuff',retriever=retriver)

result = response.invoke(desease)
if desease:
    st.write((result['result']))

    hindi = response.invoke(f"translate {result} in hindi")
    st.write(hindi['result'])
    
