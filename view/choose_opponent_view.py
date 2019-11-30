from PyInquirer import prompt, Separator

from combattant_prégénérés import sac_de_frappe, son_goku
from view.abstract_view import AbstractView
from view.combat_view import CombatView


class ChooseOpponentView(AbstractView):
    liste_action = [
        "Aller au dojo",
        Separator()
    ]
    liste_combattant = [
        sac_de_frappe.sac_de_frappe,
        son_goku.son_goku
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
        self.questions[0]["choices"] = \
            self.liste_action + liste_combattant_affichable
        reponse = prompt(self.questions)

        vue_retournee = None
        if reponse['selection_adversaire'] == self.liste_action[0]:
            from view.dojo_view import DojoView
            vue_retournee = DojoView()
        else:
            index_combattant = liste_combattant_affichable.index(
                reponse['selection_adversaire'])
            adversaire = self.liste_combattant[index_combattant]
            AbstractView.session.adversaire = adversaire
            vue_retournee = CombatView()
        return vue_retournee
