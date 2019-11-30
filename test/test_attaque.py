from unittest import TestCase

from business_object.attaque import Attaque


class TestAttaque(TestCase):
    def test___str__(self):
        # given
        tested_attk = Attaque("kamehameha", "un")
        # when
        actual_name = tested_attk.__str__()
        expected_name = "un kamehameha"
        # then
        self.assertEqual(expected_name, actual_name)
