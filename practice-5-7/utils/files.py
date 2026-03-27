from typing import List, Optional


def read_from_file(id: int, file_path: str) -> Optional[List]:
    try:
        strings = []
        with open(file=file_path, mode="r", encoding="utf-8") as f:
            strings = f.read().split("\n")
        f.close()
        for str_index in range(len(strings)):
            fields = strings[str_index].split("\t")
            if fields[0] == str(id):
                return fields
        return None
    except IOError as err:
        print(f"Error: {err}")


def save_to_file(entity_fields: List, file_path: str) -> bool:
    try:
        strings = []
        empty_string_indices = []
        string_index = -1
        max_index = 0
        with open(file=file_path, mode="r", encoding="utf-8") as f:
            strings = f.read().split("\n")
        for str_index in range(len(strings)):
            if strings[str_index] == "":
                empty_string_indices.append(str_index)
            else:
                fields = strings[str_index].split("\t")
                field_index = int(fields[0])
                if entity_fields[0] != None and field_index == entity_fields[0]:
                    string_index = str_index
                    break
                if field_index > max_index:
                    max_index = field_index
        f.close()
        new_string = "\t".join(entity_fields[1:])
        if entity_fields[0] == None:
            new_string = f"{max_index + 1}\t" + new_string
        else:
            new_string = f"{entity_fields[0]}\t" + new_string
        if string_index == -1:
            strings.append(new_string)
        else:
            strings[string_index] = new_string
        if len(empty_string_indices) > 0:
            empty_string_indices.reverse()
            for str_index in empty_string_indices:
                strings.pop(str_index)
        with open(file=file_path, mode="w", encoding="utf-8") as f:
            f.write("\n".join(strings))
        f.close()
        return True
    except IOError as err:
        print(f"Error: {err}")
        return False


def remove_from_file(id: int, file_path: str) -> bool:
    try:
        strings = []
        string_index = -1
        with open(file=file_path, mode="r", encoding="utf-8") as f:
            strings = f.read().split("\n")
        for str_index in range(len(strings)):
            fields = strings[str_index].split("\t")
            if fields[0] == str(id):
                string_index = str_index
                break
        f.close()
        if string_index == -1:
            return False
        else:
            strings[string_index] = ""
        with open(file=file_path, mode="w", encoding="utf-8") as f:
            f.write("\n".join(strings))
        f.close()
        return True
    except IOError as err:
        print(f"Error: {err}")
        return False
