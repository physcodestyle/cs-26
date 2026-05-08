from models.model import Model
from controllers.controller import Controller


class State:
    def __init__(self, id: int, model: Model, controller: Controller):
        self.id = id
        self.model = model
        self.controller = controller


class Branch:
    pass


class StateGraph:
    pass