from business_object.attaque import Attaque
from business_object.combattant import Combattant

vegeta = Combattant(
    nom="Vegeta",
    attaque=50,
    precision=50,
    niveau=1,
    defense=50,
    esquive=50,
    critical=50,
    nom_attaque_speciale=Attaque("Garlic Gun", "un"))
