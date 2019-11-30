from unittest import TestCase, mock

from business_object.attaque import Attaque
from business_object.combattant import Combattant
from service import combat_service
from service.round_service import RoundService


class TestRoundService(TestCase):
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

    @mock.patch('service.round_service.RoundService.choose_order',
                return_value=[attaquant, defenseur])
    @mock.patch('service.combat_service.CombatService')
    @mock.patch('service.frame_service.FrameService.isCritical',
                return_value=False)
    @mock.patch('service.frame_service.FrameService.isHit',
                return_value=True)
    @mock.patch('service.random_service.RandomService.generate_int_number',
                return_value=11)
    def test_round_attaque(self, generate_int_number, isCritical, isHit,
                           combat_service_mock, choose_order):
        # Given
        round_service = RoundService(self.attaquant, self.defenseur,
                                     combat_service.CombatService())
        # When
        round_service.round_attaque(round_service.round.premier_attaquant,
                                    round_service.round.second_attaquant)
        # Then
        self.assertTrue(not round_service.round.frames[0].est_critique)
        self.assertEqual(round_service.round.frames[0].degat, 77)

    @mock.patch('service.round_service.RoundService.choose_order',
                return_value=[attaquant, defenseur])
    @mock.patch('service.combat_service.CombatService')
    @mock.patch('service.frame_service.FrameService.isCritical',
                return_value=False)
    @mock.patch('service.frame_service.FrameService.isHit',
                return_value=True)
    @mock.patch('service.random_service.RandomService.generate_int_number',
                return_value=11)
    def test_round_action(self, generate_int_number, isHit, isCritical,
                          combat_service_mock, choose_order):
        # Given
        combat_service_mock.return_value.est_combat_termine.return_value = \
            False
        round_service = RoundService(self.attaquant, self.defenseur,
                                     combat_service.CombatService())
        # When
        round_service.round_action()
        # Then
        self.assertTrue(not round_service.round.frames[0].est_critique)
        self.assertEqual(round_service.round.frames[0].degat, 77)

        self.assertTrue(not round_service.round.frames[1].est_critique)
        self.assertEqual(round_service.round.frames[1].degat, 77)

    @mock.patch('service.round_service.RoundService.choose_order',
                return_value=[attaquant, defenseur])
    @mock.patch('service.combat_service.CombatService')
    @mock.patch('service.frame_service.FrameService.isCritical',
                return_value=False)
    @mock.patch('service.frame_service.FrameService.isHit',
                return_value=True)
    @mock.patch('service.random_service.RandomService.generate_int_number',
                return_value=11)
    def test_round_action_victoire1(self,
                                    generate_int_number,
                                    isCritical,
                                    isHit,
                                    combat_service_mock,
                                    choose_order):
        # Given
        combat_service_mock.return_value.est_combat_termine.return_value = True
        round_service = RoundService(self.attaquant, self.defenseur,
                                     combat_service.CombatService())
        # When
        round_service.round_action()
        # Then
        # On a bien un seul round
        self.assertEqual(len(round_service.round.frames), 1)

    @mock.patch('service.round_service.RoundService.choose_order',
                return_value=[attaquant, defenseur])
    @mock.patch('service.combat_service.CombatService')
    @mock.patch('service.frame_service.FrameService.isCritical',
                return_value=False)
    @mock.patch('service.frame_service.FrameService.isHit',
                return_value=True)
    @mock.patch('service.random_service.RandomService.generate_int_number',
                return_value=11)
    def test_round_action_victoire2(self,
                                    generate_int_number,
                                    isCritical,
                                    isHit,
                                    combat_service_mock,
                                    choose_order):
        # Given
        combat_service_mock.return_value.est_combat_termine.side_effect = [
            False, True]
        round_service = RoundService(self.attaquant, self.defenseur,
                                     combat_service.CombatService())
        # When
        round_service.round_action()
        # Then
        self.assertEqual(len(round_service.round.frames), 2)
