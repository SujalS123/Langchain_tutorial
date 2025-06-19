from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv  
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

class Person(BaseModel):
    name:str = Field(description='Name of the person')
    age:int = Field(gt=18,description='Age of the person, must be greater than 18')
    city:str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Genrate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables = {'format_instruction' : parser.get_format_instructions()}
)

prompt = template.invoke({'place': 'Indian'})
print(prompt)
result = model.invoke(prompt)
final_result = parser.parse(result.content)
print(final_result)


# OR
# Using a chain to combine the template, model, and parser
chain = template | model | parser   
final_result = chain.invoke({'place': 'Indian'})
print(final_result)