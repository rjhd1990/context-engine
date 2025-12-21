from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Context Engine"
    ENV: str = "dev"
    OPENAI_API_KEY: str = ""
    EMBEDDING_MODEL: str = ""
    CHAT_MODEL: str = ""
    PDF_DIR :str = "data/pdfs"
    INDEX_DIR: str = "data/index"
    class Config:
        env_file = ".env"

settings = Settings()
