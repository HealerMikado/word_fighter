class Round:
    def __init__(self, premier_attaquant, second_attaquant, combat):
        self.premier_attaquant = premier_attaquant
        self.second_attaquant = second_attaquant
        self.frames = []
        self.combat = combat
        self.pv_final_premier_attaquant = premier_attaquant.points_de_vie_actuel
        self.pv_final_second_attaquant = second_attaquant.points_de_vie_actuel

    def set__pv_final_premier_attaquant(self, new_pv_final):
        self.pv_final_premier_attaquant = max(0, new_pv_final)

    def set__pv_final_second_attaquant(self, new_pv_final):
        self.pv_final_second_attaquant = max(0, new_pv_final)
