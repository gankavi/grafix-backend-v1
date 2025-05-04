from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.prompt_generator import generate_prompt

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

class PromptRequest(BaseModel):
    category: str
    user_input: str

@router.post("/generate-prompt")
def generate_prompt_api(request: PromptRequest):
    try:
        prompt = generate_prompt(request.category, request.user_input)
        return {"prompt": prompt}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
