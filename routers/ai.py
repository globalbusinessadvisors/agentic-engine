from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import openai

router = APIRouter()

class AIRequest(BaseModel):
    prompt: str

class AIResponse(BaseModel):
    response: str

@router.post("/generate", response_model=AIResponse)
def generate_response(ai_request: AIRequest):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=ai_request.prompt,
            max_tokens=150
        )
        return AIResponse(response=response.choices[0].text.strip())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
