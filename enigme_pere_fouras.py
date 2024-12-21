import json
import random
import time

def charger_enigmes() :
    with open ("data/enigmesPF.json", "r",encoding= 'utf-8') as f :
        donnees = json.load(f)
    return donnees


def enigme_pere_fouras() :
    dico = {}
    liste_enigmes = charger_enigmes()
    enigme_choisie = random.choice(liste_enigmes)
    for i in enigme_choisie:
        print(enigme_choisie[i])

    print(enigme_choisie)

enigme_pere_fouras()

