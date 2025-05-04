from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import router as prompt_router  # ✅ Import your router

app = FastAPI()

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later to just frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include API routes
app.include_router(prompt_router)
