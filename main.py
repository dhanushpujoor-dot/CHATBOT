from langchain_core.messages import HumanMessage, AIMessage 
from rag_chain import get_chain 
chat_history = [] 
chain = get_chain(chat_history) 
print("🤖 Chatbot is ready! Type 'exit' to quit.\n")
while True: 
    user = input("YOU: ") 
    if user.lower() == "exit": 
        break 
    chat_history.append(HumanMessage(content=user)) 
    output = chain.invoke(user) 
    print("AI:", output) 
    chat_history.append(AIMessage(content=output))