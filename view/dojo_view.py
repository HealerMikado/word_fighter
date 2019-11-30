from PyInquirer import prompt
from tabulate import tabulate

from view.abstract_view import AbstractView


class DojoView(AbstractView):
    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'Que voulez vous faire ?',
            'choices': ["Retourner sur l'écran de selection d'un adversaire"]
        }
    ]

    def display_info(self):
        table = [
            ["Points de vie",
             AbstractView.session.combattant.points_de_vie_max],
            ["Niveau", AbstractView.session.combattant.niveau],
            ["Attaque spéciale",
             AbstractView.session.combattant.nom_attaque_speciale],
            ["Attaque", AbstractView.session.combattant.attaque],
            ["Precision", AbstractView.session.combattant.precision],
            ["Critical", AbstractView.session.combattant.critical],
            ["Defense", AbstractView.session.combattant.defense],
            ["Esquive", AbstractView.session.combattant.esquive],
            ["Vitesse", AbstractView.session.combattant.vitesse]
        ]
        print("--------------------")
        print("Statitique de {nom}".format(
            nom=AbstractView.session.combattant.nom))
        print("--------------------")
        print()
        print(tabulate(table, tablefmt="github"))

    def make_choice(self):
        reponse = prompt(self.questions)
        if reponse['action'] == "Retourner sur l'écran de selection d'un " \
                                "adversaire":
            from view.choose_opponent_view import ChooseOpponentView
            return ChooseOpponentView()
