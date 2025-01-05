"""
Module : Main - Fort Boyard

Description :
Ce fichier contient le code principal pour gérer le déroulement du jeu Fort Boyard.
Les joueurs doivent constituer une équipe, participer à des épreuves variées, et collecter
un minimum de trois clés pour accéder à l'épreuve finale dans la Salle du Trésor.
Le module inclut des fonctions pour calculer le total de clés, introduire le jeu,
et orchestrer le déroulement des épreuves.

Auteurs :
- Adnan MOUBARAC : Développement principal, logique de jeu, gestion des clés.
- Cylia GOUCEM : Développement principal, gestion des clés.

Date de création : 28/12/2024
"""


import random
import time
from fonctions_utiles import *
from epreuves_mathematiques import *
from epreuves_logiques import *
from epreuves_hasard import *
from epreuve_finale import *
from enigme_pere_fouras import *


"""
Fonction : Permet de savoir le nombre de clés totals de l'équipe
Rôle : Calcule le nombre total de clés gagnées par l'équipe.
Paramètres : 
- dico (list[dict]) : Liste de dictionnaires représentant les joueurs, où chaque dictionnaire contient les clés gagnées.
Résultat retourné :
- cle (int) : Nombre total de clés gagnées par l'équipe.
"""
def nb_de_cles(dico) :
    cle_total = 0
    for joueur in dico: # Parcourt chaque joueur de l'équipe
        cle_joueur = joueur['cles_gagnees'] # Nombre de clés gagnées par le joueur
        cle_total += cle_joueur # Ajoute ce nombre au total

    return cle_total


"""
Fonction : Introduit le jeu
Rôle : Affiche un message introductif pour présenter les règles et l'objectif du jeu.
Paramètres : Aucun
Résultat retourné : Aucun
"""
def introduction() :
    print("\n" + "=" * 60)
    print("Bienvenue dans le simulateur officiel de Fort Boyard !")
    print("=" * 60)
    time.sleep(3)
    print()
    print("Dans cette aventure palpitante, vous allez constituer une équipe,")
    print("participer à des épreuves captivantes, et tenter de récolter les")
    print("trois clés nécessaires pour accéder à la légendaire salle du trésor.")
    time.sleep(7)
    print()
    print("Mais attention, chaque épreuve mettra à l'épreuve votre logique,")
    print("votre chance, vos compétences mathématiques, et votre esprit")
    print("d'équipe. Saurez-vous relever le défi ?")
    print()
    time.sleep(7)
    print("Préparez-vous... L'aventure commence maintenant !")
    print("=" * 60 + "\n")
    time.sleep(3)


"""
Fonction : Fonction principal du jeu
Rôle : Gère le déroulement principal du jeu Fort Boyard.
Paramètres : Aucun
Résultat retourné :
- True si l'équipe réussit à ouvrir la salle du trésor.
- False si l'équipe échoue à ouvrir la salle du trésor.
"""

def jeu() :

    introduction() # Affiche le message d'introduction

    liste_equipe = composer_equipe() # Composition de l'équipe
    cles = 0 # Initialisation du nombre total de clés à 0
    print()
    print("Bienvenue dans la zone des épreuves. Préparez-vous à relever des défis !")
    time.sleep(2)

    # Réinitialisation de l'historique
    with open("data/output/historique.txt", "w") as f:
        f.close()

    # Boucle principale des épreuves
    while cles < 3 : # Continue tant que l'équipe n'a pas récolté 3 clés
        print()
        time.sleep(2)

        choix_epreuve = menu_epreuves()  # Affiche le menu des épreuves et récupère le choix

        # Sélection d'un joueur de l'équipe
        joueur = choisir_joueur(liste_equipe)
        nom_joueur = joueur["nom"] # Récupération du nom du joueur
        print()
        print("Nombre actuel de clés : {}".format(cles, ))
        time.sleep(3)
        print()

        # Lancement de l'épreuve selon le choix
        if choix_epreuve == 1:
            epreuve = epreuve_math()
            nom_epreuve = "Mathématiques"


        elif choix_epreuve == 2:
            epreuve = jeu_tictactoe()
            nom_epreuve = "Morpion"

        elif choix_epreuve == 3:
            epreuve = epreuve_hasard()
            nom_epreuve = "Hasard"

        else:
            epreuve = enigme_pere_fouras()
            nom_epreuve = "Énigmes pére Fouras"

        # Mise à jour des résultats
        if epreuve : # Si l'épreuve est réussie
            joueur["cles_gagnees"] += 1 # Ajoute une clé au joueur
            resultat = "Réussi"
        else : # Si l'épreuve est échouée
            resultat = "Échoué"

        nb_de_clees = joueur["cles_gagnees"] # Mise à jour des clés gagnées par le joueur

        # Ajout de l'entrée dans l'historique
        ajouter_historique(nom_joueur, nom_epreuve, resultat, nb_de_clees)
        cles = nb_de_cles(liste_equipe) # Calcul du total de clés
        time.sleep(3)
        print()

    # Lancement de l'épreuve finale
    reussite = salle_De_Tresor()

    time.sleep(3)
    print()
    print()
    print("Voici l'historique de votre partie : ")
    print()

    # Affiche l'historique de la partie
    affichage_historique()

    # Retourne le résultat final
    if reussite :
        return True
    else :
        return False




jeu()



