import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "GraFix AI Studio Backend"
    api_prefix: str = "/api"
    version: str = "1.0.0"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
