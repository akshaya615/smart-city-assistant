from fastapi import APIRouter, Request
from pydantic import BaseModel
from app.utils.model_call import query_model

router = APIRouter()

class FeedbackRequest(BaseModel):
    feedback: str

@router.post("/citizen_feedback")
async def citizen_feedback(data: FeedbackRequest):
    prompt = f"""You are a helpful assistant collecting citizen feedback for the smart city team.
User feedback: "{data.feedback}"
Respond politely and acknowledge their input. Thank them and assure it's noted."""
    
    response = query_model(prompt, model_key="feedback")
    return {"response": response}
