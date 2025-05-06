import os
from dotenv import load_dotenv
load_dotenv()

DATAPATH = os.getenv("DATAPATH")
EMBEDDINGMODEL = os.getenv("EMBEDDINGMODEL")
SHORT_FAISSINDEX = os.getenv("SHORT_FAISSINDEX")
SHORT_DIC = os.getenv("SHORT_DIC")
LONG_FAISSINDEX = os.getenv("LONG_FAISSINDEX")
LONG_DIC = os.getenv("LONG_DIC")
MID_FAISSINDEX = os.getenv("MID_FAISSINDEX")
MID_DIC = os.getenv("MID_DIC")
EMBEDDING_URL = os.getenv("EMBEDDING_URL")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")