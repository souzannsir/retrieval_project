from config import *
import faiss
import json 

def search(index_file_path, json_file_path, emb_query, top_k, k=1000):
    index = faiss.read_index(index_file_path)
    distances, indices = index.search(emb_query.reshape(1, -1), k)

    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        loaded_sentence_index_mapping = json.load(json_file)
        mmap = indices[0]
        unique_indices = set()
        result_list = []
        
        for chunk_id in mmap:
            for entry in loaded_sentence_index_mapping:
                for chunk in entry["chunks"]:
                    if chunk["id"] == chunk_id and entry["index"] not in unique_indices:
                        result_list.append(entry["index"])
                        unique_indices.add(entry["index"])
        
        top_index = result_list[:top_k]
        
        # ✅ إرجاع قائمة تحتوي فقط على نصوص الوثائق
        selected_texts = [
            item["text"]
            for index in top_index
            for item in loaded_sentence_index_mapping
            if item["index"] == index
        ]
    
    return selected_texts  # ✅ إرجاع قائمة نصوص فقط

