import random


class RandomService:
    @staticmethod
    def generate_int_number(min, max):
        """
        Retourne un nombre aléatoire compris entre [min,max]
        :param min: le min de l'interval inclu
        :param max: le max de l'interval inclu
        :return: un nombre aléatoire
        """
        return random.randint(min, max)
