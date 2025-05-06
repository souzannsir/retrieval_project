from sentence_transformers import SentenceTransformer
import faiss
import json
import numpy as np
import re
import logging
from config import *
import pandas as pd
embeddingmodel = EMBEDDINGMODEL
datapath = DATAPATH
short_faiss_index = SHORT_FAISSINDEX
short_dic = SHORT_DIC
long_faiss_index = LONG_FAISSINDEX
long_dic = LONG_DIC
mid_faiss_index = MID_FAISSINDEX
mid_dic = MID_DIC
logger = logging.getLogger(__name__)
#Embedding Models
model = SentenceTransformer(embeddingmodel)

#read data file 
data = pd.read_excel(datapath)
# data = data.head(4)
sentences = []
for index, row in data.iterrows():
    article_id = row["article_id"]
    context = row["text"]
    title = row["title"]
    # law_name = row["law_name"]
    sentences.append({"article_id": article_id, "title": title, "context": context})

def chunk_text(text, chunk_size, overlap):
    words = re.findall(r'\b\w+\b', text)
    chunks = []
    i = 0
    while i < len(words):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks

def create_index(sentences, model, index_file_path, json_file_path,chunk_size,overlap):
    chunked_sentences = [chunk_text(sentence["context"], chunk_size, overlap) for sentence in sentences]
    chunked_embeddings = [model.encode(chunk) for sentence_chunks in chunked_sentences for chunk in sentence_chunks]

    index = faiss.IndexFlatL2(chunked_embeddings[0].shape[0])
    index.add(np.vstack(chunked_embeddings))
    faiss.write_index(index, index_file_path)
    rrrr = []
    sentence_index_mapping = {}
    total_chunk_count = 0

    for i, sentence in enumerate(sentences):
        sentence_index_mapping[sentence["context"]] = {
            "article_id": sentence["article_id"],
            "title": sentence["title"],
            "text": sentence["context"],
            # "law_name": sentence['law_name'],
            "chunks": [],
            "index": i
        }

        for j, chunk in enumerate(chunked_sentences[i]):
            sentence_index_mapping[sentence["context"]]["chunks"].append({
                "id": total_chunk_count,
                "text": chunk
            })
            total_chunk_count += 1

        rrrr.append(sentence_index_mapping[sentence["context"]])

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(rrrr, json_file, ensure_ascii=False)


def indexing(short= False , mid= False, long= False):
    if short:
        index_file_path = short_faiss_index
        json_file_path = short_dic
        chunk_size=5
        overlap=2
        print ("1111")
        create_index(sentences, model, index_file_path, json_file_path, chunk_size, overlap)
    if mid:
        index_file_path = mid_faiss_index
        json_file_path = mid_dic
        chunk_size=10
        overlap=3
        print ("2222")
        create_index(sentences, model, index_file_path, json_file_path, chunk_size, overlap)
    if long:
        index_file_path = long_faiss_index
        json_file_path = long_dic
        chunk_size=20
        overlap=5
        print ("3333")
        create_index(sentences, model, index_file_path, json_file_path, chunk_size, overlap)
indexing(short=True, mid=True, long=True)