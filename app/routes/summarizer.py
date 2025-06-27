from fastapi import APIRouter
from pydantic import BaseModel
from ..utils.model_call import query_model

router = APIRouter()

class SummaryInput(BaseModel):
    text: str

@router.post("/summarize")
def summarize_text(data: SummaryInput):
    prompt = data.text
    result = query_model(prompt, "summary")
    return {"response": result}

