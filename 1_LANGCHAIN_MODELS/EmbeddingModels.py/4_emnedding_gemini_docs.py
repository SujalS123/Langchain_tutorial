from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",  # Specify the model you want to use
    dimensions=32, 
)
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]       
result = embeddings.embed_documents(documents)
print(str(result))