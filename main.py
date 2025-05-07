from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# App உருவாக்குதல்
app = FastAPI()

# CORS policy (Frontend-க்கு அனுமதி)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Model உருவாக்குதல்
class PromptRequest(BaseModel):
    category: str
    user_input: str

# முதன்மை Route
@app.get("/")
async def root():
    return {"message": "Grafix backend is live!"}

# Prompt Generate Route
@app.post("/generate-prompt")
async def generate_prompt(req: PromptRequest):
    # இந்த இடத்தில் Prompt generate logic எழுதவும்.
    generated_prompt = f"{req.category}-க்கான Prompt: {req.user_input}"
    return {"prompt": generated_prompt}
