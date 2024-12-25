import random
import time

from epreuves_mathematiques import epreuve_math
from epreuves_hasard import epreuve_hasard
from epreuves_logiques import epreuves_logiques
from enigme_pere_fouras import enigme_pere_fouras


def introduction() :
    print("Bienvenue dans l’univers de Fort Boyard.")
    time.sleep(2)
    print("Accomplis des épreuves pour obtenir trois clés.")
    time.sleep(2)
    print("Une fois les trois clés en main, la salle du trésor t’attend !")
    time.sleep(2)

def premier_caractere_majuscule(chaine) :


    chaine = chaine.lower()
    premier_lettre = chaine[0]
    if 'a' <= premier_lettre <= 'z':
        premier_lettre = chr(ord(premier_lettre) - 32)

    reste = chaine[1:]
    return premier_lettre + reste

#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------

equipe_global = []
nb_joueur_global = 0
def composer_equipe():
    liste_equipe = []
    valide = False

    print("Bienvenue dans la composition de ton équipe !")
    time.sleep(2)

    print("Combien de joueurs veux-tu inscrire dans ton équipe ? ")
    nb_de_joueur = int(input())

    while valide == False:

        if nb_de_joueur > 3 or nb_de_joueur <= 0:
            print("Veuillez saisir un nombre de joueurs entre 1 et 3. ")
            nb_de_joueur = int(input())
        else:
            valide = True

    global nb_joueur_global
    nb_joueur_global = nb_de_joueur



    print("Parfait ! {} joueur(s) ont été inscrits dans ton équipe.".format(nb_de_joueur))
    time.sleep(2)

    for i in range(nb_de_joueur):
        print("Inscription du Joueur {} ".format(i + 1))
        print()
        time.sleep(2)

        nom = input("Entrez le nom du joueur : ")
        nom = nom.lower
        nom = premier_caractere_majuscule(nom)

        profesion = input("Entrez le profession du joueur : ")
        profesion = profesion.lower
        profesion = premier_caractere_majuscule(profesion)

        leader_valide = False
        while leader_valide == False:
            print(" Ce joueur est-il le leader ? ")
            leader = input()
            leader = leader.lower()
            print()
            if leader in ["oui", "non"]:
                leader_valide = True
            else:
                print("Votre saisie est incorrecte. ")
                print("Veuillez répondre par 'oui' ou 'non' ")
                time.sleep(1)

        if leader in ["oui"]:
            est_leader = True
        else:
            est_leader = False

        joueur = {"nom": nom, "profesion": profesion, "leader": est_leader, "cles_gagnees": 0}
        liste_equipe.append(joueur)

    leader_trouver = False

    for joueur in liste_equipe:
        if joueur["leader"] == True:
            leader_trouver = True

    if not leader_trouver:
        print('Le premier candidat a étè attribuer comme leader.')
        time.sleep(2)
        liste_equipe[0]['leader'] = True

    global equipe_global
    equipe_global = liste_equipe
    return liste_equipe, nb_de_joueur


composer_equipe()

#-----------------------------------------------------------------------------------------------------------------------

def choisir_joueur(liste_equipe) :
    i = 1
    print("-"*55)
    for joueur in liste_equipe:

        a = joueur['nom']
        b = joueur['profesion']
        if joueur['leader'] == True :
            c = "Leader"
        else :
            c = "Membre"

        print("{}.  {}   ( {} )   -    {} ".format(i  ,a, b, c,  ))
        i += 1
    print("-" * 55)

    joueur_choisie =  int(input("Entrez le numéro du joueur:"))
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

#-----------------------------------------------------------------------------------------------------------------------


def menu_epreuves() :
    print()
    print('Menu')
    print()
    print("1. Épreuve de Mathématiques ")
    print("2. Épreuve de Logique ")
    print("3. Épreuve du hasard ")
    print("4. Énigme du Père Fouras")
    print()
    choix = int(input("Choix : "))
    while choix < 1 or choix > 4 :
        choix = int(input("Saisissez un choix entre 1 et 4: "))

    if choix == 1 :
        epreuve_math()
    elif choix == 2 :
        epreuves_logiques()
    elif choix == 3 :
        epreuve_hasard()
    else :
        enigme_pere_fouras()



