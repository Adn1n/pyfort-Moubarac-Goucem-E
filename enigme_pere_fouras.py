"""
Module : Énigmes du Père Fouras - Fort Boyard

Description :
Ce module gère l'épreuve des énigmes du Père Fouras pour le jeu Fort Boyard.

Auteurs :
- Adnan MOUBARAC : Développement principal, l'ergonomie.
- Cylia GOUCEM : Développement principal, l'ergonomie.

Date de création : 17/12/2024
"""


# Import des bibliothèques nécessaires
import json
import random
import time


"""
Fonction qui introduit l'épreuve
Role : Affiche un texte d'introduction et les règles pour l'épreuve des énigmes du Père Fouras.
Paramètre : Aucun
Résultat retourné : Aucun (Affichage)
"""
def intro () :
    print("Bienvenue dans l'antre du Père Fouras !")
    time.sleep(2)
    print("Attention, vous n’avez que 3 essais. Bonne chance !")
    time.sleep(2)
    print()

"""
Chargement des fichiers JSON :
Role : Charge et retourne les énigmes depuis un fichier JSON contenant les données des énigmes.
Paramètre : Aucun
Résultat retourné : Liste des énigmes sous forme de dictionnaires.
"""
def charger_enigmes() :
    with open ("data/enigmesPF.json", "r",encoding= 'utf-8') as f :
        donnees = json.load(f)
    return donnees

"""
Fonction principale pour lancer l'énigme du Père Fouras.
Role : Simule une épreuve d'énigmes où le joueur à trois essais pour trouver la bonne réponse.
Paramètre : Aucun
Résultat retourné : True si le joueur trouve la bonne réponse à l'énigme.
                    False si le joueur échoue après avoir épuisé ses trois essais.
"""
def enigme_pere_fouras() :

    essai = 1 # Initialisation compteur essaie
    essai_restant = 3 # Initialisation compteur essaie-restant
    resultat = False # Indicateur pour savoir si le joueur a gagné
    intro() # Fonction intro qui introduit l'épreuve


    # Boucle principale le joueur dispose de 3 essais
    while essai <= 3 and resultat == False :

        # Chargement des listes d'énigme et en choisir une aléatoirement
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
            time.sleep(2) # Affiche chaque phrase avec un intervalle de deux secondes
        print("-" * 45)
        time.sleep(2)
        print()

        # Réponse de l'utilisateur
        reponse = input("Réponse    : ")
        reponse = reponse.lower() # Affectation de la réponse en minuscule afin de la mieux comparer


        # Vérification de la réponse du joueur
        if reponse == reel_reponse:
            print()
            print("Excellente déduction, aventurier ! Vous gagnez une clé.")
            time.sleep(2)
            resultat = True # Indique que le joueur a trouvé la bonne réponse
            return True

        else :
            essai_restant -= 1 # Réduit le nombre d'essais restants
            if essai_restant >= 1 : # Vérifie si le joueur possède encore des essais

                print("Reprenez vos esprits et tentez de nouveau !")
                print()
                time.sleep(2)
                print('La réponse était {}. '.format(enigme_choisie["reponse"]))
                time.sleep(2)
                print("Courage, il vous reste encore {} essai(s)".format(essai_restant))
                print()
                time.sleep(3)
                essai += 1 # Met à jour le compteur
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




