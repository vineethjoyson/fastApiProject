
from fastapi import FastAPI
from app.api.routes import auth_routes, user_routes
from app.core.logger import logger
from app.middleware.error_handler import add_exception_handlers

app = FastAPI(title="Production FastAPI")

# Register middleware
add_exception_handlers(app)

# Include routers
app.include_router(auth_routes.router)
app.include_router(user_routes.router)

logger.info("Application started")
