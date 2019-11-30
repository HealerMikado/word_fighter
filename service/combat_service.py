from business_object.combat import Combat
from service.round_service import RoundService


class CombatService:
    def __init__(self, combattant1, combattant2):
        self.combat = Combat(combattant1, combattant2)

    def new_round(self):
        """
        Créer un round et l'ajoute à la liste des rounds du combat
        :return:
        """
        round_service = RoundService(self.combat.combattant1,
                                     self.combat.combattant2,
                                     self)
        round_courant = round_service.round_action()
        self.combat.rounds.append(round_courant)

    def deroule_combat(self):
        """
        Méthode qui va éxécuter le combat. Tant qu'il n'y a pas de gagnant
        le combat continue
        :return:
        """
        while not self.combat.gagnant:
            self.new_round()

    def est_combat_termine(self):
        """
        Détermine si le combat est terminé. Un combat se termine si un des
        combattant a ses pv <=0. Set le gagnant et le perdant
        :return: True si combat termine, False sinon, set gagnant et perdant
        """
        output = False
        if self.combat.combattant1.points_de_vie_actuel <= 0:
            output = True
            self.set_gagnant_perdant(self.combat.combattant2,
                                     self.combat.combattant2)
        elif self.combat.combattant2.points_de_vie_actuel <= 0:
            output = True
            self.set_gagnant_perdant(self.combat.combattant1,
                                     self.combat.combattant2)
        return output

    def set_gagnant_perdant(self, gagnant, perdant):
        self.combat.gagnant = gagnant
        self.combat.perdant = perdant
