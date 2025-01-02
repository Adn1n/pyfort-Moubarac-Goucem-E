"""
Module : Salle du Trésor - Fort Boyard

Description :
Ce fichier contient le code pour gérer l'épreuve de la Salle du Trésor dans le jeu Fort Boyard.
Le joueur doit découvrir un mot-code en se basant sur des indices, avec un maximum de trois essais.

Auteurs :
- Adnan MOUBARAC : Développement principal, Messages de bienvenus,
- Cylia GOUCEM : Développement principal, ergonomie
Date de création : 25/12/2024
"""


# Import des bibliothèques nécessaires
import random
import time
import json
"""
Fonction qui met la première lettre d'une chaîne en majuscule
Role : Met en majuscule la première lettre d'une chaîne tout en maintenant les autres lettres en minuscule
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
Fonction d'introduction du jeu
Role : Affiche l'introduction du jeu pour l'utilisateur
Paramètre : Aucun
Résultat retourné : Aucun (Affichage)
"""
def intro_enigmes():
    print("Bienvenue dans la Salle du Trésor !")
    time.sleep(1)
    print()
    print("Seuls les esprits brillants peuvent découvrir le mot-code.")
    time.sleep(1)
    print("Préparez-vous, aventurier, et montrez votre ingéniosité.")
    time.sleep(2)
    print()
    print("Le Fort vous met à l’épreuve. Bonne chance !")
    time.sleep(2)
    print()


"""
Fonction principale pour la Salle du Trésor
Role : Simule une épreuve où le joueur à trois essais pour trouver la bonne réponse.
Paramètre : Aucun
Résultat retourné : True si le joueur trouve la réponse, False sinon
"""
def salle_De_Tresor () :
    liste_annee = [] # Création d'une liste pour les années
    liste_emission =[] # Création d'une liste pour les émissions
    with open ("data/indicesSalle.json", "r") as f: # Ouverture du fichier
        jeu_tv = json.load(f) # Chargement des données sans jeu_tv


    intro_enigmes()

    premier_dico = jeu_tv['Fort Boyard']

    for keys in premier_dico : # Affectation de chaques années dans une liste
        liste_annee.append(keys)

    annee = random.choice(liste_annee) #Choix aléatoire de l'année

    dico_annee_choisi = premier_dico[annee] # Prend en compte les émissions de l'année choisit

    for emission in dico_annee_choisi : # Affectation de chaque émission dans une liste
        liste_emission.append(emission)

    emission = random.choice(liste_emission) # Choix aléatoire de l'émission

    # Affichage utilisateur
    print("Voici l'{} pour vous de l'année {} !".format(emission,annee))
    print()
    time.sleep(2)
    print("Voici vos premiers indices, observez bien : chaque mot est une clé pour votre succès.")
    time.sleep(3)



    dico_presente_utilisateur = dico_annee_choisi[emission] # Finalement le dictionnaire choisit pour présenter à l'utilisateur


    indices = dico_presente_utilisateur['Indices'] # Affectation des indices

    reponse = dico_presente_utilisateur['MOT-CODE'] # Affectation de la réponse réelle
    reponse = reponse.lower() # Pour vérification de la saisie du joueur

    reponse_afficher_utilisateur = premier_caractere_majuscule(reponse) # pour afficher à l'utilisateur ou cas ou s'il a faux

    trois_premier_indices = indices[:3] # Liste contenant que les trois premiers indices
    indices_restantes = {} # Set vide
    indices_restantes = indices[2:] # Affectation des indices restants dans le set,
    #                    on prend enn compte l'élèment au deuxième indice, dans notre boucle afin d'afficher
    #                    les indices un par un, on va supprimer le premier

    nb_indice = 1 # Initialisation compteur
    print()
    for indice in trois_premier_indices : # Boucle pour afficher en sautant des lignes les indices
        print("Indice {} : {}".format(nb_indice, indice))
        time.sleep(2)
        nb_indice += 1

    essaie = 4 # Initialisation
    reponse_correcte = False # Initialisation


    # Boucle principale : Tant que le joueur dispose encore des essais et qu'il n'a pas trouvé de réponse
    while reponse_correcte == False and essaie > 0:

        # Demande la réponse de l'utilisateur
        saisie_utilisateur = input("Entrez la solution qui déverrouillera la Salle du Trésor : ")
        saisie_utilisateur = saisie_utilisateur.lower() # Transformation de la réponse en minuscule afin de la comparer

        if saisie_utilisateur == reponse :
            print("Bravo ! Vous avez trouvé la bonne réponse !")
            time.sleep(2)
            reponse_correcte = True
        else:
            essaie -= 1
            if essaie > 0: # s'il reste encore des essais, donner un nouvel indice
                print("Raté ! Réfléchissez bien, il vous reste {} tentative(s)".format(essaie))
                time.sleep(2)
                print()
                print("Voici un indice supplémentaire ")
                time.sleep(2)
                del indices_restantes[0] #Supprime la premiere indice
                print("Indice {} : {}".format(nb_indice, indices_restantes[0]))
                time.sleep(1)
                nb_indice += 1
            else :
                print("Vous ne disposez plus d'essaie.")
                time.sleep(1)
                print()
                print("La réponse était {} ".format(reponse_afficher_utilisateur))
                time.sleep(2)


    if reponse_correcte == True: # Vérification de la réponse
        print()
        print("Félicitations, vous avez remporté la partie !")
        return True # Le joueur a trouvé la bonne réponse
    else :
        print("C’est perdu, mais ce n’est qu’un jeu ! ")
        return False # Le joueur n'a pas trouvé la réponse





