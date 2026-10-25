from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage,HumanMessage

messages=[
     ]

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are a {domain} Engineer, Explain me under 30 words , with one reallife example",),
        ("user", "{query}")
       
    ]
)



model_name = "llama3.2:latest"
llm = ChatOllama(model=model_name, temperature=0.5)


parser = StrOutputParser()

chain=prompt_template | llm | parser

while True:
    user_query=input("You: ")
    if "bye"in user_query.lower():
        print("Assistant: goodbye!!")
        break
   
    response=chain.invoke({
    "domain":"Computer science",
    "query":user_query})
    print("Assistant: ",response)
    prompt_template.append(response)
    
    