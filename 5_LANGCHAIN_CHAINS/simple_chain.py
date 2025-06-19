from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



load_dotenv()

model = ChatGoogleGenerativeAI(model ="gemini-1.5-flash")

prompt = PromptTemplate(
    template='Generate 5 interesting facts  about {topic}.',
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt | model | parser 
# | -> pipe operator to chain the components together
# LCEF -> LangChain Expression Format, a way to express chains in a more readable format
chain.get_graph().print_ascii()
result = chain.invoke({'topic': 'cricket'})
print(result)
