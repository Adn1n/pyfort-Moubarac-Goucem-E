import random
import time
import json

def premier_caractere_majuscule(chaine) :
    chaine = chaine.lower() # Transformation de la chaine avec toutes les lettres en minuscules
    premier_lettre = chaine[0] # Affectation de la premiere lettre
    if 'a' <= premier_lettre <= 'z': # Condition si la premiere lettre se trouve en 'a' et 'z'
        premier_lettre = chr(ord(premier_lettre) - 32) # Transformation de la lettre en majuscules avec le code ASCII

    reste = chaine[1:] # Reste de la chaine de caractère qui est en minuscule
    return premier_lettre + reste # Retourne la chaine de caractère avec la premiere lettre en majuscule


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
    print("Bienvenue dans l'{} !".format(emission))
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
    indices_restantes = indices[2:] # Affectation des indices restants dans le set

    nb_indice = 1
    print()
    for indice in trois_premier_indices : # Boucle pour afficher en sautant des lignes les indices
        print("Indice {} : {}".format(nb_indice, indice))
        time.sleep(2)
        nb_indice += 1

    essaie = 4
    reponse_correcte = False



    while reponse_correcte == False and essaie > 0:
        saisie_utilisateur = input("Entrez la solution qui déverrouillera la Salle du Trésor : ")
        saisie_utilisateur = saisie_utilisateur.lower()

        if saisie_utilisateur == reponse_correcte:
            reponse_correcte = True
        else:
            essaie -= 1
            if essaie > 0:
                print("Il vous reste encore {} essaie(s)".format(essaie))
                print()
                print("Voici un indice supplémentaire ")
                del indices_restantes[0]
                print("Indice {} : {}".format(nb_indice, indices_restantes[0]))
                nb_indice += 1
            else :
                print("Vous ne disposez plus d'essaie.")
                time.sleep(1)
                print()
                print("La réponse était {} ".format(reponse_afficher_utilisateur))


    if reponse_correcte == True:
        print()
        print("Vous avez gagné !")
        return True
    else :
        print("Vous avez perdu")
        return False





salle_De_Tresor()