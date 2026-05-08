from typing import List, Dict, TypedDict, Optional
from models.model import Model
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


class AuthorModel(Model[Author]):
    def __init__(self, file_name = get_config()["AUTHOR_FILE"], fields = RECORD_KEYS):
        super().__init__(file_name, fields)


    def search(self, values_dict: Dict[str, any]) -> List[Author]:
        pass


    def create(
            self,
            id: Optional[int] = None,
            first_name: str = "",
            middle_name: str = "",
            last_name: str = "",
            science_degree: str = "",
            science_title: str = "",
            notes: List[int] = []
        ) -> bool:
        new_author = Author(
            id=id,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            science_degree=science_degree,
            science_title=science_title,
            notes=notes,
        )
        return self.save_author_to_file(author=new_author)


    def read(self, id: int) -> Optional[Author]:
        return self.read_author_from_file(id=id)


    def update(self, id: int, values_dict: Dict[str, any]) -> bool:
        updating_author = self.read_author_from_file(id=id)
        if updating_author == None:
            return False
        for key in values_dict.keys():
            if key in self.fields.keys() and type(values_dict[key]) is self.fields[key]:
                updating_author[key] = values_dict[key]
        return self.save_author_to_file(author=updating_author)  


    def delete(self, id: int) -> bool:
        return self.remove_author_from_file(id=id)


    def read_author_from_file(self, id: int) -> Optional[Author]:
        author_fields = read_from_file(id=id, file_path=self.file_name)
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


    def save_author_to_file(self, author: Author) -> bool:
        author_fields = []
        author_fields.append(author['id'])
        author_fields.append(author['first_name'])
        author_fields.append(author['middle_name'])
        author_fields.append(author['last_name'])
        author_fields.append(author['science_degree'])
        author_fields.append(author['science_title'])
        author_fields.append('-'.join(list_int_to_str(author['notes'])))
        save_to_file(entity_fields=author_fields, file_path=self.file_name)


    def remove_author_from_file(self, id: int) -> bool:
        return remove_from_file(id=id, file_path=self.file_name)
