from controllers.view_controller import ViewController
from views.list_view import ListView


CONTROLLER_CODE = 1


# data = {
#     "preprocess": lambda item, index: f"{index}. {item}",
#     "operations": [Operation]
#     "fields": []
#     "list": []
# }


class ListController(ViewController):
    def __init__(self):
        list_view = ListView()
        super().__init__(view=list_view)
