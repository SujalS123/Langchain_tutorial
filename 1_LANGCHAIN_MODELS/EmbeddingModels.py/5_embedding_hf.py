from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2")

text = "Delhi is the capital of India"
vector = embeddings.embed_query(text)
print(str(vector))  