from typing import Optional

from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    
    PROJECT_NAME: str = 'API DEPLOY'
    
    # database configurations
    DATABASE_URL: Optional[str] = None

    # JWT
    secret_key: str = "secret"
    algorithm: str = "HS256"
    
    # General
    API_VERSION: str = "/api/v1"

    class Config:
        env_file = ".env"
        from_attributes = True

settings = Settings()
