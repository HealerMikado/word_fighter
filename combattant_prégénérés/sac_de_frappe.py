from business_object.attaque import Attaque
from business_object.combattant import Combattant

sac_de_frappe = Combattant(
    nom="Sac de frappe",
    attaque=0,
    precision=0,
    niveau=1,
    defense=30,
    esquive=30,
    critical=1,
    vitesse=1,
    points_de_vie_max=10000,
    nom_attaque_speciale=Attaque("calin", "un")
)
