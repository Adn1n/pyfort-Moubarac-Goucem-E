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
    enigne_choisie = random.choice(liste_enigmes)
    for i in enigne_choisie:
        print(enigne_choisie[i])

    print(enigne_choisie)

enigme_pere_fouras()

