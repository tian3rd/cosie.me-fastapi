from datetime import datetime

from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    date: datetime
    author: str
    tags: list[str]
    body: str
    version: int
    is_published: bool
