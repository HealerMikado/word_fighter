from business_object.attaque import Attaque


class Combattant:
    def __init__(self, nom, attaque=0, precision=0, defense=0,
                 esquive=0, critical=0, points_de_vie_max=0, vitesse=0,
                 niveau=1,
                 arme=None,
                 armure=None, nom_attaque_speciale=Attaque("Critical", "un"),
                 accessoires=[None]):
        self.nom = nom
        self.attaque = attaque
        self.precision = precision
        self.defense = defense
        self.esquive = esquive
        self.critical = critical
        self.points_de_vie_max = points_de_vie_max
        self.points_de_vie_actuel = points_de_vie_max
        self.vitesse = vitesse
        self.niveau = niveau
        self.arme = arme
        self.armure = armure
        self.nom_attaque_speciale = nom_attaque_speciale
        self.accessoires = accessoires
