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

def composer_equipe() :
    l = []
    valide = False


    print("Bienvenue dans la composition de ton équipe !")
    time.sleep(2)

    print("Combien de joueurs veux-tu inscrire dans ton équipe ? ")
    nb_de_joueur = int(input())

    while valide == False :

        if nb_de_joueur > 3 or nb_de_joueur <= 0:
            print("Veuillez saisir un nombre de joueurs entre 1 et 3. ")
            nb_de_joueur = int(input())
        else :
            valide = True

    print("Parfait ! {} joueur(s) ont été inscrits dans ton équipe.".format(nb_de_joueur))
    time.sleep(2)


    for i in range(nb_de_joueur) :
        print("Inscription du Joueur {} ".format(i+1))
        print()
        time.sleep(2)

        nom = input("Entrez le nom du joueur : ")
        profesion = input("Entrez le profession du joueur : ")

        leader_valide = False
        while leader_valide == False :
            print(" Ce joueur est-il le leader ? ")
            leader = input()
            print()
            if leader in ["Non","Oui", "oui", "non","OUI","NON"] :
                leader_valide = True
            else:
                print("Votre saisie est incorrecte. ")
                print("Veuillez répondre par 'oui' ou 'non' ")
                time.sleep(1)
                print()

        est_leader = leader_valide in ["Oui", "oui","OUI"]


        joueur = { "nom" : nom, "profesion" : profesion, "leader" : est_leader, "cles_gagnees" : 0}
        l.append(joueur)

    leader_trouver = False

    for joueur in l:
        if joueur["leader"] :
            leader_trouver = True

    if not leader_trouver:
        print('Le premier candidat a étè attribuer comme leader.')
        time.sleep(2)
        l[0]['leader'] = True

    for personne in l:
        print(personne)

composer_equipe()

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

menu_epreuves()

