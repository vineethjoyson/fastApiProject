
from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "supersecret"
    ALGORITHM: str = "HS256"
    REDIS_URL: str = "redis://localhost:6379"

settings = Settings()
