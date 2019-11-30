from combattant_prégénérés import son_goku
from view.abstract_view import AbstractView
from view.main_menu import MainMenu

if __name__ == '__main__':

    AbstractView.session.combattant = son_goku.son_goku
    # on démarre sur l'écran accueil
    current_vue = MainMenu()

    # tant qu'on a un écran à afficher, on continue
    while current_vue:
        # on affiche une bordure pour séparer les vue
        # with open('assets/border.txt', 'r', encoding="utf-8") as asset:
        #     print(asset.read())
        # les infos à afficher
        current_vue.display_info()
        # le choix que doit saisir l'utilisateur
        current_vue = current_vue.make_choice()

    # with open('assets/cat.txt', 'r', encoding="utf-8") as asset:
    #     print(asset.read())
