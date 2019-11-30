from unittest import TestCase

from business_object.combattant import Combattant
from service.combattant_service import CombattantService


class TestCombattantService(TestCase):
    def test_creation_combattant(self):
        # given
        nom = "Son Goku"
        # when
        actual_combattant = CombattantService.creation_combattant(nom)
        # then
        expected_combattant = Combattant(
            nom=nom,
            attaque=66,
            defense=57,
            esquive=60,
            critical=36,
            niveau=1,
            points_de_vie_max=740,
            precision=87,
            initiative=64
        )
        self.assertEqual(expected_combattant.nom, actual_combattant.nom)
        self.assertEqual(expected_combattant.attaque, actual_combattant.attaque)
        self.assertEqual(expected_combattant.defense, actual_combattant.defense)
        self.assertEqual(expected_combattant.esquive, actual_combattant.esquive)
        self.assertEqual(expected_combattant.points_de_vie,
                         actual_combattant.points_de_vie)
        self.assertEqual(expected_combattant.precision,
                         actual_combattant.precision)
        self.assertEqual(expected_combattant.initiative,
                         actual_combattant.initiative)
        self.assertEqual(expected_combattant.critical,
                         actual_combattant.critical)
