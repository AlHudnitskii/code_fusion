from pydantic import BaseSettings
import os
from dotenv import load_dotenv


class Settings(BaseSettings):
    mongo_url: str = "mongodb://localhost:27017"
    mongo_db_name: str = "code_fusion"

    class Config:
        env_file = ".env"

load_dotenv()
SECRET_KEY = os.getenv("JWT_SECRET")

if not SECRET_KEY:
    raise ValueError("❌ Ошибка: В .env отсутствует JWT_SECRET!")

settings = Settings()