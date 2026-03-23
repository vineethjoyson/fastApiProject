
from jose import jwt
from datetime import datetime, timedelta
from app.core.config import settings

def create_access_token(data):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=30)
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def create_refresh_token(data):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(days=7)
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
