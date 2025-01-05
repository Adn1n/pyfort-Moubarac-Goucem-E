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
import time
import datetime as dt
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
    if not chaine:  # Vérifie si la chaîne est vide
        return ""  # Retourne une chaîne vide
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


def lettre_majuscule(chaine) :
    resultat = ""
    chaine = chaine.lower()  # Convertit la chaine en minuscule
    liste = chaine.split(' ')  # Création d'une liste avec chaques mots

    for mot in liste:  # Parcourt chaques mots de la liste
        if mot : # Si le mot existe
            maj = mot[0]  # Affectation de la premiére lettre de chaque
            reste = mot[1:]  # Affectation des restes des mots

            if 'a' <= maj <= 'z':
                maj = chr(ord(maj) - 32)  # Convertit la premiere lettre en majuscule

                nouveau_mot = maj + reste  # Ajout du mot

            resultat += nouveau_mot + " "  # Ajout de chaques mots

    return resultat



"""
Fonction de composition d'équipe
Rôle : Permet au joueur de créer une équipe de 1 à 3 joueurs, définissant leurs noms, professions, et désignant un leader.
Paramètres : Aucun
Résultat retourné : Une liste de dictionnaires représentant les joueurs et le nombre de joueurs.
"""
def composer_equipe() :
    liste_equipe = []
    valide = False
    est_leader = False
    verif_leader = False

    print("Commençons par la composition de ton équipe !")
    time.sleep(2)

    print("Combien de joueurs veux-tu inscrire dans ton équipe ? ")
    # Demande au joueur de choisir le nombre de participants
    nb_de_joueur = int(input())

    # Validation du nombre de joueurs
    while not valide :

        if nb_de_joueur > 3 or nb_de_joueur <= 0: # Si le nb de joueur est supérieur à trois ou inférieur ou égale à zéro
            print("Veuillez saisir un nombre de joueurs entre 1 et 3. ")
            nb_de_joueur = int(input())  # Demande de resaisir le nb
        else:
            valide = True  # Nb de joueur correct




    print("Parfait ! {} joueur(s) ont été inscrits dans ton équipe.".format(nb_de_joueur))
    time.sleep(2)

    # Inscription de chaque en demandant leurs noms, leurs professions, et s'il est leader
    for i in range(nb_de_joueur):
        print()
        print("Inscription du Joueur {} ".format(i + 1))

        time.sleep(1)

        nom = input("Entrez le nom du joueur : ").lower() # La variable est convertit en minuscules
        nom = lettre_majuscule(nom) #La premiere lettre devient une majuscule

        profesion = input("Entrez le profession du joueur : ").lower() # La variable est convertit en minuscules
        profesion = premier_caractere_majuscule(profesion) # La premiere lettre devient une majuscule

        if not verif_leader : # Vérification pour savoir s'il est bien leader
            leader_valide = False # Vérification de la saisie
            #Boucle principale pour la vérification
            while not leader_valide :
                leader = input("Ce joueur est-il le leader ? ")
                leader = leader.lower()
                print()
                if leader in ["oui", "non"]: # La saisie de l'utilisateur doit etre soit "oui" ou "non"
                    leader_valide = True
                else:
                    print("Réponse incorrecte. Veuillez répondre par 'oui' ou 'non'.")
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
        if joueur["leader"] : # S'il il y a un leader
            leader_trouver = True # Leader a étè trouvé

    if not leader_trouver: # Si le leader n'a oas étè trouvé
        print("Aucun leader n'a été choisi. Le premier joueur sera attribué comme leader.")
        time.sleep(2)
        liste_equipe[0]['leader'] = True # Le premier candidat devient leader

    print("Équipe composée avec succès !")
    time.sleep(2)
    return liste_equipe




