# !pip install sentence-transformers
import json
import requests
from data_dict import *
from langgraph.graph import StateGraph
from typing import TypedDict, List, Annotated
from langchain_openai import AzureChatOpenAI
import operator
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langgraph.graph import END
from langchain_core.messages import HumanMessage, SystemMessage
import os
# from langchain_community.document_loaders import WebBaseLoader
from langgraph.graph import END, StateGraph, START
from langchain_openai import AzureOpenAIEmbeddings
# from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from typing import List
from langchain_community.vectorstores import FAISS
from typing_extensions import TypedDict
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate



os.environ["OPENAI_API_VERSION"] = "2024-02-01"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://expazure-openai.openai.azure.com/"
os.environ["AZURE_OPENAI_API_KEY"] = "0f5cb3c2ad3d40d9a76142c3f49cad9f"

llm = AzureChatOpenAI(
    azure_deployment="gpt35",
    api_version="2024-02-01",
    temperature=0,
    max_tokens=2000,
    timeout=None,
    max_retries=2,
    )




embeddings = AzureOpenAIEmbeddings(
    azure_deployment="embeddingada",
    openai_api_version="2024-02-01",
)
api_token="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"
API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/msmarco-distilbert-base-tas-b"
headers = {"Authorization": f"Bearer {api_token}"}



def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def get_key_from_value(d, value):
    for key, val in d.items():
        if val == value:
            return key
    return None 



# FInd the list of topics that can contain the answer for the user query
def topic_finder(question,topics):

    data = query(
        {
            "inputs": {
                "source_sentence":question,
                "sentences":topics
            }
        })
    print(len(data))
    data_Score=[]

    for i in range(0,len(data)):
        data_Score.append((data[i],topics[i]))

    # Sort the list of tuples by the first element in descending order
    data_ = sorted(data_Score, key=lambda x: x[0], reverse=True)

    # Extract the top 3 values and sentences
    top_10 = data_[:80]
    list_subtopics=[top_10[i][1] for i in range(0,5)]
    
    topic_list=[]
    for i in storagegrid_dict.values():
        for j in list_subtopics:
            if j in i:
                topic_list.append(get_key_from_value(storagegrid_dict,i))
    
    return list(set(topic_list))

# print(topic_finder(question="abcd",topics=sentence_identifier))

def query_fromer(question):
    messages = [
        SystemMessage(content=f"""You are a question reinterpreter.The queries are provided by Customers to NetApp Storage Grid
        a Data Storage Management System.
            
            --If the provided question is not properly formed, then form a proper question out of the input.
            --If the provided question is given as a proper query then return the output as it is.
            --DO NOT loose information from the input
            
            Output: Return only the reformed question as the output.
            """),
        HumanMessage(content=f"Here is the question:{question}"),
    ]
                    

    chain=llm | StrOutputParser()

    output=chain.invoke(messages)

    return output



def vector_db(topic):

    topic_vectordb_dict={"Configure and Manage a StorageGRID": r"Vector_data\Configure and manage a storageGRID system",
                         "Expand a StorageGRID": r"Vector_data\Expand a Grid",
                         "Install, Upgrade and Hotfix StorageGRID" : r"Vector_data\Install,Upgrade and hotflix StorageGRID",
                         "Maintain a StorageGRID": r"Vector_data\Maintain a Storage Grid",
                         "Monitor and Troubleshoot a StorageGRID":r"Vector_data\Monitor and troubleshoot a storageGRID system",
                      "Recovery or Replace Nodes" :r"Vector_data\Recovery or Replace Nodes",
                     "Use StorageGRID Tenants and Clients": r"Vector_data\UseStorageGRID tenant and clients"
                           }

    vector_db=topic_vectordb_dict.get(topic)

    return vector_db

# print(vector_db("Recovery or Replace Nodes"))


def retrieve_docs(vector_db,question):
    
    database=FAISS.load_local(vector_db,embeddings,allow_dangerous_deserialization=True)
    
    retriever=database.as_retriever()
    
    docs = retriever.get_relevant_documents(question)
    
    documents=[docs[i] for i in range(0,4)]
    
    return documents

# print(retrieve_docs(r"Vector_data\UseStorageGRID tenant and clients","Does the solution have automatic failure notification via email, text, and other methods?"))

def final_response(docs,query):

    prompt=f"""----------------------------
    This is the query: {query}.
    -----------------------------------
    These are the dcouments: {docs}
    ----------------------------------
    Answer the query based on the provided documents.Do not asnwer things on your own.Answer only from the data provided.    
    """
    llm = AzureChatOpenAI(
    deployment_name="gpt35",
                )
    output=llm.invoke(prompt)

    return output






    




