""""
Module : Fonctions utiles

Description :
Ce fichier contient le code pour gérer l'épreuve de la Salle du Trésor dans le jeu Fort Boyard.
Le joueur doit composer une équipe, choisir des épreuves, et obtenir des clés pour accéder à la salle du trésor.

Auteurs :
- Adnan MOUBARAC : Développement principal, Messages de bienvenue,
- Cylia GOUCEM : Développement principal, ergonomie
Date de création : 17/12/2024
"""

# Import des bibliothèques nécessaires
import random
import time

from epreuves_mathematiques import epreuve_math
from epreuves_hasard import epreuve_hasard
from epreuves_logiques import jeu_tictactoe
from enigme_pere_fouras import enigme_pere_fouras

"""
Fonction d'introduction
Rôle : Affiche un message d'accueil au joueur et explique le but du jeu.
Paramètres : Aucun
Résultat retourné : Aucun
"""
def introduction() :
    # Affichage de messages bienvenus
    print("Bienvenue dans l’univers de Fort Boyard.")
    time.sleep(2)
    print("Accomplis des épreuves pour obtenir trois clés.")
    time.sleep(2)
    print("Une fois les trois clés en main, la salle du trésor t’attend !")
    time.sleep(2)



"""
Fonction qui met la première lettre d'une chaîne en majuscule
Rôle : Met en majuscule la première lettre d'une chaîne tout en maintenant les autres lettres en minuscule.
Paramètre : la chaîne de caractères à transformer (chaine)
Résultat retourné : la chaîne avec la première lettre en majuscule (premier_lettre + reste)
"""
def premier_caractere_majuscule(chaine) :
    chaine = chaine.lower() # Transformation de la chaine avec toutes les lettres en minuscules
    premier_lettre = chaine[0] # Affectation de la premiere lettre
    if 'a' <= premier_lettre <= 'z': # Condition si la premiere lettre se trouve en 'a' et 'z'
        premier_lettre = chr(ord(premier_lettre) - 32) # Transformation de la lettre en majuscules avec le code ASCII

    reste = chaine[1:] # Reste de la chaine de caractère qui est en minuscule
    return premier_lettre + reste # Retourne la chaine de caractère avec la premiere lettre en majuscule


"""
Fonction qui met la première lettre de chaque mots dans la chaîne en majuscule
Rôle : Met en majuscule la première lettre de chaque mots de la chaîne tout en maintenant les autres lettres en minuscule.
Paramètre : la chaîne de caractères à transformer (chaine)
Résultat retourné : la chaîne avec la première lettre en majuscule de chaque mots (résultat)
"""


def lettre_majuscule(chaine):
    resultat = ""
    chaine = chaine.lower()  # Convertit la chaine en minuscule
    liste = chaine.split(' ')  # Création d'une liste avec chaques mots

    for mot in liste:  # Parcourt chaques mots de la liste
        maj = mot[0]  # Affectation de la premiére lettre de chaque
        reste = mot[1:]  # Affectation des restes des mots

        if 'a' <= maj <= 'z':
            maj = chr(ord(maj) - 32)  # Convertit la premiere lettre en majuscule

            nouveau_mot = maj + reste  # Ajout du mot

        resultat += nouveau_mot + " "  # Ajout de chaques mots

    return resultat


equipe_global = [] # Création d'une liste global vide
nb_joueur_global = 0 # Création d'une variable globale

