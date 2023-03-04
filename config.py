from pydantic import BaseSettings


class Settings(BaseSettings):
    openai_organization: str
    openai_api_key: str

    class Config:
        env_file = ".env"
