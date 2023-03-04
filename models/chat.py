from pydantic import BaseModel


class Request(BaseModel):
    model: str
    messages: list[dict[str, str]]

    def __str__(self) -> str:
        return "ChatRequest"