"""
Fonction de composition d'équipe
Rôle : Permet au joueur de créer une équipe de 1 à 3 joueurs, définissant leurs noms, professions, et désignant un leader.
Paramètres : Aucun
Résultat retourné : Une liste de dictionnaires représentant les joueurs et le nombre de joueurs.
"""
def composer_equipe():
    liste_equipe = []
    valide = False
    est_leader = False
    verif_leader = False

    print("Bienvenue dans la composition de ton équipe !")
    time.sleep(2)

    print("Combien de joueurs veux-tu inscrire dans ton équipe ? ")
    # Demande au joueur de choisir le nombre de participants
    nb_de_joueur = int(input())

    # Validation du nombre de joueurs
    while valide == False:

        if nb_de_joueur > 3 or nb_de_joueur <= 0: # Si le nb de joueur est supérieur à trois ou inférieur ou égale à zéro
            print("Veuillez saisir un nombre de joueurs entre 1 et 3. ")
            nb_de_joueur = int(input())  # Demande de resaisir le nb
        else:
            valide = True  # Nb de joueur correct

    global nb_joueur_global # Affectation de la variable nb_joueur_global en tant que global
    nb_joueur_global = nb_de_joueur # Prend la valeur du nb de joueur affecter dans la fonction



    print("Parfait ! {} joueur(s) ont été inscrits dans ton équipe.".format(nb_de_joueur))
    time.sleep(2)
    # Inscription de chaque en demandant leurs noms, leurs professions, et s'il est leader
    for i in range(nb_de_joueur):
        print("Inscription du Joueur {} ".format(i + 1))
        print()
        time.sleep(1)

        nom = input("Entrez le nom du joueur : ")
        nom = nom.lower() # La variable est convertit en minuscules
        nom = lettre_majuscule(nom) #La premiere lettre devient une majuscule

        profesion = input("Entrez le profession du joueur : ")
        profesion = profesion.lower() # La variable est convertit en minuscules
        profesion = premier_caractere_majuscule(profesion) # La premiere lettre devient une majuscule

        if not verif_leader : # Vérification pour savoir s'il est bien leader
            leader_valide = False # Vérification de la saisie
            #Boucle principale pour la vérification
            while leader_valide == False:
                print("Ce joueur est-il le leader ? ")
                leader = input()
                leader = leader.lower()
                print()
                if leader in ["oui", "non"]: # La saisie de l'utilisateur doit etre soit "oui" ou "non"
                    leader_valide = True
                else:
                    print("Votre saisie est incorrecte. ")
                    print("Veuillez répondre par 'oui' ou 'non' ")
                    time.sleep(1)

            if leader == "oui": # S'il est le leader
                est_leader = True
                verif_leader = True # Afin d'avoir qu'un seul leader
        else :
            est_leader = False

        joueur = {"nom": nom, "profesion": profesion, "leader": est_leader, "cles_gagnees": 0}
        liste_equipe.append(joueur) # Ajout du dictionnaire dans la liste

    leader_trouver = False # Pour trouver s'il existe un leader

    for joueur in liste_equipe: # Parcourt les différents dictionnaires dans la liste
        if joueur["leader"] == True: # S'il il y a un leader
            leader_trouver = True # Leader a étè trouvé

    if not leader_trouver: # Si le leader n'a oas étè trouvé
        print('Le premier candidat a étè attribuer comme leader.')
        time.sleep(2)
        liste_equipe[0]['leader'] = True # Le premier candidat devient leader

    global equipe_global
    equipe_global = liste_equipe
    return liste_equipe, nb_de_joueur





"""
Fonction de sélection de joueur
Rôle : Permet de sélectionner un joueur de l'équipe pour une épreuve.
Paramètres : liste_equipe (liste des joueurs disponibles)
Résultat retourné : Le dictionnaire correspondant au joueur sélectionné.
"""
def choisir_joueur(liste_equipe) :
    i = 1 # Pour l'affichage des numéros des joueurs
    print("-"*55)
    # Affichage des joueurs disponibles
    for joueur in liste_equipe:

        a = joueur['nom']
        b = joueur['profesion']
        if joueur['leader'] == True : # S'il est le leader
            c = "Leader"
        else :
            c = "Membre"

        print("{}.  {}   ( {} )   -    {} ".format(i  ,a, b, c,  ))
        i += 1 # Incrémentation du compteur
    print("-" * 55)

    # Saisie du choix du joueur
    joueur_choisie =  int(input("Entrez le numéro du joueur:"))
    #Boucle permettant de choisir un joueur entre 1 et le nombre de joueurs disponible
    while joueur_choisie < 1 or joueur_choisie > nb_joueur_global :
        print()
        print("Saisie Incorrect")
        joueur_choisie = int(input(" Veuillez saisir un joueur disponible : "))
        print()

    if joueur_choisie == 1 :
        return equipe_global[0]
    elif joueur_choisie == 2 :
        return equipe_global[1]
    elif joueur_choisie == 3 :
        return equipe_global[2]



"""
Fonction de menu des épreuves
Rôle : Affiche un menu permettant de choisir une épreuve parmi celles disponibles.
Paramètres : Aucun
Résultat retourné : Aucun
"""
def menu_epreuves() :
    # Affichage des choix d'épreuves
    print()
    print('Menu')
    print()
    print("1. Épreuve de Mathématiques ")
    print("2. Épreuve de Logique ")
    print("3. Épreuve du hasard ")
    print("4. Énigme du Père Fouras")
    print()

    # Saisie et validation du choix
    choix = int(input("Choix : "))
    while choix < 1 or choix > 4 :
        choix = int(input("Saisissez un choix entre 1 et 4: "))

    # Exécution de l'épreuve correspondante
    if choix == 1 :
        epreuve_math()
    elif choix == 2 :
        jeu_tictactoe()
    elif choix == 3 :
        epreuve_hasard()
    else :
        enigme_pere_fouras()



