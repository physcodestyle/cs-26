from typing import List, TypedDict


RECORD_KEYS = {
    "title": str,
    "country": str,
    "city": str,
    "notes": list
}


class Publisher(TypedDict):
    id: int
    title: str
    country: str
    city: str
    notes: List[int]
