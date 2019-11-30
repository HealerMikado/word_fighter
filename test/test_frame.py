from unittest import TestCase

from business_object.frame import Frame
from combattant_prégénérés import son_goku, vegeta


class TestFrame(TestCase):
    def test___str__critique(self):
        # given
        frame = Frame(son_goku.son_goku, vegeta.vegeta, 10, True,
                      False)
        # when
        # then
        expected_string = "Son Goku lance un Kamehameha à Vegeta et inflige " \
                          "10 dégâts!!!"
        self.assertEqual(
            expected_string,
            frame.__str__()
        )

    def test___str__critique_esquive(self):
        # given
        frame = Frame(son_goku.son_goku, vegeta.vegeta, 10, True, True)
        # when
        # then
        expected_string = "Son Goku lance un Kamehameha à Vegeta et inflige " \
                          "10 dégâts!!!"
        self.assertEqual(
            expected_string,
            frame.__str__()
        )

    def test___str__esquive(self):
        # given
        frame = Frame(son_goku.son_goku, vegeta.vegeta, 10, False, True)
        # when
        # then
        expected_string = "Vegeta esquive gracieusement l'attaque"
        self.assertEqual(
            expected_string,
            frame.__str__()

        )

    def test___str__normal(self):
        # given
        frame = Frame(son_goku.son_goku, vegeta.vegeta, 10, False,
                      False)
        # when
        # then
        expected_string = "Son Goku donne un coup Vegeta et inflige 10 dégâts"
        self.assertEqual(
            expected_string,
            frame.__str__()

        )
