from functools import lru_cache

from fastapi import Depends, FastAPI
import openai

import config
from models import ChatRequest

app = FastAPI()


@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/")
async def root():
    return {
        "massage": "Hello!"
    }


@app.post("/chat")
async def chat(req: ChatRequest, settings: config.Settings = Depends(get_settings)):
    openai.organization = settings.openai_organization
    openai.api_key = settings.openai_api_key
    return openai.ChatCompletion.create(
        model=req.model,
        messages=req.messages
    )
