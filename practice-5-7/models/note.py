from typing import Dict, TypedDict, Optional
from config.config import get_config
from utils.files import read_from_file, save_to_file, remove_from_file


RECORD_KEYS = {
    "text": str,
}


class Note(TypedDict):
    id: Optional[int]
    text: str


def create(
        note_id: Optional[int] = None,
        text: str = ""
    ) -> bool:
    new_note = Note(
        id=note_id,
        text=text
    )
    return save_note_to_file(note=new_note)


def read(note_id: int) -> Optional[Note]:
    return read_note_from_file(note_id=note_id)


def update(note_id: int, values_dict: Dict[str, type]) -> bool:
    updating_note = read_note_from_file(note_id=note_id)
    if updating_note == None:
        return False
    for key in values_dict.keys():
        if key in RECORD_KEYS.keys() and type(values_dict[key]) is RECORD_KEYS[key]:
            updating_note[key] = values_dict[key]
    return save_note_to_file(note=updating_note)  


def delete(note_id: int) -> bool:
    return remove_note_from_file(note_id=note_id)


def read_note_from_file(note_id: int) -> Optional[Note]:
    note_fields = read_from_file(id=note_id, file_path=get_config()["NOTE_FILE"])
    if note_fields != None:
        return Note(
            id=int(note_fields[0]),
            text=note_fields[1],
        )
    return None


def save_note_to_file(note: Note) -> bool:
    note_fields = []
    note_fields.append(note['id'])
    note_fields.append(note['text'])
    save_to_file(entity_fields=note_fields, file_path=get_config()["NOTE_FILE"])


def remove_note_from_file(note_id: int) -> bool:
    return remove_from_file(id=note_id, file_path=get_config()["NOTE_FILE"])
