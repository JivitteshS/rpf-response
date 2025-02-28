
# RFP Response Creation Hackathon

This project involves creating a **question-answering bot** that provides responses for customer-posted questions related to **NetApp Storage Grid**. The solution leverages document processing, vector databases, and advanced language models to generate high-quality responses.

---


Have provided an example for the input and output below:
![Alt text](https://github.com/JivitteshS/rpf_response/blob/main/Response%20example.png)

---

## 📁 Project Structure

```
rpf_Response/
├── Code/
│   ├── main.py
│   ├── utils.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🚀 Project Overview

### 1. Data Extraction

The **NetApp Storage Grid** document (PDF) is split into 8 topics (resulting in 8 PDFs). Each page of these PDFs is processed to extract:

- **Text**
- **Images**
- **Tables**

For images and tables, summaries are generated using **LLaMA models**. These extracted and summarized pieces of content are stored locally for further use.

**Tools Used:**  
- Pymupdf  
- Nvidia AI  
- pdfplumber  
- Langchain  

---

### 2. Vector Database Creation

All extracted content (text, image summaries, table summaries) is ingested into **AstraDB**, stored as vectors with rich metadata for efficient retrieval.

| Metadata Field | Description |
|---|---|
| **Topic** | The topic under which the data falls |
| **Type** | Type of data (`text`, `image`, `table`) |
| **Text** | Text content (includes extracted text, image summaries, table summaries) |
| **Table_json** | JSON representation of table data (only for `table` type) |
| **Image_summary** | Summary of images (only for `image` type) |

**Tools Used:**  
- AstraDB  
- Azure OpenAI Embeddings  

---

### 3. Response Generation

The query handling process works as follows:

- The **input query** is split into **sub-queries** if it spans multiple topics.
- Each sub-query is compared against pre-generated **topic summaries** using **Hugging Face similarity models**, selecting the most relevant topics.
- These filtered topics are used to query **AstraDB**, retrieving the most relevant documents for each sub-query.
- The retrieved documents, along with the original query, are passed to **Azure OpenAI LLM** to generate the final response.

**Tools Used:**  
- Streamlit  
- Azure OpenAI  
- Langchain  
- Hugging Face  
- Nvidia AI  

---

### 📌 Example Input & Output

#### Example Input
> What are the data protection features and security features offered by NetApp Storage Grid?

#### Example Output
> NetApp Storage Grid offers comprehensive data protection mechanisms including erasure coding, replication across geo-locations, and robust access control policies. Security features include role-based access control (RBAC), audit logging, encryption at rest and in transit, and integration with external identity providers such as LDAP or Active Directory.

---

## ⚙️ Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Locally

```bash
python Code/main.py
```

---

## 🐳 Docker Instructions

### 1. Build Docker Image

```bash
docker build -t rpf_response .
```

### 2. Run Docker Container

```bash
docker run -p 8502:8502 rpf_response
```

After running, access the app at:  
👉 [http://localhost:8502](http://localhost:8502)

---

## 📂 Folder Structure Explained

| File/Folder | Purpose |
|---|---|
| **Code/** | Contains main application code |
| **main.py** | Main entry point for the Streamlit app |
| **utils.py** | Helper functions for document retrieval, vector search, etc. |
| **requirements.txt** | Required Python dependencies |
| **Dockerfile** | Instructions for building the Docker image |
| **README.md** | Project documentation |

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Streamlit** (UI framework for the app)
- **AstraDB** (Vector Database for document retrieval)
- **Azure OpenAI** (LLM for response generation)
- **Langchain** (LLM orchestration and chaining)
- **Hugging Face Models** (Similarity models for topic matching)
- **Nvidia AI** (Summarization models for image and table data)
- **Pymupdf** & **pdfplumber** (PDF processing tools)

---

## 👥 Contributors

- [Your Name or Team Name]  
- [Your GitHub Profile or Contact Info]

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

For questions, suggestions, or contributions, please raise an issue in this repository.

---











