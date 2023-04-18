from enum import Enum
from pydantic import BaseModel
from requests import Session
from typing import List

class Role(str, Enum):
    ASSISTANT: str
    SYSTEM: str
    USER: str

class Message(BaseModel):
    role: Role
    content: str
    class Config:
        use_enum_values: bool

class TokenUsage(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int

class Choice(BaseModel):
    finish_reason: str
    index: int
    message: Message

class RespCompletions(BaseModel):
    id: str
    model: str
    object: str
    created: int
    usage: TokenUsage
    choices: list[Choice]

class OpenAIAPI(Session):
    url: str
    def __init__(self, token: str, organization: str | None) -> None: ...
    def chat_completions(self, messages: List[Message], model: str = ..., temperature: int = ..., n: int = ..., user: str = ...) -> RespCompletions: ...
