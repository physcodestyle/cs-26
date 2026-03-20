from typing import Any, List, Dict, TypedDict, Optional
from config.config import get_config
from utils.types import list_str_to_int


RECORD_KEYS = {
    "title": str,
    "note": str,
    "source_id": int,
    "pages": list,
    "paragraphs": list,
    "words": list,
}


class Record(TypedDict):
    id: int
    title: str
    note: str
    source_id: int
    pages: List[int]
    paragraphs: List[int]
    words: List[int]


def create(
        record_id: int,
        title: str,
        note: str = "",
        source_id: str = "",
        pages: List[int] = {},
        paragraphs: List[int] = {},
        words: List[int] = {}
    ) -> bool:
    new_record = Record(
        id=record_id,
        title=title,
        note=note,
        source_id=source_id,
        pages=pages,
        paragraphs=paragraphs,
        words=words
    )
    return save_to_file(record=new_record, file_path=get_config()["RECORD_FILE"])


def read(record_id: int) -> Optional[Record]:
    return read_from_file(record_id=record_id, file_path=get_config()["RECORD_FILE"])


def update(record_id: int, values_dict: Dict[Any]) -> bool:
    updating_record = read_from_file(record_id=record_id, file_path=get_config()["RECORD_FILE"])
    if updating_record == None:
        return False
    for key in values_dict.keys():
        if key in RECORD_KEYS.keys() and type(values_dict[key]) is RECORD_KEYS[key]:
            updating_record[key] = values_dict[key]
    return save_to_file(record=updating_record, file_path=get_config()["RECORD_FILE"])


def delete(record_id: int) -> bool:
    return remove_from_file(record_id=record_id, file_path=get_config()["RECORD_FILE"])


def print(record: Record):
    print(record)


def remove_empty_strings_in_file(file_path: str) -> int:
    try:
        strings = []
        empty_string_indices = []
        with open(file=file_path, mode="r", encoding="utf-8") as f:
            strings = f.read().split("\n")
        for str_index in range(len(strings)):
            if strings[str_index] == "":
                empty_string_indices.append(str_index)
        f.close()
        if len(empty_string_indices) > 0:
            empty_string_indices.reverse()
            for str_index in empty_string_indices:
                strings.pop(str_index)
        with open(file=file_path, mode="w", encoding="utf-8") as f:
            f.write("\n".join(strings))
        f.close()   
    except IOError as err:
        print(f"Error: {err}")
        return False


def read_from_file(record_id: int, file_path: str) -> Optional[Record]:
    try:
        strings = []
        with open(file=file_path, mode="r", encoding="utf-8") as f:
            strings = f.read().split("\n")
        f.close()
        for str_index in range(len(strings)):
            fields = strings[str_index].split("\t")
            if fields[0] == str(record_id):
                return Record(
                    id=int(fields[0]),
                    title=fields[1],
                    note=fields[2],
                    source_id=int(fields[3]),
                    pages=list_str_to_int(fields[4].split("-")),
                    paragraphs=list_str_to_int(fields[5].split("-")),
                    words=list_str_to_int(fields[6].split("-"))
                )
        return None
    except IOError as err:
        print(f"Error: {err}")


def save_to_file(record: Record, file_path: str) -> bool:
    try:
        strings = []
        record_string_index = -1
        with open(file=file_path, mode="r", encoding="utf-8") as f:
            strings = f.read().split("\n")
        for str_index in range(len(strings)):
            fields = strings[str_index].split("\t")
            if fields[0] == str(record['id']):
                record_string_index = str_index
                break
        f.close()
        new_string = f"{record['id']}\t{record['title']}\t{record['note']}\t{record['source_id']}\t{'-'.join(record['pages'])}\t{'-'.join(record['paragraphs'])}\t{'-'.join(record['words'])}"
        if (record_string_index == -1):
            strings.append(new_string)
        else:
            strings[record_string_index] = new_string
        with open(file=file_path, mode="w", encoding="utf-8") as f:
            f.write("\n".join(strings))
        f.close()
        return True
    except IOError as err:
        print(f"Error: {err}")
        return False


def remove_from_file(record_id: int, file_path: str) -> bool:
    try:
        strings = []
        record_string_index = -1
        with open(file=file_path, mode="r", encoding="utf-8") as f:
            strings = f.read().split("\n")
        for str_index in range(len(strings)):
            fields = strings[str_index].split("\t")
            if fields[0] == str(record_id):
                record_string_index = str_index
                break
        f.close()
        if record_string_index == -1:
            return False
        else:
            strings[record_string_index] = ""
        with open(file=file_path, mode="w", encoding="utf-8") as f:
            f.write("\n".join(strings))
        f.close()
        remove_empty_strings_in_file(file_path=file_path)
        return True
    except IOError as err:
        print(f"Error: {err}")
        return False
