### RFP Response Creation Hackathon

This project involves creating a question answering bot that can provide responses for questions posted by the customer for NetApp Storage Grid. 

### The project involves following steps:

#### 1.Data Extraction
The Netapp storage grid document pdf is split based on the 8 topics (8 pdfs) present in the document. Each pdf is taken and text, image and tables are extracted from each page and stored locally.For the table and image data we are creating summaries using llama model. the text , image and table summaries are taken for data ingestion.

Tools used: Pymupdf , Nvidia AI , pdfplumber , Langchain

#### 2.VectorDatabase creation
AstraDB is used for storing the vectordata.The metadata for the data consists of following fields 

* Topic {Topic under which the data is present}
* Type {type of data [text,image,table]}
* Text {the text on which the search will be made {text data/ image summary / table summary }
* Table_json {table data incase if the type of text is table}
* Image_summary {summary of image if the type of text is image}

Tools used: Astradb, Azure OpenAI Embeddings

#### 3.Response creation

* Query input is split into  multiple subqueries if the input query has multiple topics to it.
* The sub queries are then matched with list of topic summaries using similarity models from hugging face to select a subset of topics to retrieve the metadata(These summaries are representation of the topics in 
  the Storage Grid Document.Each topic has a list of summaries to it).
* Now we search the vectordata with subquery and its sub topics as metadata filter to retreive the documents.
* We then take these documents  with initial query and pass it on to the LLM for generating the final response.

Tools used: Streamlit, Azure OpenAI , Langchain, Hugging face , Nvidia AI

The final query response generator is deployed as streamlit app.



Have provided an example for the input and output below:
![Alt text](https://github.com/JivitteshS/rpf_response/blob/main/Response%20example.png)









