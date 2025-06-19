from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

prompt1 = PromptTemplate(
    template='Genrate short and simple notes for the following text: \n{text}',
    input_variables=["text"]        
)
prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the folloeing text \n {text}',
    input_variables=["text"]        
)
prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes}  \n  quiz -> {quiz}',
    input_variables=["notes", "quiz"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes' : prompt1 | model | parser,
    'quiz' : prompt2 | model | parser ,
})

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain


text = """The Indian economy is the world's sixth-largest by nominal GDP and the third-largest by
             purchasing power parity (PPP). It is classified as a newly industrialised country, and
             is one of the G20 major economies. India is a member of the BRICS group of emerging economies, 
             and is also a member of the World Trade Organization (WTO), the G20, and the International Monetary Fund (IMF).
             The country has a mixed economy, which includes traditional 
            village farming, modern agriculture, handicrafts, a wide range of industries, and numerous services."""
chain.get_graph().print_ascii()

result = chain.invoke({'text': text})
print(result)




