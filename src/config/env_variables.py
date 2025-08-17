import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:

    # Application Configuration
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI Application")
    APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
    APP_DESCRIPTION: str = os.getenv("APP_DESCRIPTION", "A FastAPI application")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    # Server Configuration
    HOST: str = os.getenv("HOST", "0.0.0.0")
    INTERNAL_PORT: int = int(os.getenv("INTERNAL_PORT", "8000"))

    # Postgres db configuration
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")

    def __init__(self):
        pass


# Create a global settings instance
settings = Settings()