from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.chatbot import getChatResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str
    chatName: str

@app.post("/chat")
def chat_endpoint(data: ChatRequest):
    try:
        response = getChatResponse(data.prompt, data.chatName)
        return {"response": response}
    except Exception as e:
        print(f"[ERROR] {e}")
        return {"error": str(e)}
