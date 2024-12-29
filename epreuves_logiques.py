"""
Module : Jeu du Morpion - Tic-Tac-Toe

Description :
Ce module implémente le jeu classique du Morpion où un joueur affronte le Maitre du jeu.

Auteurs :
- Adnan MOUBARAC : Développement principal
- Cylia GOUCEM: Développement principal

Date de création : 29/12/2024
"""

# Import des bibliothèques nécessaires
import random
import time

"""
Fonction qui affiche la grille de jeu.

Rôle : Afficher la grille actuelle du jeu avec des séparateurs pour les lignes et les colonnes.
Paramètre : 
- grille : La liste 2D représentant l'état actuel de la grille (3x3)
Résultat retourné : Aucun (affichage).
"""
def afficher_grille(grille) :
    # Parcours de chaque ligne de la grille
    for i in range(3):
        lignes = " "
        # Construction de chaque ligne avec séparateurs
        for j in range(3):
            lignes += str(grille[i][j])
            if j < 2 : # Ajout de séparateurs verticaux entre les colonnes
                lignes += " | "
        print(lignes)
        if i < 2 : # Ajout de séparateurs horizontaux entre les lignes
            print("-"*10)


"""
Fonction qui vérifie si un joueur a gagné.

Rôle : Détecter si un joueur a aligné trois symboles identiques horizontalement, verticalement ou en diagonale.
Paramètres :
- grille : La liste 2D représentant l'état actuel de la grille (3x3).
- symbole : Le symbole du joueur à vérifier ('X' ou 'O').
Résultat retourné : 
- True si le joueur a gagné.
- False sinon.
"""
def verifier_victoire(grille, symbole) :

    # Vérification des lignes
    for i in range(3):
        if grille[i][0] == symbole and grille[i][1] == symbole and grille[i][2] == symbole :
            return True

    #Vérification des colonnes
    for j in range(3):
        if grille[0][j] == symbole and grille[1][j] == symbole and grille[2][j] == symbole :
            return True

    #Vérification des diagonales
    if grille[0][0] == symbole and grille[1][1] == symbole and grille[2][2] == symbole :
        return True

    #Vérification de l'anti-diagonales
    if grille[0][2] == symbole and grille[1][1] == symbole and grille[2][0] == symbole :
        return True

    return False


"""
Fonction qui détermine le meilleur coup pour le Maître du Jeu.

Rôle : Identifier le coup optimal pour gagner, bloquer le joueur, ou jouer aléatoirement si aucune priorité n'est trouvée.
Paramètres :
- grille : La liste 2D représentant l'état actuel de la grille (3x3).
- symbole : Le symbole du Maître du Jeu ('O').
Résultat retourné :
- Un tuple (ligne, colonne) correspondant aux coordonnées de la case choisie.
"""
def coup_maitre(grille,symbole) :

    symbole_adversaire = "X"
    # Première priorité : trouver un coup gagnant
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " " :
                grille[i][j] = symbole
                if verifier_victoire(grille,symbole):
                    grille[i][j] = " "
                    return (i,j)
                grille[i][j] = " "

    # Deuxième priorité : bloquer le joueur si nécessaire
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " " :
                grille[i][j] = symbole_adversaire
                if verifier_victoire(grille,symbole_adversaire) :
                    grille[i][j] = " "
                    return (i,j)
                grille[i][j] = " "

    case_aleatoire = []
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " " :
                case_aleatoire.append((i,j))

    # Dernière option : choisir un coup aléatoire parmi les cases libres
    case_maitre = random.choice(case_aleatoire)
    return case_maitre


"""
Fonction qui gère le tour du joueur humain.

Rôle : Permettre au joueur de saisir ses coordonnées et place son symbole sur la grille.
Paramètre :
- grille : La liste 2D représentant l'état actuel de la grille (3x3).
Résultat retourné : Aucun (modifie la grille).
"""
def tour_joueur(grille) :

    boucle_principal = False
    boucle_secondaire = False
    boucle_final = True

    while boucle_principal == False:
        # Demander au joueur de saisir ses coordonnées

        while boucle_secondaire == False:
            coordonee = input("Joueur X, c'est à vous. Où voulez-vous placer votre symbole (1,1) ? ")
            if coordonee == "1,1" or coordonee == "1,2" or coordonee == "1,3" or coordonee == "2,1" or coordonee == "2,2" or coordonee == "2,3" or coordonee == "3,1" or coordonee == "3,2" or coordonee == "3,3" :
                boucle_secondaire = True

        # Boucle ou cas s'il y a une saisie invalide
        while boucle_final == False:
            coordonee = input("Veuillez saisir une case valide : ")
            if coordonee == "1,1" or coordonee == "1,2" or coordonee == "1,3" or coordonee == "2,1" or coordonee == "2,2" or coordonee == "2,3" or coordonee == "3,1" or coordonee == "3,2" or coordonee == "3,3":
                boucle_final = True

        ligne, colonne = coordonee.split(",")

        ligne = int(ligne)
        colonne = int(colonne)

        if 1 <= ligne <= 3 and 1 <= colonne <= 3: # Vérification des limites
            ligne -= 1 # Conversion des coordonnées en indices
            colonne -= 1 # Conversion des coordonnées en indices
            if grille[ligne][colonne] == " " : # Vérifier si la case est libre
                grille[ligne][colonne] = "X" # Placer le symbole
                boucle_principal = True
            else :
                print("Oups ! Cette case est déjà occupée. Essayez une autre.")
                print()
                time.sleep(2)
                boucle_final = False


