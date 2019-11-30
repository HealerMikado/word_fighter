from business_object.abstract_attaque import AbstractAttaque


class Attaque(AbstractAttaque):
    def __init__(self, nom, preposition):
        super(Attaque, self).__init__(nom, preposition)

    def __str__(self):
        return (("%s %s") % (self.preposition, self.nom))
