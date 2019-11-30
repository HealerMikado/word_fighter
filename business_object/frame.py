from business_object.attaque import Attaque


class Frame:
    attaque_defaut = Attaque("coup", "un")

    def __init__(self, attaquant, defenseur, degat=0, est_critique=False,
                 est_esquive=False):
        self.attaquant = attaquant
        self.defenseur = defenseur
        self.degat = degat
        self.est_critique = est_critique
        self.est_esquive = est_esquive

    def __str__(self):
        output = ""
        if self.est_critique:
            output = "{attaquant} lance {nom_attaque} à {defenseur} et inflige {deg} dégâts!!!".format(
                attaquant=self.attaquant.nom,
                nom_attaque=self.attaquant.nom_attaque_speciale,
                defenseur=self.defenseur.nom,
                deg=self.degat)
        elif self.est_esquive:
            output = "{defenseur} esquive gracieusement l'attaque".format(
                defenseur=self.defenseur.nom)
        else:
            output = "{attaquant} donne {nom_attaque} à {defenseur} et " \
                     "inflige {deg} dégâts".format(
                attaquant=self.attaquant.nom,
                defenseur=self.defenseur.nom,
                nom_attaque=self.attaque_defaut,
                deg=self.degat)
        return output
