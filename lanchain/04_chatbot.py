from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

model_name = "llama3.2:latest"
messages = [SystemMessage("You are a Strict professor!!, reply in one line")]
llm = ChatOllama(model=model_name, temperature=0.5)

while True:
    user_promt = input("You: ")
    if "bye" in user_promt.lower():
        print("Assiatant: goodbye Student")
        break
    human_msg = HumanMessage(user_promt)
    messages.append(human_msg)

    response = llm.invoke(messages)
    print("Assitant:", response.content)
    messages.append(response)
