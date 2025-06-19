from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(model_name="claude-sonnet-4", temperature=0, max_tokens=1000)

result = model.invoke("what is the capital of india?, and who is the prime minister of india?")
print(result.content)
