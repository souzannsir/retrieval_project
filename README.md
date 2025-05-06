Step 1. create conda environmrnt with python version 3.9 using this command
`conda create -n retriver python==3.9 -y`

Step 2. activate retriver environment
`conda activate retriver `

Step 3.  download the multilingual-e5-large model from Hugging Face and put it in the models folder

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