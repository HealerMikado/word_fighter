from unittest import TestCase

from business_object.frame import Frame


class TestFrame(TestCase):
    def test___str__critique(self):
        # given
        frame = Frame("Son Goku", "Vegeta", 10, True, "un kamehameha", False)
        # when
        # then
        expected_string = "Son Goku lance un kamehameha à Vegeta et inflige 10 dégâts!!!"
        self.assertEqual(
            frame.__str__(),
            expected_string
        )

    def test___str__critique_esquive(self):
        # given
        frame = Frame("Son Goku", "Vegeta", 10, True, "un kamehameha", True)
        # when
        # then
        expected_string = "Son Goku lance un kamehameha à Vegeta et inflige 10 dégâts!!!"
        self.assertEqual(
            frame.__str__(),
            expected_string
        )

    def test___str__esquive(self):
        # given
        frame = Frame("Son Goku", "Vegeta", 10, False, "un kamehameha", True)
        # when
        # then
        expected_string = "Vegeta esquive gracieusement l'attaque"
        self.assertEqual(
            frame.__str__(),
            expected_string
        )

    def test___str__normal(self):
        # given
        frame = Frame("Son Goku", "Vegeta", 10, False, "un kamehameha", False)
        # when
        # then
        expected_string = "Son Goku attaque Vegeta et inflige 10 dégâts"
        self.assertEqual(
            frame.__str__(),
            expected_string
        )
