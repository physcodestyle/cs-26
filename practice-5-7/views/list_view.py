from enum import Enum
from typing import Tuple
from views.view import View


class States(Enum):
    SHOW_LIST = 1
    INSERT_ITEM = 2
    READ_ITEM = 3
    UPDATE_ITEM = 4
    DELETE_ITEM = 5
    SAVING_ITEM = 6


class Operation(Enum):
    NO_ACTION = 0
    INSERT_ITEM = 1
    READ_ITEM = 2
    UPDATE_ITEM = 3
    DELETE_ITEM = 4


operation_name_dict = {
    "INSERT": Operation.INSERT_ITEM,
    "READ": Operation.READ_ITEM,
    "UPDATE": Operation.UPDATE_ITEM,
    "DELETE": Operation.DELETE_ITEM,
}


class ListView(View):
    def __init__(self):
        super().__init__()
        self.operations = []
        
    
    def change_state(self, data: any, state: int = States.SHOW_LIST.value) -> Tuple[any, int]:
        if state == States.SHOW_LIST.value:
            self.operations = data["operations"]
            self.print_response(response=data)
            operation, item_index = self.get_user_request(request="Prompt")
            return self.process_user_prompt(data=data, state=state, operation=operation, item_index=item_index)
        else:
            return (data, state)


    def get_user_request(self, state: int, request: str = "") -> Tuple[Operation, int]:
        if state == States.SHOW_LIST.value:
            for operation in self.operations:
                if operation == Operation.INSERT_ITEM:
                    print(f"Use 'INSERT <item_number>' for create a new list item")
                elif operation == Operation.READ_ITEM:
                    print(f"Use 'READ <item_number>' to show selected item's details")
                elif operation == Operation.UPDATE_ITEM:
                    print(f"Use 'UPDATE <item_number>' to update selected item's data")
                elif operation == Operation.DELETE_ITEM:
                    print(f"Use 'DELETE <item_number>' to delete selected item")
            prompt = input(f"{request} {self.prompt_text}").split(" ")
            operation = operation_name_dict[prompt.split(" ")[0]]
            item_index = int(prompt.split(" ")[1]) - 1
            return (operation, item_index)
        elif state == States.INSERT_ITEM.value:
            print(f"Set field(s) by following string '{request}' for create a new item")
            prompt = input(f"{self.prompt_text}").split(" | ")
        else:
            return (Operation.NO_ACTION, -1)


    def print_response(self, response: str):
        for item_index in range(len(response["list"])):
            print(response["preprocess"](response["list"][item_index], item_index + 1))


    def process_user_prompt(self, data: any, state: int, operation: str, item_index: int) -> Tuple[any, int]:
        if operation in self.operations and operation == Operation.INSERT_ITEM:
            return self.create_item(data=data, state=state, item_index=item_index)
        elif operation in self.operations and operation == Operation.READ_ITEM:
            return self.read_item(data=data, state=state, item_index=item_index)
        elif operation in self.operations and operation == Operation.UPDATE_ITEM:
            return self.update_item(data=data, state=state, item_index=item_index)
        elif operation in self.operations and operation == Operation.DELETE_ITEM:
            return self.delete_item(data=data, state=state, item_index=item_index)


    def create_item(self, data: any, state: int, item_index: int) -> Tuple[any, int]:
        if state == States.SHOW_LIST.value:
            return (None, States.INSERT_ITEM.value)
        elif state == States.INSERT_ITEM.value:
            if len(data['fields']) > 0:
                help_field_string = []
                for field in data['fields']:
                    help_field_string.append(f"<{field}>")
                help_string = " | ".join(help_field_string)
            else:
                help_string = "<field_value>"
                
            field_values = self.get_user_request(state=state, request=help_string)
            insertion_data = {
                "fields": field_values,
                "item_index": item_index
            }
            return (insertion_data, States.SAVING_ITEM.value)
        else:
            return (None, States.SHOW_LIST.value)


    def read_item(self, data: any, state: int, item_index: int) -> Tuple[any, int]:
        pass


    def update_item(self, data: any, state: int, item_index: int) -> Tuple[any, int]:
        pass


    def delete_item(self, data: any, state: int, item_index: int) -> Tuple[any, int]:
        pass