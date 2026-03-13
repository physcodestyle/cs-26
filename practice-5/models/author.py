from typing import List, TypedDict


class Author(TypedDict):
    id: int
    first_name: str
    middle_name: str
    last_name: str
    science_degree: str
    science_title: str
    notes: List[str]
