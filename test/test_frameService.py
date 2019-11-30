from unittest import TestCase, mock

from business_object.attaque import Attaque
from business_object.combattant import Combattant
from service.frame_service import FrameService


class TestFrameService(TestCase):
    attaquant = Combattant(
        nom="Son Goku",
        attaque=50,
        precision=50,
        niveau=1,
        defense=50,
        esquive=50,
        critical=50,
        nom_attaque_speciale=Attaque("Kamehameha", "un")
    )
    defenseur = Combattant(
        nom="Vegeta",
        attaque=50,
        precision=50,
        niveau=1,
        defense=50,
        esquive=50,
        critical=50,
        nom_attaque_speciale=Attaque("Garlic Gun", "un")
    )

    @mock.patch('service.random_service.RandomService.generate_int_number',
                return_value=10)
    def test_generateFrameCrit(self, generate_int_number):
        """
        Clairement une méthode difficile à tester à cause du random.
        Pour pallier à ce problème on va forcer le hasard
        """
        # Given
        frame_service = FrameService(self.attaquant, self.defenseur)
        # When
        actual_frame = frame_service.generateFrame()
        # Then
        self.assertTrue(actual_frame.est_critique)

    @mock.patch('service.random_service.RandomService.generate_int_number',
                return_value=11)
    @mock.patch('service.frame_service.FrameService.isCritical',
                return_value=False)
    @mock.patch('service.frame_service.FrameService.isHit',
                return_value=True)
    def test_generateFrameNotCrit(self, generate_int_number, isCritical, isHit):
        """
        Clairement une méthode difficile à tester à cause du random.
        Pour pallier à ce problème on va forcer le hasard
        """
        # Given
        frame_service = FrameService(self.attaquant, self.defenseur)
        # When
        actual_frame = frame_service.generateFrame()
        # Then
        self.assertTrue(not actual_frame.est_critique)
        self.assertEqual(actual_frame.degat, 77)

        @mock.patch('service.random_service.RandomService.generate_int_number',
                    return_value=11)
        @mock.patch('service.frame_service.FrameService.isHit',
                    return_value=True)
        def test_generateFrameNotCrit(self, generate_int_number, isHit):
            """
            Clairement une méthode difficile à tester à cause du random.
            Pour pallier à ce problème on va forcer le hasard
            """
            # Given
            frame_service = FrameService(self.attaquant, self.defenseur)
            # When
            actual_frame = frame_service.generateFrame()
            # Then
            self.assertTrue(not actual_frame.est_critique)
            self.assertEqual(actual_frame.degat, 77)

    @mock.patch('service.random_service.RandomService.generate_int_number',
                return_value=11)
    def test_generateFrameEsquive(self, generate_int_number):
        """
        Clairement une méthode difficile à tester à cause du random.
        Pour pallier à ce problème on va forcer le hasard
        """
        # Given
        frame_service = FrameService(self.attaquant, self.defenseur)
        # When
        actual_frame = frame_service.generateFrame()
        # Then
        self.assertTrue(actual_frame.est_esquive)
