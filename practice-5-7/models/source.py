from typing import List, TypedDict


class Source(TypedDict):
    id: int
    title: str
    authors: List[int]
    publisher: int
    volume: int
    year: int
    issue: int
    pages: List[int]
