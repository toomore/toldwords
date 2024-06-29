''' OpenAI API Connect '''
from enum import Enum
from typing import List

from pydantic import BaseModel, ConfigDict
from requests import Session


class Role(str, Enum):
    ''' Role '''
    ASSISTANT = 'assistant'
    SYSTEM = 'system'
    USER = 'user'


class Message(BaseModel):
    ''' Message in chat format '''
    model_config = ConfigDict(use_enum_values=True)
    role: Role
    content: str


class TokenUsage(BaseModel):
    ''' Token usage '''
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int


class Choice(BaseModel):
    ''' choice '''
    finish_reason: str
    index: int
    message: Message


class RespCompletions(BaseModel):
    ''' Response of chat.completions'''
    id: str
    model: str
    object: str
    created: int
    usage: TokenUsage
    choices: list[Choice]


class OpenAIAPI(Session):
    ''' OpenAI API '''

    def __init__(self, token: str, organization: str | None) -> None:
        super().__init__()
        self.url = 'https://api.openai.com/v1'
        self.headers['Authorization'] = f'Bearer {token}'

        if organization:
            self.headers['OpenAI-Organization'] = organization

    def chat_completions(self,  # pylint: disable=too-many-arguments
                         messages: List[Message],
                         model: str = 'gpt-4o',
                         temperature: int = 1,
                         n: int = 1,  # pylint: disable=invalid-name
                         user: str = 'api') -> RespCompletions:
        ''' chat completions '''
        data = {
            'model': model,
            'messages': [msg.model_dump() for msg in messages],
            'temperature': temperature,
            'n': n,
            'user': user,
        }
        return RespCompletions.model_validate(
            self.post(self.url + '/chat/completions', json=data).json()
        )
