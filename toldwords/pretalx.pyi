from _typeshed import Incomplete
from pydantic import BaseModel
from requests import Session
from typing import List

class Item(BaseModel):
    code: str
    title: str
    track_id: int
    state: str
    abstract: str

class PretalxResponse(BaseModel):
    count: int
    next: str | None
    previous: str | None
    results: List[Item]

class Pretalx(Session):
    url: Incomplete
    def __init__(self, domain: str, project: str, resource: str) -> None: ...
    def fetch(self) -> PretalxResponse: ...
