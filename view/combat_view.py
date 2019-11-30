from service.combat_service import CombatService
from view.abstract_view import AbstractView


class CombatView(AbstractView):
    def display_info(self):
        combat_service = CombatService(AbstractView.session.combattant,
                                       AbstractView.session.adversaire)
        combat_service.deroule_combat()
        round_number = 1
        print("---------------------------")
        print("          Combat           ")
        print("---------------------------")
        print(AbstractView.session.combattant.nom)
        print("------------>  ")
        print("           CONTRE ")
        print("               <------------")
        print("               " + AbstractView.session.adversaire.nom)
        print()
        # Boucle sur les rounds
        for round in combat_service.combat.rounds:
            print("------------")
            print("Round {round_number}".format(round_number=round_number))
            print("{combattant1} est le plus rapide et frappe en "
                  "premier".format(combattant1=round.premier_attaquant.nom))
            # boucle sur les frame
            for frame in round.frames:
                print(frame)
            round_number += 1
            print("PV à la fin du round {round_number}".format(
                round_number=round_number))
            print("{attaquant1} : {pv_attaquant1} PV".format(
                attaquant1=round.premier_attaquant.nom,
                pv_attaquant1=round.pv_final_premier_attaquant))
            print("{attaquant2} : {pv_attaquant2} PV".format(
                attaquant2=round.second_attaquant.nom,
                pv_attaquant2=round.pv_final_second_attaquant))
            print()

    def make_choice(self):
        pass
