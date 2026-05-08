from controllers.view_controller import ViewController
from views.list_view import ListView


class ListController(ViewController):
    def __init__(self):
        list_view = ListView()
        super().__init__(view=list_view)