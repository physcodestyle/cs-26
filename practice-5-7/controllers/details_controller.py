from controllers.view_controller import ViewController
from views.details_view import DetailsView


class DetailsController(ViewController):
    def __init__(self):
        details_view = DetailsView()
        super().__init__(view=details_view)