from typing import List, Dict, TypedDict, Optional
from config.config import get_config
from utils.types import list_str_to_int, list_int_to_str
from utils.files import read_from_file, save_to_file, remove_from_file


RECORD_KEYS = {
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


def create(
        author_id: Optional[int] = None,
        first_name: str = "",
        middle_name: str = "",
        last_name: str = "",
        science_degree: str = "",
        science_title: str = "",
        notes: List[int] = []
    ) -> bool:
    new_author = Author(
        id=author_id,
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        science_degree=science_degree,
        science_title=science_title,
        notes=notes,
    )
    return save_author_to_file(author=new_author)


def read(author_id: int) -> Optional[Author]:
    return read_author_from_file(author_id=author_id)


def update(author_id: int, values_dict: Dict[str, type]) -> bool:
    updating_author = read_author_from_file(author_id=author_id)
    if updating_author == None:
        return False
    for key in values_dict.keys():
        if key in RECORD_KEYS.keys() and type(values_dict[key]) is RECORD_KEYS[key]:
            updating_author[key] = values_dict[key]
    return save_author_to_file(author=updating_author)  


def delete(author_id: int) -> bool:
    return remove_author_from_file(author_id=author_id)


def read_author_from_file(author_id: int) -> Optional[Author]:
    author_fields = read_from_file(id=author_id, file_path=get_config()["AUTHOR_FILE"])
    if author_fields != None:
        return Author(
            id=int(author_fields[0]),
            first_name=author_fields[1],
            middle_name=author_fields[2],
            last_name=author_fields[3],
            science_degree=author_fields[4],
            science_title=author_fields[5],
            notes=list_str_to_int(author_fields[6].split("-"))
        )
    return None


def save_author_to_file(author: Author) -> bool:
    author_fields = []
    author_fields.append(author['id'])
    author_fields.append(author['first_name'])
    author_fields.append(author['middle_name'])
    author_fields.append(author['last_name'])
    author_fields.append(author['science_degree'])
    author_fields.append(author['science_title'])
    author_fields.append('-'.join(list_int_to_str(author['notes'])))
    save_to_file(entity_fields=author_fields, file_path=get_config()["AUTHOR_FILE"])


def remove_author_from_file(author_id: int) -> bool:
    return remove_from_file(id=author_id, file_path=get_config()["AUTHOR_FILE"])
