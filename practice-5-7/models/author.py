from typing import List, Dict, TypedDict, Optional

author_KEYS = {
    "first_name": str,
    "middle_name": str,
    "last_name": str,
    "science_degree": str,
    "science_title": str,
    "notes": list,
}


class Author(TypedDict):
    id: int
    first_name: str
    middle_name: str
    last_name: str
    science_degree: str
    science_title: str
    notes: List[int]
