from typing import List, Dict, TypedDict, Optional
from config.config import get_config
from utils.types import list_str_to_int, list_int_to_str
from utils.files import read_from_file, save_to_file, remove_from_file


RECORD_KEYS = {
    "title": str,
    "note": str,
    "quotation": str,
    "source_id": int,
    "pages": list,
    "paragraphs": list,
    "words": list,
}


class Record(TypedDict):
    id: Optional[int]
    title: str
    note: str
    quotation: str
    source_id: int
    pages: List[int]
    paragraphs: List[int]
    words: List[int]


def create(
        record_id: Optional[int] = None,
        title: str = "",
        note: str = "",
        quotation: str = "",
        source_id: int = 0,
        pages: List[int] = {},
        paragraphs: List[int] = {},
        words: List[int] = {}
    ) -> bool:
    new_record = Record(
        id=record_id,
        title=title,
        note=note,
        quotation=quotation,
        source_id=source_id,
        pages=pages,
        paragraphs=paragraphs,
        words=words
    )
    return save_record_to_file(record=new_record)


def read(record_id: int) -> Optional[Record]:
    return read_record_from_file(record_id=record_id)


def update(record_id: int, values_dict: Dict[str, type]) -> bool:
    updating_record = read_record_from_file(record_id=record_id)
    if updating_record == None:
        return False
    for key in values_dict.keys():
        if key in RECORD_KEYS.keys() and type(values_dict[key]) is RECORD_KEYS[key]:
            updating_record[key] = values_dict[key]
    return save_record_to_file(record=updating_record)


def delete(record_id: int) -> bool:
    return remove_record_from_file(record_id=record_id)


def read_record_from_file(record_id: int) -> Optional[Record]:
    record_fields = read_from_file(id=record_id, file_path=get_config()["RECORD_FILE"])
    if record_fields != None:
        return Record(
            id=int(record_fields[0]),
            title=record_fields[1],
            note=record_fields[2],
            quotation=record_fields[3],
            source_id=int(record_fields[4]),
            pages=list_str_to_int(record_fields[5].split("-")),
            paragraphs=list_str_to_int(record_fields[6].split("-")),
            words=list_str_to_int(record_fields[7].split("-"))
        )
    return None


def save_record_to_file(record: Record) -> bool:
    record_fields = []
    record_fields.append(record['id'])
    record_fields.append(record['title'])
    record_fields.append(record['note'])
    record_fields.append(record['quotation'])
    record_fields.append(str(record['source_id']))
    record_fields.append('-'.join(list_int_to_str(record['pages'])))
    record_fields.append('-'.join(list_int_to_str(record['paragraphs'])))
    record_fields.append('-'.join(list_int_to_str(record['words'])))
    save_to_file(entity_fields=record_fields, file_path=get_config()["RECORD_FILE"])


def remove_record_from_file(record_id: int) -> bool:
    return remove_from_file(id=record_id, file_path=get_config()["RECORD_FILE"])
