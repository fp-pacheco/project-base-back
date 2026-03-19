import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_ENV: str = os.getenv("APP_ENV", "dev")
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: str = os.getenv("API_PORT", "8000")
    API_VERSION: str = os.getenv("API_VERSION", "1.0.0")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "")
