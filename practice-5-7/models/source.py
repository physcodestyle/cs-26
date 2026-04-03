from typing import List, Dict, TypedDict, Optional
from config.config import get_config
from utils.types import list_str_to_int, list_int_to_str
from utils.files import read_from_file, save_to_file, remove_from_file


RECORD_KEYS = {
    "title": str,
    "publisher": int,
    "volume": int,
    "year": int,
    "issue": int,
    "pages": list,
    "notes": list,
    "link": str,
}


class Source(TypedDict):
    id: Optional[int]
    title: str
    publisher: int
    volume: int
    year: int
    issue: int
    pages: List[int]
    notes: List[int]
    link: str


def create(
        source_id: Optional[int] = None,
        title: str = "",
        publisher: int = 0,
        volume: int = 0,
        year: int = 0,
        issue: int = 0,
        pages: List[int] = [],
        notes: List[int] = [],
        link: str = "",
    ) -> bool:
    new_source = Source(
        id=source_id,
        title=title,
        publisher=publisher,
        volume=volume,
        year=year,
        issue=issue,
        pages=pages,
        notes=notes,
        link=link
    )
    return save_source_to_file(source=new_source)


def read(source_id: int) -> Optional[Source]:
    return read_source_from_file(source_id=source_id)


def update(source_id: int, values_dict: Dict[str, type]) -> bool:
    updating_source = read_source_from_file(source_id=source_id)
    if updating_source == None:
        return False
    for key in values_dict.keys():
        if key in RECORD_KEYS.keys() and type(values_dict[key]) is RECORD_KEYS[key]:
            updating_source[key] = values_dict[key]
    return save_source_to_file(source=updating_source)    


def delete(source_id: int) -> bool:
    return read_source_from_file(source_id=source_id)


def read_source_from_file(source_id: int) -> Optional[Source]:
    source_fields = read_from_file(id=source_id, file_path=get_config()["SOURCE_FILE"])
    if source_fields != None:
        return Source(
            id=int(source_fields[0]),
            title=source_fields[1],
            publisher=source_fields[3],
            volume=source_fields[4],
            year=source_fields[5],
            issue=source_fields[6],
            pages=list_str_to_int(source_fields[7].split("-")),
            notes=list_str_to_int(source_fields[8].split("-")),
            link=source_fields[9]
        )
    return None


def save_source_to_file(source: Source) -> bool:
    source_fields = []
    source_fields.append(source['id'])
    source_fields.append(source['title'])
    source_fields.append(source['publisher'])
    source_fields.append(source['volume'])
    source_fields.append(source['year'])
    source_fields.append(source['issue'])
    source_fields.append('-'.join(list_int_to_str(source['pages'])))
    source_fields.append('-'.join(list_int_to_str(source['notes'])))
    source_fields.append(source['link'])
    save_to_file(entity_fields=source_fields, file_path=get_config()["SOURCE_FILE"])


def remove_source_from_file(source_id: int) -> bool:
    return remove_from_file(id=source_id, file_path=get_config()["SOURCE_FILE"])

