from fastapi import APIRouter
from pydantic import BaseModel
from ..utils.model_call import query_model

router = APIRouter()

class EcoInput(BaseModel):
    query: str

@router.post("/eco_advice")
def eco_advice(data: EcoInput):
    prompt = f"Give eco-friendly advice for this query: {data.query}"
    result = query_model(prompt, "eco")
    return {"response": result}