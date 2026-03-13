from enum import Enum
from typing import List, TypedDict


class SourceType(Enum):
    ARTICLE = 1
    BOOK = 2
    WEB = 3


class Source(TypedDict):
    id: int
    title: str
    summary: str
    publisher_id: int
    incoming_date: int      # POSIX FORMAT (seconds from 00:00:00, Jan 1, 1970)
    release_date: int       # POSIX FORMAT (seconds from 00:00:00, Jan 1, 1970)
    issue: int
    volume: int
    author_id: List[int]
    notes: List[str]
