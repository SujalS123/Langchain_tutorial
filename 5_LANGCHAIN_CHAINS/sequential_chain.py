from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

prompt1 = PromptTemplate(
    template='Genrate a detailed report on {topic}.',
    input_variables=["topic"]   
)

prompt2 = PromptTemplate(
    template   = 'Generate a 5 pointer summary from the following text \n{text}',
    input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt1 | model |parser| prompt2| model | parser

chain.get_graph().print_ascii()
result = chain.invoke({'topic': 'employment in India'})
print(result)