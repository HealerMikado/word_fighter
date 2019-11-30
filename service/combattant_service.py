import hashlib

from business_object.combattant import Combattant


class CombattantService():

    @staticmethod
    def creation_combattant(mot):
        """
        Hashe un mot pour créer un personnage à partir
        du hash.

        :param mot: le mot saisi par l'utilisateur
        à la création de son personnage.
        :return: Un combatant généré à partir du hash
        produit par le mot saisi par l'utilisateur
        """
        # On hash le mot, le tranforme en str, puis on le coupe
        # la chaine en sous chaine de taille 4 qu'on
        # passe ensuite en int base 10
        hash = str(int(hashlib.sha224(mot.encode()).hexdigest(), 16))
        list_value = [int(hash[i:i + 2], 16) for i in range(0, len(hash), 2)]
        size_sample = len(list_value) // 7
        attaque = CombattantService.createStat(list_value, size_sample)
        precision = CombattantService.createStat(list_value, size_sample)
        defense = CombattantService.createStat(list_value, size_sample)
        esquive = CombattantService.createStat(list_value, size_sample)
        critical = CombattantService.createStat(list_value, size_sample)
        initiative = CombattantService.createStat(list_value, size_sample)
        points_de_vie = CombattantService.createStat(list_value,
                                                     size_sample) * 10
        combattant_cree = Combattant(nom=mot, attaque=attaque,
                                     precision=precision, defense=defense,
                                     esquive=esquive,
                                     critical=critical,
                                     vitesse=initiative,
                                     niveau=1,
                                     points_de_vie_max=points_de_vie)

        return combattant_cree

    @staticmethod
    def createStat(list, size):
        """
        /!\ on va retirer des éléments de list, donc l'altérer !
        :param list: la liste dont on va prendre les valeurs
        :param size: le nombre de valeur que l'on veut
        :return: la somme des valeurs prise
        """
        value = 0
        for i in range(size):
            value += list.pop()
        return value // size

    @staticmethod
    def infliger_degats(combattant, degat):
        """
        Dimiue les pv d'un combattant
        :param combattant: le combattant à blesser
        :param degat: les dégâts infligé
        :return:
        """
        combattant.points_de_vie_actuel -= degat

    @staticmethod
    def remise_a_zero_degat(combattant):
        combattant.points_de_vie_actuel = combattant.points_de_vie_max
