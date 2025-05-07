# ⚖️ Legal Text Retrieval Project Using Automated Segmentation and Multidimensional Embedding

This project implements an advanced legal information retrieval system that enhances search accuracy through Dynamic Text Segmentation and Multidimensional Embeddings, leveraging the multilingual-e5-large model. The system achieves a precision rate of 0.74 across 909 legal articles using FAISS (Facebook AI Similarity Search) for efficient vector similarity search.

## Project Overview

The system improves legal text retrieval by:
1. Segmenting legal documents into meaningful semantic chunks
2. Creating multidimensional text representations using state-of-the-art embedding techniques
3. Building an efficient retrieval database with FAISS indexing
4. Providing a REST API interface for query processing

## Prerequisites

• Python 3.9 
• Conda (for environment management management) 
• Postman (for API testing)

## Installation

**Step 1: Create and Activate Conda Environment**

```bash
# Create a new conda environment with python 3.9
conda create -n retriever python==3.9 -y

# Activate the Environment
conda activate retriever
```

**Step 2: Download Required Model**

```bash
# Download the multilingual-e5-large model from Hugging Face
https://huggingface.co/models/multilingual-e5-large/
```

**Step 3: Install Dependencies**

```bash
# Install all required packages
pip install -r requirements.txt
```

**Indexing the Data**

```bash
# To build the initial search index
python indexing.py
```

## Running the Application

**Start the Retrieval Service**

```bash
# Start the retrieval service
python app.py
```

## API Documentation

The system exposes a REST API that can be accessed for text retrieval queries.

**Example API Call**

Using cURL:

```bash
curl --location 'http://localhost:5050/api/v01/retrive' \
--header 'Content-Type: application/json' \
--data '{
    "texts": "ماحكم الاستقالة ولمن تعطى؟"
}'
```

You can also test the API using Postman with the above endpoint and payload.

## License

Open source project - for academic and educational use only.

## Performance

The current implementation achieves a precision of 0.74 on a datatset consisting of 909 legal articles, demonstrating the effectiveness of combining dynamic text segmentation with multidimensional embeddings for legal information retrieval.
