from utils import *
import os
from data_dict import sentence_identifier


doc_list=[]

vector_dbs=['Vector_data\\Maintain a Storage Grid', 'Vector_data\\Recovery or Replace Nodes', 'Vector_data\\Install,Upgrade and hotflix StorageGRID', 'Vector_data\\Monitor and troubleshoot a storageGRID system']


question="Does the solution have automatic failure notification via email, text, and other methods?"


docs=retrieve_docs('Vector_data\\Maintain a Storage Grid',question=question)
print("==================")
combined_docs= docs[0].page_content+"\n" +"=================" + "\n" +docs[1].page_content+"\n"+"=================" + "\n"+docs[2].page_content+"\n"+"=================" + "\n"+docs[3].page_content
print("==================")
print(combined_docs)

