# Import des bibliothèques nécessaires
import json
import random
import time

# Texte d'introduction : permet d'introduire un texte à l'utilisateur et ne renvoie rien car il affiche directement les textes
def intro () :
    print("Bienvenue dans l'antre du Père Fouras !")
    time.sleep(2)
    print("Attention, vous n’avez que 3 essais. Bonne chance !")
    time.sleep(2)
    print()
# Chargement des fichiers JSON :
def charger_enigmes() :
    with open ("data/enigmesPF.json", "r",encoding= 'utf-8') as f :
        donnees = json.load(f)
    return donnees

#Fonction principale pour lancer l'enigme de pere fouras : il renvoie Vrai ou Faux selon le résultat
def enigme_pere_fouras() :

    dico = {} # Affectation d'un set vide
    essai = 1 # Initialisation compteur essaie
    essai_restant = 3 # Initialisation compteur essaie-restant
    resultat = False #Indicateur pour savoir si le joueur il a gagné
    intro() # Fonction intro qui introduit l'épreuve


    # Boucle principal le joueur dispose de 3 essais
    while essai <= 3 and resultat == False :

        # Charegement des listes d'enigme et en choisir une aléatoirement
        liste_enigmes = charger_enigmes()
        enigme_choisie = random.choice(liste_enigmes) # Choix aléatoire d'une énigme
        reel_reponse = enigme_choisie["reponse"].lower() # Réponse correcte en minuscule afin de la vérifier avec la réponse de l'utilisateur
        question_utilisateur = enigme_choisie["question"].split("\n") # Affectation de chaque découpage entre les sauts dans une liste


        # Affichage utilisateur
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
        for phrase in question_utilisateur: # Affiche phrase par phrase avec des sauts de lignes gràce à notre découpage
            print('| {:^10} '.format(phrase))
            time.sleep(2)
        print("-" * 45)
        time.sleep(2)
        print()

        # Réponse de l'utilsateur
        reponse = input("Réponse    : ")
        reponse = reponse.lower() # Affectation de la réponse en minuscule afin de la mieux comparer


        # Vérification de la réponse du joueur
        if reponse == reel_reponse:
            print()
            print("Excellente déduction, aventurier ! Vous gagnez une clé.")
            time.sleep(2)
            resultat = True # Indique que le joueur a trouvé la bonne réponse

        else :
            essai_restant -= 1 # Réduire le nombre d'essais restants
            if essai_restant >= 1 : # Vérification si le joueur possède encore des essais

                print("Reprenez vos esprits et tentez de nouveau !")
                print()
                time.sleep(2)
                print('La réponse était {}. '.format(enigme_choisie["reponse"]))
                time.sleep(2)
                print("Courage, il vous reste {} encore essai(s)".format(essai_restant))
                print()
                time.sleep(3)
                essai += 1 # Mettre à jour le compteur
                time.sleep(2)
                print()

            else : # Si le joueur ne possède plus d'essai
                print("Réponse incorrect")
                print('La réponse était {}. '.format(enigme_choisie["reponse"])) #Affichage de la vraie réponse
                time.sleep(2)
                print()
                print("Même les plus grands esprits échouent parfois. Relevez-vous et continuez. ")
                time.sleep(2)
                print("L'épreuve est terminée. Revenez plus fort pour les prochaines énigmes.")
                print()
                time.sleep(1)
                resultat = True # Termine la boucle principale
                return False # Le joueur a échoué l'épreuve


enigme_pere_fouras()

