import json
import random
import time

def intro () :
    print("Bienvenue dans l'antre du Père Fouras !")
    time.sleep(2)
    print("Attention, vous n’avez que 3 essais. Bonne chance !")
    time.sleep(2)
    print()

def charger_enigmes() :
    with open ("data/enigmesPF.json", "r",encoding= 'utf-8') as f :
        donnees = json.load(f)
    return donnees


def enigme_pere_fouras() :
    dico = {}
    essai = 1
    essai_restant = 3
    resultat = False
    intro()
    while essai <= 3 and resultat == False :

        liste_enigmes = charger_enigmes()
        enigme_choisie = random.choice(liste_enigmes)
        reel_reponse = enigme_choisie["reponse"].lower()
        question_utilisateur = enigme_choisie["question"].split("\n")



        print("Émission   : {}".format(enigme_choisie["emission"]))
        time.sleep(1)
        print("Numero     : {}".format(enigme_choisie["numero"]))
        print("Type       : {}".format(enigme_choisie["type"]))
        time.sleep(2)
        print()
        time.sleep(1)
        print("Plongeons dans le mystère... Voici votre question !")
        time.sleep(2)
        print("-"*45)
        for phrase in question_utilisateur:
            print('| {:^10} '.format(phrase))
            time.sleep(2)
        print("-" * 45)
        time.sleep(2)
        print()

        reponse = input("Réponse    : ")
        reponse = reponse.lower()



        if reponse == reel_reponse:
            print()
            print("Excellente déduction, aventurier ! Vous gagnez une clé.")
            time.sleep(2)
            resultat = True

        else :
            essai_restant -= 1
            if essai_restant >= 1 :

                print("Reprenez vos esprits et tentez de nouveau !")
                print()
                time.sleep(2)
                print('La réponse était {}. '.format(enigme_choisie["reponse"]))
                time.sleep(2)
                print("Courage, il vous reste {} encore essai(s)".format(essai_restant))
                print()
                time.sleep(3)
                essai += 1
                time.sleep(2)
                print()
            else :
                print("Réponse incorrect")
                print('La réponse était {}. '.format(enigme_choisie["reponse"]))
                time.sleep(2)
                print()
                print("Même les plus grands esprits échouent parfois. Relevez-vous et continuez. ")
                time.sleep(2)
                print("L'épreuve est terminée. Revenez plus fort pour les prochaines énigmes.")
                print()
                time.sleep(1)
                resultat = True
                return False


enigme_pere_fouras()

