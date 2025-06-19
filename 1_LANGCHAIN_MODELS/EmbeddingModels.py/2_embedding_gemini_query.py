from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",  # Specify the model you want to use
    dimensions= 32, 
)
result = embeddings.embed_query("Delhi is the capital of India ")

print(str(result))