"""
Fonction qui gère le tour du Maître du Jeu (IA).

Rôle : Utiliser la fonction coup_maitre pour décider et jouer le coup du Maître du Jeu.
Paramètre :
- grille : La liste 2D représentant l'état actuel de la grille (3x3).
Résultat retourné : Aucun (modifie la grille).
"""
def tour_maitre(grille) :

    coordonne_du_maitre = coup_maitre(grille,'O') #Affectation des coordonnées dans un tuple
    ligne = coordonne_du_maitre[0] # Premier indice affecter a la ligne
    colonne = coordonne_du_maitre[1] # Deuxième indice pour la colonne

    grille[ligne][colonne] = "O" # Placement du symbole du maitre de jeu


"""
Fonction qui vérifie si la grille est pleine.

Rôle : Déterminer si toutes les cases de la grille sont occupées.
Paramètre :
- grille : La liste 2D représentant l'état actuel de la grille (3x3).
Résultat retourné :
- True si la grille est pleine.
- False sinon.
"""
def grille_complete(grille):
    cpt = 0 # Initialisation du compteur
    # Parcourt la grille
    for i in range(3):
        for j in range(3):
            if grille[i][j] != " " : # Si la case n'est pas vide
                cpt += 1 # Ajoute un au compteur

    if cpt == 9: # Si le compteur est égale à neuf donc la grille est pleine
        return True
    else:
        return False


"""
Fonction qui vérifie si la partie est terminée.

Rôle : Vérifie si un joueur a gagné ou si la grille est pleine (match nul).
Paramètre :
- grille : La liste 2D représentant l'état actuel de la grille (3x3).
Résultat retourné :
- True si la partie est terminée.
- False sinon.
"""
def verifier_resultat(grille):
    # Pour vérifier si la partie est finis
    if verifier_victoire(grille, 'X') == True or verifier_victoire(grille, 'O') == True or grille_complete(grille) == True :
        return True
    else :
        return False


"""
Fonction qui affiche un message de bienvenue.

Paramètre : Aucun
Rôle : Présenter les règles du jeu et motiver les joueurs.
Résultat retourné : Aucun (affichage).
"""
def message_de_bienvenue() :
    print("Bienvenue dans le jeu du Morpion ! ")
    time.sleep(2)
    print()
    print("Votre objectif est simple : soyez le premier à aligner trois symboles identiques ")
    time.sleep(2)
    print("Vous jouez avec les 'X' et affrontez le Maître du Jeu qui contrôle les 'O'.")
    print()
    time.sleep(2)
    print("Bonne chance et amusez-vous !")
    print()
    time.sleep(2)


"""
Fonction principale qui gère le déroulement complet de la partie.

Paramètre : Aucun
Rôle : Alterner les tours entre le joueur et le Maître du Jeu jusqu'à la fin de la partie.
Résultat retourné :
- True si le joueur gagne.
- False si le Maître du Jeu gagne ou en cas de match nul.
"""
def jeu_tictactoe() :
    # Création d'une grille vide
    grille = []

    for i in range(3):
        ligne = []
        for j in range(3):
            ligne.append(" ") # Ajout d'un espace à chaque case
        grille.append(ligne) # Ajour de la ligne dans la grille

    match = False # Permet de vérifier si la partie est terminé

    message_de_bienvenue()

    print("Pour jouer, entrez les coordonnées de votre coup sous forme ligne, colonne (ex: 1,2)")
    time.sleep(2)
    print("C'est parti ! Voici la grille initiale : ")
    print()
    afficher_grille(grille)
    time.sleep(4)

    while not match: # Boucle principale qui alterne entre joueur et maitre du jeu
        print()
        # Tour du joueur
        tour_joueur(grille)
        afficher_grille(grille)

        if verifier_victoire(grille, 'X'):
            print()
            print("Félicitations ! Vous avez gagné.")
            match = True
            return True

        if verifier_resultat(grille):
            print()
            print("Match nul ! Quelle partie serrée. Rejouons pour décider le vainqueur.")
            match = True
            return False

        # Tour du Maître du Jeu
        tour_maitre(grille)

        print()
        print("Tour de du maître du jeu (O)...")
        time.sleep(2)
        afficher_grille(grille)
        time.sleep(4)

        if verifier_victoire(grille, 'O'):
            print()
            print("Défaite ! Le Maître du Jeu a été plus malin cette fois.")
            match = True
            return False

        if verifier_resultat(grille):
            print()
            print("Match nul ! Aucune victoire cette fois-ci.")
            match = True
            return False



