from typing import TypedDict


RECORD_KEYS = {
    "text": str,
}


class Note(TypedDict):
    id: int
    text: str
