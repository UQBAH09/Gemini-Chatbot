import re
import json
import os
import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

chats = {}

def getResponse(prompt,chat):
    try:
        response = chat.send_message(prompt)
        return strip_markdown(response.text)
    except Exception as e:
        return f"Error: {str(e)}"

def strip_markdown(text):
    return re.sub(r'(\*\*|\*)', '', text)

def saveChat(chat, filePath):
    chatData = []
    for msg in chat.history:
        part = msg.parts[0].text if hasattr(msg.parts[0], "text") else str(msg.parts[0])
        chatData.append({
            "role": msg.role,
            "parts": [part]
        })

    with open(filePath, 'w') as file:
        json.dump(chatData, file, indent=2)

def loadChatHistory(filePath):
    try:
        with open(filePath, 'r') as file:
            rawData = json.load(file)
            history = []
            for msg in rawData:
                history.append({
                    "role": msg["role"],
                    "parts": msg["parts"]
                })
            return model.start_chat(history=history)
    
    except(FileNotFoundError):
        createNewChat(filePath)
        loadChatHistory(filePath)

    except (json.JSONDecodeError) as e:
        print(f"[!] Failed to load chat: {e}")
        return model.start_chat(history=[])

def createNewChat(filePath):
    if not os.path.exists("Chatbots"):
        os.makedirs("Chatbots")

    with open(filePath, 'w') as file:
        json.dump([], file)

    return loadChatHistory(filePath), filePath

def readChat(chat):
    print("\n[✓] Chat history loaded:\n")
    for msg in chat.history:
        content = msg.parts[0].text if hasattr(msg.parts[0], "text") else str(msg.parts[0])
        print(f"{msg.role}: {content}")

def getFilePath(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # directory where chatbot.py is
    chatbots_dir = os.path.join(base_dir, "Chatbots")
    return os.path.join(chatbots_dir, filename + ".json")


def getChatResponse(prompt, chatName):
    if chatName not in chats:
        chats[chatName] = loadChatHistory(getFilePath(chatName))
    
    chat = chats[chatName]
    response = getResponse(prompt,chat)
    saveChat(chat, getFilePath(chatName))
    return response


def main():
    choice = input("Start new chat or load existing? (new/load): ").strip().lower()
    if choice == "new":
        chat, filePath = createNewChat()
    else:
        filename = input("Enter chat name to load: ").strip()
        filePath = os.path.join("Chatbots", filename + ".json")
        chat = loadChatHistory(filePath)
        readChat(chat)

    while True:
        prompt = input("You: ")
        if 'exit' in prompt.lower():
            break

        response = getResponse(prompt, chat)
        print("Bot:", strip_markdown(response.text))

    saveChat(chat, filePath)

if __name__ == "__main__":
    main()