from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser , ResponseSchema

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')


schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables= { 'format_instruction': parser.get_format_instructions()}

)
#using the template to create a prompt
prompt = template.invoke({'topic': 'black hole'})
result = model.invoke(prompt)
final_result = parser.parse(result.content)
print(final_result)

# OR 

# Using a chain to combine the template, model, and parser
chain = template | model | parser
final_result = chain.invoke({'topic': 'black hole'})
print(final_result)


 