from abc import ABC


class AbstractAttaque(ABC):
    def __init__(self, nom, preposition):
        self.nom = nom
        self.preposition = preposition
