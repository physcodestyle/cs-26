from typing import List, Tuple


class View:
    def __init__(self):
        self.prompt_text = "> "


    def change_state(self, data: any, state: int) -> Tuple[any, int]:
        self.print_response(response=data)
        new_data = self.get_user_request(request="Default view prompt")
        return (new_data[0], state)


    def get_user_request(self, request: str) -> List[str]:
        return input(f"{request} {self.prompt_text}").split(" ")


    def print_response(self, response: str):
        print(f"--------\n\n{response}\n\n")
