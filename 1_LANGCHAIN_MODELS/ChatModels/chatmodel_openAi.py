from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, max_tokens=1000)

result = model.invoke("what is the capital of india?, and who is the prime minister of india?")
print(result.content)


