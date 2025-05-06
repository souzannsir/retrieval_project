⚖️ Legal Text Retrieval Project Using Automated Segmentation and Multidimensional Embedding
This project aims to improve the accuracy and effectiveness of legal information retrieval by segmenting texts into meaningful chunks (Dynamic Text Segmentation) and using multidimensional text representations (Multidimensional Embeddings) using the multilingual-e5-large model.

The FAISS library was used to build an effective retrieval database based on 909 legal articles, and the system achieved a precision of 0.74.


Step 1. create conda environmrnt with python version 3.9 using this command
`conda create -n retriver python==3.9 -y`

Step 2. activate retriver environment
`conda activate retriver `

Step 3.  download the multilingual-e5-large model from Hugging Face 
`models/multilingual-e5-large/`

Step 4. install requirements
`pip install -r requirements.txt`

indexing data file
`python indexing.py`

run application 
`python app.py`

install postman in your pc

try this curl 

`curl --location 'http://localhost:5050/api/v01/retrive' \
--header 'Content-Type: application/json' \
--data '{
    "texts": "ماحكم الاستقالة ولمن تعطى؟"
}'`

Open source project — for academic and educational use only.