"""
Fonction de sélection de joueur
Rôle : Permet de sélectionner un joueur de l'équipe pour une épreuve.
Paramètres : liste_equipe (liste des joueurs disponibles)
Résultat retourné : Le dictionnaire correspondant au joueur sélectionné.
"""
def choisir_joueur(liste_equipe) :

    print("Choisissez un joueur pour participer à l'épreuve :")
    print()
    i = 1 # Pour l'affichage des numéros des joueurs
    print("-"*55)
    # Affichage des joueurs disponibles
    for joueur in liste_equipe:

        nom = joueur['nom']
        profession = joueur['profesion']
        if joueur['leader'] :  # S'il est le leader
            statut = "Leader"
        else :
            statut = "Membre"

        print("{}.  {}   ( {} )   -    {} ".format(i  ,nom, profession, statut,  ))
        i += 1 # Incrémentation du compteur
    print("-" * 55)

    # Saisie du choix du joueur
    joueur_choisie =  int(input("Entrez le numéro du joueur : "))
    #Boucle permettant de choisir un joueur entre 1 et le nombre de joueurs disponible
    while joueur_choisie < 1 or joueur_choisie > len(liste_equipe) :
        print()
        print("Saisie incorrecte. Veuillez choisir un joueur valide.")
        joueur_choisie = int(input("Entrez le numéro du joueur : "))
        print()


    if joueur_choisie == 1 :
        return liste_equipe[0]
    elif joueur_choisie == 2 :
        return liste_equipe[1]
    elif joueur_choisie == 3 :
        return liste_equipe[2]





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
    print()
    while choix < 1 or choix > 4 :
        choix = int(input("Saisissez un choix entre 1 et 4 : "))
        print()

    return choix


"""
Fonction : Formate l'heure de maniére "YYYY-MM-DD HH:MM:SS"
Rôle : Récupère l'horodatage actuel sous le format "YYYY-MM-DD HH:MM:SS".
Paramètres : Aucun
Résultat retourné : 
- Une chaîne de caractères contenant la date et l'heure actuelles formatées.
"""
def heure():
    heure_fonction = dt.datetime.today() # Récupérer l'heure actuelle
    x = str(heure_fonction) # Convertir l'objet datetime en chaîne de caractères

    date_heure = [] # Liste pour stocker les parties de la date et de l'heure

    # Séparer la date et l'heure
    list_date_heure = x.split(" ")
    date_exacte = list_date_heure[0] # Obtenir la partie date

    # Séparer l'heure exacte et les fractions de secondes
    heure = list_date_heure[1].split(".")
    heure_exacte = heure[0]

    # Formatage de la date et de l'heure pour l'horodatage
    horodage ="{} {}".format(date_exacte, heure_exacte)

    return horodage


"""
Fonction : Écrit une ligne contenant les informations dans le fichier d'historique.
Rôle : Enregistre les informations sur une partie dans un fichier d'historique.
Paramètres : 
- joueur (str) : Nom du joueur.
- epreuve (str) : Nom de l'épreuve réalisée.
- resultat (str) : Résultat de l'épreuve ("Gagné", "Perdu", etc.).
- cles (int) : Nombre de clés obtenues.
Résultat retourné : Aucun

"""
def ajouter_historique(joueur, epreuve, resultat, cles):
    with open("data/output/historique.txt", "a") as f : # Ouverture du fichier en mode append
        heure_jeu = heure() # Récupérer l'horodatage actuel

        # Créer une entrée formatée pour l'historique
        entree = "Date : {} |Joueur : {} |Épreuve : {} |Résultat : {} |Clés : {}\n".format(heure_jeu,joueur,epreuve,resultat,cles)
        f.write(entree) # Écrire l'entrée dans le fichier


"""
Fonction : Affiche chaque entrée, séparant les informations par "|".
Rôle : Affiche les entrées du fichier d'historique ligne par ligne.
Paramètres : Aucun
Résultat retourné : Aucun
"""
def affichage_historique():

    with open("data/output/historique.txt", "r") as f : # Ouverture du fichier en mode read
        contenu = f.readlines() # Lire toutes les lignes du fichier

        for ligne in contenu: # Parcourir chaque ligne pour extraire les informations
            liste_ligne = ligne.split("|") # Diviser chaque ligne par le séparateur "|"
            for info in liste_ligne: # Afficher chaque information séparément
                print(info)
            time.sleep(1)




