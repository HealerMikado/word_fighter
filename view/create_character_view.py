from PyInquirer import prompt

from business_object.attaque import Attaque
from service.combattant_service import CombattantService
from view.abstract_view import AbstractView
from view.choose_opponent_view import ChooseOpponentView


class CreateCharacterView(AbstractView):
    questions = [
        {
            'type': 'input',
            'name': 'character_creation',
            'message': 'Quel est le nom de votre personnage',
        },
        {
            'type': 'input',
            'name': 'critical',
            'message': 'Quel est votre super attaque sans déterminant devant?'
                       'Par exemple "rayons ardents"'
        },
        {
            'type': 'input',
            'name': 'determinant',
            'message': 'Quel est le derterminant devant votre super attaque ?'
                       'Par exemple "des"'
        }
    ]

    def display_info(self):
        print("""
        Bienvenu dans l'écran de création de combattant de word fighter. 
        """)

    def make_choice(self):
        reponse = prompt(self.questions)
        combattant_cree = CombattantService.creation_combattant(
            reponse['character_creation'])
        combattant_cree.nom_attaque_speciale = Attaque(reponse[
                                                           'critical'],
                                                       reponse['determinant'])
        AbstractView.session.combattant = combattant_cree
        return ChooseOpponentView()
