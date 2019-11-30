from unittest import TestCase, mock

from service.random_service import RandomService


class TestRandomService(TestCase):
    @mock.patch('service.random_service.RandomService.generate_int_number',
                return_value=40)
    def test_generate_int_number(self, generate_int_number):
        self.assertEqual(RandomService.generate_int_number(10, 50), 40)
