from fastapi import APIRouter
from pydantic import BaseModel
from ..utils.model_call import query_model

router = APIRouter()

class HealthInput(BaseModel):
    question: str

@router.post("/city_health")
async def city_health(data: HealthInput):
    prompt = f"{data.question}"
    result = query_model(prompt, "health")
    return {"response": result}
