from business_object.attaque import Attaque
from business_object.combattant import Combattant

son_goku = Combattant(
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
