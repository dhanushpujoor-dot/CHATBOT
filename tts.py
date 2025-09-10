from langchain_core.messages import HumanMessage, AIMessage
from rag_chain import get_chain
from langchain_core.output_parsers import StrOutputParser
import os  # macOS TTS

chat_history = []
chain = get_chain(chat_history)
parser = StrOutputParser()  # Ensure outputs are strings

print("🤖 Chatbot is ready! Type 'exit' to quit.\n")

while True:
    user = input("YOU: ")
    if user.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=user))
    
    # Get AI response
    raw_output = chain.invoke(user)
    
    # Parse output to string
    output_text = parser.parse(raw_output)

    # Print AI text
    print("AI:", output_text)

    # Speak AI text using macOS 'say' command
    os.system(f'say "{output_text}"')

    # Append AI response to history
    chat_history.append(AIMessage(content=output_text))



# from langchain_core.messages import HumanMessage, AIMessage
# from rag_chain import get_chain
# import pyttsx3

# # Initialize TTS engine ONCE
# engine = pyttsx3.init()
# engine.setProperty('rate', 150)   # Speech rate
# engine.setProperty('volume', 1.0) # Volume

# chat_history = []
# chain = get_chain(chat_history)

# print("🤖 Chatbot is ready! Type 'exit' to quit.\n")

# while True:
#     user = input("YOU: ")
#     if user.lower() == "exit":
#         break

#     chat_history.append(HumanMessage(content=user))
#     output = chain.invoke(user)

#     # Print AI text
#     print("AI:", output)

#     # Speak AI text (reuse the engine)
#     engine.say(output)
#     engine.runAndWait()  # don’t call engine.stop() here

#     chat_history.append(AIMessage(content=output))