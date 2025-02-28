# !pip install sentence-transformers
import json
import requests
from data_dict import *
import re
from langchain_openai import AzureChatOpenAI
from langchain_nvidia import ChatNVIDIA
from langchain_core.messages import HumanMessage, SystemMessage
import os
from langchain_openai import AzureOpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain_astradb import AstraDBVectorStore
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


OPENAI_API_VERSION = os.getenv('OPENAI_API_VERSION')
AZURE_OPENAI_ENDPOINT  = os.getenv('AZURE_OPENAI_ENDPOINT')
AZURE_OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY')
ASTRADB_ENDPOINT =os.getenv('ASTRADB_ENDPOINT')
ASTRADB_TOKEN = os.getenv('ASTRADB_TOKEN')
NVIDIA_API_KEY = os.getenv('NVIDIA_API_KEY')
HUGGINGFACE_TOKEN = os.getenv('HUGGINGFACE_TOKEN')
HUGGINGFACE_URL = os.getenv('HUGGINGFACE_URL')


llm = AzureChatOpenAI(
    azure_deployment="gpt35",
    api_version="2024-02-01",
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    temperature=0,
    max_tokens=4096,
    timeout=None,
    max_retries=2,
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

def get_relevant_data(topics,question):
    docs_retrieved=[]
    embeddings = AzureOpenAIEmbeddings(
        azure_deployment="embeddingada",
        openai_api_version="2024-02-01",
        api_key=AZURE_OPENAI_API_KEY,
        azure_endpoint= AZURE_OPENAI_ENDPOINT
    )
    vector_store = AstraDBVectorStore(
            collection_name="rpf_data",
            embedding=embeddings,
            api_endpoint=ASTRADB_ENDPOINT,
            token=ASTRADB_TOKEN,
            namespace="default_keyspace",
        )
    for topic in topics:
        results = vector_store.similarity_search(
                f"{question}",
                k=3,
                filter={"topic": f"{topic}"},
            )

        docs_retrieved.append(results)

    return docs_retrieved

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
def query_breakdown(query):

    llm = ChatNVIDIA(model="meta/llama-3.1-405b-instruct",temperature=0,
                    nvidia_api_key=NVIDIA_API_KEY)
    messages = [
        SystemMessage(content=f"""You are a helpful assistant in breaking down the customers-provided queries from the NetApp Storage Grid Data Storage Management System.

    You will be provided with a query.You have to provide the output in json format

    Follow the instructions to provide the output.

    1. Understand the question .
    2. break it into multiple questions if required.
    3. Provide the questions as output. STRICTLY Provide the output in json format with only the questions.
        """),
        HumanMessage(content=f"Here is the question:{query}"),
    ]
    chain=llm | StrOutputParser()
    questions=chain.invoke(messages)
    
    result = llm.invoke(f"You are a json extractor. Extract the json data from the given string {questions}.OUTPUT should be STRICTLY in JSON Format. only the text within curly braces")

    
    
    match = re.search(r'```\s*({.*?})\s*```',result.content, re.DOTALL)
    if match:
        extracted_json = match.group(1)
        print(extracted_json)

    queries=json.loads(extracted_json)

    query_list = queries["questions"]

    return query_list


# print(retrieve_docs(r"Vector_data\UseStorageGRID tenant and clients","Does the solution have automatic failure notification via email, text, and other methods?"))

def final_response(docs,query):
    

    prompt=f"""A query/topic is provided along with relevant documents. Your tasks is to answer the query/topic based on the documents provided. 

----------------------------
  query: {query}.
  -----------------------------------
  dcouments: {docs}
  ----------------------------------

Instructions:
1. Be descriptive 
2. Answer only from documents provided
3. Do not use the word "based on documents provided"
    """

    output=llm.invoke(prompt)

    return output







    




