import streamlit as st
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import AzureOpenAI  # Corrected import statement
import pandas as pd
import os
from dotenv import load_dotenv
 
load_dotenv()
 
os.environ["OPENAI_API_BASE"] = os.environ["AZURE_OPENAI_ENDPOINT"] = 'https://aoiaipsi.openai.azure.com/'
os.environ["OPENAI_API_KEY"] = os.environ["AZURE_OPENAI_API_KEY"] = 'f769445c82844edda56668cb92806c21'
os.environ["OPENAI_API_VERSION"] = os.environ["AZURE_OPENAI_API_VERSION"] = 'preview'  # Corrected value
 
os.environ["OPENAI_API_TYPE"] = "azure"
AZURE_OPENAI_NAME = 'gpt-35-turbo-0301'  # Added missing quotes
 
def main():
    st.set_page_config(page_title="Ask your CSV")
 
    st.header("Ask your CSV(agent)")
 
    user_csv = st.file_uploader("Upload your CSV file", type='csv', accept_multiple_files=True)
    data_list = []
 
    if user_csv is not None:
        for f in user_csv:
            data = pd.read_csv(f)
            data_list.append(data)
        if data_list:
            df = pd.concat(data_list,ignore_index=True)
            Ilm = AzureOpenAI(deployment_name=AZURE_OPENAI_NAME, temperature=0)  # Corrected 'temperatur' to 'temperature'
            agent = create_pandas_dataframe_agent(Ilm, df, verbose=True)

         
 
        user_question = st.text_input("ASK YOUR QUESTION:")
 
 
 
            if user_question is not None and user_question != "":
                response = agent.run(user_question)
     
                st.spinner("Generating response.....")
                st.write(response)
 
if __name__ == "__main__":  # Corrected "__main__" with double underscores
    main()
