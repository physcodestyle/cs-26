from typing import List, TypedDict


class Record(TypedDict):
    id: str
    title: str
    note: str
    source_id: str
    pages: List[str]
    paragraphs: List[str]
    words: List[str]


def create_record(id: str, title: str, note: str = "", source_id: str = "", pages: List[str] = {}, paragraphs: List[str] = {}, words: List[str] = {}) -> Record:
    return Record(
        id=id,
        title=title,
        note=note,
        source_id=source_id,
        pages=pages,
        paragraphs=paragraphs,
        words=words
    )


def print_record(record: Record):
    print(record)


def read(record_id: int, file_path: str) -> Record:
    try:
        strings = []
        with open(file=file_path, mode="r", encoding="utf-8") as f:
            strings = f.read().split("\n")
        f.close()
        for str_index in range(len(strings)):
            fields = strings[str_index].split("\t")
            if fields[0] == str(record_id):
                return create_record(
                    id=fields[0],
                    title=fields[1],
                    note=fields[2],
                    source_id=fields[3],
                    pages=fields[4].split("-"),
                    paragraphs=fields[5].split("-"),
                    words=fields[6].split("-")
                )
        return None
    except IOError as err:
        print(f"Error: {err}")


def save(record: Record, file_path: str):
    try:
        strings = []
        record_string_index = -1
        with open(file=file_path, mode="r", encoding="utf-8") as f:
            strings = f.read().split("\n")
        for str_index in range(len(strings)):
            fields = strings[str_index].split("\t")
            if fields[0] == record['id']:
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
    except IOError as err:
        print(f"Error: {err}")
