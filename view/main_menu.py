from PyInquirer import prompt

from combattant_prégénérés import sac_de_frappe
from view.abstract_view import AbstractView
from view.combat_view import CombatView


class MainMenu(AbstractView):
    liste_combattant = [
        sac_de_frappe.sac_de_frappe,
    ]

    questions = [
        {
            'type': 'list',
            'name': 'selection_adversaire',
            'message': 'Qui voulez vous affronter ?',
            'choices': []
        }
    ]

    def display_info(self):
        pass

    def make_choice(self):
        liste_combattant_affichable = [
            "{nom} (niveau {niv})".format(nom=combattant.nom,
                                          niv=combattant.niveau)
            for combattant in self.liste_combattant]
        self.questions[0]["choices"] = liste_combattant_affichable
        reponse = prompt(self.questions)
        index_combattant = liste_combattant_affichable.index(
            reponse['selection_adversaire'])
        adversaire = self.liste_combattant[index_combattant]
        AbstractView.session.adversaire = adversaire
        return CombatView()
