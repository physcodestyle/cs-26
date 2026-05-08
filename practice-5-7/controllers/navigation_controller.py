from typing import Tuple
from enum import Enum
from controllers.view_controller import ViewController
from controllers.details_controller import DetailsController
from controllers.list_controller import ListController
from controllers.table_controller import TableController


class NavigationCode(Enum):
    DEFAULT_CONTROLLER = -1
    DETAILS_CONTROLLER = 0
    LIST_CONTROLLER = 1
    TABLE_CONTROLLER = 2


class NavigationController:
    def __init__(self, data: any, state: int, default_controller: int = NavigationCode.DEFAULT_CONTROLLER):
        self.current_controller = None
        next_data, next_state, next_code = self.change_view_controller(data=data, state=state, controller=default_controller)
        self.next_data = next_data
        self.next_state = next_state
        self.next_controller = next_code


    def next(self) -> int:
        next_data, next_state, next_code = self.change_view_controller(
            data=self.next_data,
            state=self.next_state,
            controller=self.next_controller
        )
        self.next_data = next_data
        self.next_state = next_state
        self.next_controller = next_code
        if self.next_data == "exit":
            return -1
        return 0

    
    def change_view_controller(self, data: any, state: int, controller: NavigationCode) -> Tuple[any, int, int]:
        if controller == NavigationCode.DETAILS_CONTROLLER:
            self.current_controller = DetailsController()
        elif controller == NavigationCode.LIST_CONTROLLER:
            self.current_controller = ListController()
        elif controller == NavigationCode.TABLE_CONTROLLER:
            self.current_controller = TableController()
        else:
            self.current_controller = ViewController()
        return self.current_controller.show(data=data, state=state)
