### RFP Response Creation Hackathon

This project involves creating a question answering bot that can provide responses for questions posted by the customer for NetApp Storage Grid.


Have provided an example for the input and output below:
![Alt text](https://github.com/JivitteshS/rpf_response/blob/main/Response%20example.png)


### The project involves following steps:

#### Data Extraction
The Netapp storage grid document pdf is split based on the 8 topics (8 pdfs) present in the document. Each pdf is taken and text, image and tables are extracted from each page and stored locally.For the table and image data we are creating summaries using llama 405b instruct model. the text , image and table summaries are taken for data ingestion.

#### VectorDatabase creation
AstraDB is used for storing the vectordata.The metadata for the data consists of following fields 

* Topic{Topic under which the data is present},
* Type{type of data [text,image,table]},
* Text{the text on which the search will be made {text data/ image summary / table summary },
* Table_json{table data incase if the type of text is table},
* Image_summary{summary of image if the type of text is image}

#### Response creation









