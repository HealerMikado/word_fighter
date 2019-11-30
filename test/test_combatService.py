from unittest import TestCase

from business_object.attaque import Attaque
from business_object.combattant import Combattant
from service.combat_service import CombatService


class TestCombatService(TestCase):
    attaquant = Combattant(
        nom="Son Goku",
        attaque=50,
        precision=50,
        niveau=1,
        defense=50,
        esquive=50,
        critical=50,
        vitesse=50,
        points_de_vie_max=1000,
        nom_attaque_speciale=Attaque("Kamehameha", "un")
    )
    defenseur = Combattant(
        nom="Sac de frappe",
        attaque=10,
        precision=10,
        niveau=1,
        defense=10,
        esquive=10,
        critical=10,
        vitesse=10,
        points_de_vie_max=10000,
        nom_attaque_speciale=Attaque("calin", "un")
    )

    def test_deroule_combat(self):
        # GIVEN
        combat_service = CombatService(self.attaquant, self.defenseur)
        # WHEN
        combat_service.deroule_combat()
        # THEN
        self.assertEqual(self.attaquant, combat_service.combat.gagnant)
