import math

from business_object.frame import Frame
from service.random_service import RandomService


class FrameService:
    def __init__(self, theAttaquant, theDefenseur):
        self.frame = Frame(theAttaquant, theDefenseur)

    def generateFrame(self):
        """
        Permet de créer une frame de combat. Va tester les différents
        cas possible
            - critique
            - esquive
            - attaque normale
        :return: la frame générée
        """
        if self.isCritical():
            self.frame.est_critique = True
            self.frame.degat = self.degat_Crit()
        elif not self.isHit():
            self.frame.est_esquive = True

        else:
            self.frame.est_critique = False
            self.frame.degat = self.degat_nonCrit()

        return self.frame

    def isCritical(self):
        """
        Retourne si l'attaque est un critique
        P(critique) =min(50, (crit/5)*(niv_att/niv_def))
        :return: true si critique, false sinon
        """
        proba = min(50, self.frame.attaquant.critical // 5 * (
                self.frame.attaquant.niveau // self.frame.defenseur.niveau))
        generated_number = RandomService.generate_int_number(1, 100)
        return generated_number <= proba

    def isHit(self):
        """
        Retourne si l'attaque touche
        P(hit) =max(10, 50+(precision/esquive)*(niv_att/niv_def))
        :return: true si touche
        """
        proba = max(10, 50 +
                    self.frame.attaquant.precision // self.frame.defenseur.esquive * (
                            self.frame.attaquant.niveau // self.frame.defenseur.niveau))
        generated_number = RandomService.generate_int_number(1, 100)
        return generated_number < proba

    def degat_nonCrit(self):
        """
         Retourne les dégâts de l'attaque
        degats = random(20,50)*((niv_att*0.4+2)*att)/(def*niv_def*0.4) +
        random(10,30)
        :return: les degats
        """

        return math.floor(RandomService.generate_int_number(20, 50)
                          * ((
                                     self.frame.attaquant.niveau * 0.4 + 2) * self.frame.attaquant.attaque)
                          // (
                                  self.frame.defenseur.niveau * 0.4 * self.frame.defenseur.defense)
                          + RandomService.generate_int_number(10, 30))

    def degat_Crit(self):
        """
         Retourne les dégâts de l'attaque si critique
        degats = random(20,50)*((niv_att*0.4+2)*att)/(def*niv_def*0.1) +
        random(10,30)
        :return: les degats
        :return:
        """
        return math.floor(RandomService.generate_int_number(20, 50)
                          * ((
                                     self.frame.attaquant.niveau * 0.4 + 2) * self.frame.attaquant.attaque)
                          // (self.frame.defenseur.niveau * 0.1 *
                              self.frame.defenseur.defense)
                          + RandomService.generate_int_number(10, 30))
