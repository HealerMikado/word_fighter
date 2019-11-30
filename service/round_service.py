from business_object.round import Round
from service.combattant_service import CombattantService
from service.frame_service import FrameService
from service.random_service import RandomService


class RoundService:
    def __init__(self, combattant1, combattant2, combatService):
        ordre = RoundService.choose_order(combattant1, combattant2)
        self.round = Round(ordre[0], ordre[1], combatService.combat)
        self.combat_service = combatService

    @staticmethod
    def choose_order(combattant1, combattant2):
        ordre_attaque = []
        while not ordre_attaque:
            init1 = RandomService.generate_int_number(0,
                                                      50) + combattant1.vitesse
            init2 = RandomService.generate_int_number(0,
                                                      50) + combattant2.vitesse
            if init1 < init2:
                ordre_attaque.append(combattant2)
                ordre_attaque.append(combattant1)
            elif init2 < init1:
                ordre_attaque.append(combattant1)
                ordre_attaque.append(combattant2)
        return ordre_attaque

    def round_action(self):
        # Première attaque du round
        self.round_attaque(self.round.premier_attaquant,
                           self.round.second_attaquant)
        CombattantService.infliger_degats(self.round.second_attaquant,
                                          self.round.frames[-1].degat)
        if not self.combat_service.est_combat_termine():
            # seconde attaque du round
            self.round_attaque(self.round.second_attaquant,
                               self.round.premier_attaquant)
            CombattantService.infliger_degats(self.round.premier_attaquant,
                                              self.round.frames[-1].degat)
            self.combat_service.est_combat_termine()
        return self.round

    def round_attaque(self, attaquant, defenseur):
        frame_service = FrameService(attaquant,
                                     defenseur)
        self.round.frames.append(frame_service.generateFrame())
