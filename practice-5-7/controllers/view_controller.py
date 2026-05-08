from typing import Tuple
from views.view import View


CONTROLLER_CODE = -1


class ViewController:
    def __init__(self, view: View):
        self.view = view


    def __init__(self):
        view = View()
        self.view = view
    

    def show(self, data: any, state: int) -> Tuple[any, int, int]:
        next_data, next_state = self.view.change_state(data=data, state=state)
        return (next_data, next_state, CONTROLLER_CODE)