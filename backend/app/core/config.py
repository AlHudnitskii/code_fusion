from pydantic import BaseSettings

class Settings(BaseSettings):
    mongo_url: str = "mongodb://localhost:27017"
    mongo_db_name: str = "code_fusion"

    class Config:
        env_file = ".env"

settings = Settings()