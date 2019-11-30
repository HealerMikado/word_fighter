from abc import ABC

from view.session import Session


class AbstractView(ABC):
    session = Session()

    def display_info(self):
        pass

    def make_choice(self):
        pass
