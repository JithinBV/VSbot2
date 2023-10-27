import streamlit as st
import pandas as pd
from io import StringIO
import streamlit as st
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import AzureOpenAI


import os

os.environ["OPENAI_API_BASE"] = os.environ["AZURE_OPENAI_ENDPOINT"] = 'https://aoiaipsi.openai.azure.com/'

os.environ["OPENAI_API_KEY"] = os.environ["AZURE_OPENAI_API_KEY"] = 'f769445c82844edda56668cb92806c21'

os.environ["OPENAI_API_VERSION"] = os.environ["AZURE_OPENAI_API_VERSION"] = "2023-07-01-preview" #"2023-03-15-preview"

os.environ["OPENAI_API_TYPE"] = "azure"

AZURE_OPENAI_NAME = 'gpt-35-turbo-0301'

uploaded_files = st.file_uploader("Upload CSV", type="csv", accept_multiple_files=True)
user_question = st.text_input("Your question")
if uploaded_files:
    for file in uploaded_files:
        file.seek(0)
    uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
    raw_data = pd.concat(uploaded_data_read)
    llm = AzureOpenAI(deployment_name=AZURE_OPENAI_NAME, temperature=0)
    agent = create_pandas_dataframe_agent(llm,raw_data,verbose=True)
    
    if raw_data is not None:
        response = agent.run(user_question)
        st.spinner("Generating response.....")
        st.write(response)

    
