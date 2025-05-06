from sentence_transformers import SentenceTransformer
import searcher
from config import *
from flask import Flask, request,jsonify
from flask_cors import CORS
import requests
import json
from threading import Timer
from sklearn.metrics.pairwise import cosine_similarity
embeddingmodel = EMBEDDINGMODEL
datapath = DATAPATH
short_faiss_index = SHORT_FAISSINDEX
short_dic = SHORT_DIC
long_faiss_index = LONG_FAISSINDEX
long_dic = LONG_DIC
mid_faiss_index = MID_FAISSINDEX
mid_dic = MID_DIC
host_id = HOST
port_id = PORT
model = SentenceTransformer(embeddingmodel)
app = Flask(__name__, template_folder='templates')
CORS(app)


@app.route('/api/v01/retrive', methods=['POST'])
def search():
    data = request.get_json(force=True)
    query = data['texts']
    if query:
        eemb_query = model.encode(query)
        try:
            words = query.split(" ")
            if len(words) <= 5:
                faiss_file = short_faiss_index
                mmap_file = short_dic
            elif len(words) >5 and len(words) <= 10:
                faiss_file = mid_faiss_index
                mmap_file = mid_dic
            else:
                faiss_file = long_faiss_index
                mmap_file = long_dic
            return searcher.search(faiss_file, mmap_file, emb_query=eemb_query, top_k=10)
        except:
            return "error"
    else:
        return "query os empty"

if __name__ == '__main__':
    print(f"server listining on http://{host_id}:{port_id}")
    app.run(host=host_id,port=port_id, debug=True)