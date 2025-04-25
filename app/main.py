# fastapi
from fastapi import FastAPI

# app
from config.config import settings
from src.routes import router

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_VERSION}/openapi.json"
)

app.include_router(router)