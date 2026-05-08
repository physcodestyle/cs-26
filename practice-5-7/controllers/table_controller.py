from controllers.view_controller import ViewController
from views.table_view import TableView


class TableController(ViewController):
    def __init__(self):
        table_view = TableView()
        super().__init__(view=table_view)
