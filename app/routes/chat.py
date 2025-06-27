from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.utils.model_call import query_model

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/chat_assistant")
async def chat_assistant(data: ChatRequest):
    prompt = f"""You are a smart city assistant. Provide helpful, simple, and clear answers for citizens.
User: "{data.query}"
Assistant:"""
    
    response = query_model(prompt, model_key="chat")
    return {"response": response}

