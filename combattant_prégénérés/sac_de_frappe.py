from business_object.attaque import Attaque
from business_object.combattant import Combattant

sac_de_frappe = Combattant(
    nom="Sac de frappe",
    attaque=10,
    precision=10,
    niveau=1,
    defense=10,
    esquive=10,
    critical=10,
    vitesse=10,
    points_de_vie_max=10000,
    nom_attaque_speciale=Attaque("calin", "un")
)
