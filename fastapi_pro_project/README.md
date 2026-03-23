
# Production FastAPI Project

## Features
- JWT Auth (Access + Refresh)
- Role-based payload
- External API aggregation
- Logging + Middleware
- Docker ready

## Run
pip install -r requirements.txt
uvicorn app.main:app --reload

## Docker
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app

## Future
- Deploy to ECS/EKS
- Add CI/CD pipeline
