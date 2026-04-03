from typing import List, Dict, TypedDict, Optional
from config.config import get_config
from utils.types import list_str_to_int, list_int_to_str
from utils.files import read_from_file, save_to_file, remove_from_file


RECORD_KEYS = {
    "title": str,
    "country": str,
    "city": str,
    "notes": list
}


class Publisher(TypedDict):
    id: Optional[int]
    title: str
    country: str
    city: str
    notes: List[int]


def create(
        publisher_id: Optional[int] = None,
        title: str = "",
        country: str = "",
        city: str = "",
        notes: List[int] = [],
    ) -> bool:
    new_publisher = Publisher(
        id=publisher_id,
        title=title,
        country=country,
        city=city,
        notes=notes
    )
    return save_publisher_to_file(publisher=new_publisher)


def read(publisher_id: int) -> Optional[Publisher]:
    return read_publisher_from_file(publisher_id=publisher_id)


def update(publisher_id: int, values_dict: Dict[str, type]) -> bool:
    updating_publisher = read_publisher_from_file(publisher_id=publisher_id)
    if updating_publisher == None:
        return False
    for key in values_dict.keys():
        if key in RECORD_KEYS.keys() and type(values_dict[key]) is RECORD_KEYS[key]:
            updating_publisher[key] = values_dict[key]
    return save_publisher_to_file(publisher=updating_publisher)  


def delete(publisher_id: int) -> bool:
    return remove_publisher_from_file(publisher_id=publisher_id)


def read_publisher_from_file(publisher_id: int) -> Optional[Publisher]:
    publisher_fields = read_from_file(id=publisher_id, file_path=get_config()["PUBLISHER_FILE"])
    if publisher_fields != None:
        return Publisher(
            id=int(publisher_fields[0]),
            title=publisher_fields[1],
            country=publisher_fields[2],
            city=publisher_fields[3],
            notes=list_str_to_int(publisher_fields[4].split("-"))
        )
    return None


def save_publisher_to_file(publisher: Publisher) -> bool:
    publisher_fields = []
    publisher_fields.append(publisher['id'])
    publisher_fields.append(publisher['title'])
    publisher_fields.append(publisher['country'])
    publisher_fields.append(publisher['city'])
    publisher_fields.append('-'.join(list_int_to_str(publisher['notes'])))
    save_to_file(entity_fields=publisher_fields, file_path=get_config()["PUBLISHER_FILE"])


def remove_publisher_from_file(publisher_id: int) -> bool:
    return remove_from_file(id=publisher_id, file_path=get_config()["PUBLISHER_FILE"])

