from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Context Engine"
    ENV: str = "dev"

    class Config:
        env_file = ".env"

settings = Settings()
