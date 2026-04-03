from typing import List, TypedDict


RECORD_KEYS = {
    "title": str,
    "authors": list,
    "publisher": int,
    "volume": int,
    "year": int,
    "issue": int,
    "pages": list,
    "notes": list,
}


class Source(TypedDict):
    id: int
    title: str
    authors: List[int]
    publisher: int
    volume: int
    year: int
    issue: int
    pages: List[int]
    notes: List[int]
