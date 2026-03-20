from typing import List


def list_str_to_int(list: List[str]) -> List[int]:
    new_list = []
    for item in list:
        new_list.append(int(item))
    return new_list
