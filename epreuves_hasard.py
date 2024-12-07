import random
import time




def message_bienvenue():
    print("Bienvenue dans le jeu du Bonneteau !")
    time.sleep(2)
    print("Le but du jeu est simple : une clé est cachée sous l’un des trois bonneteaux (A, B ou C).")
    time.sleep(4)
    print("Votre mission est de deviner sous quel bonneteau se trouve la clé.")
    time.sleep(4)
    print("Attention : après chaque tentative, la clé changera de place.")
    time.sleep(4)
    print("Vous n’avez que deux essais. Réfléchissez bien et bonne chance !")
    time.sleep(4)

def bonneteau() :
    liste = ['A','B','C']
    l = ['A', 'B', 'C', 'a', 'b', 'c']
    message_bienvenue()
    print("Choisissez entre l'un des trois bonneteau disponible : " + " ".join(liste))
    essaie = 1
    reponse = False
    while essaie <= 2 and reponse == False:

        x = random.choice(liste)

        choix_joueur = input("Choisissez un bonneteau : ")

        while choix_joueur not in l:
            choix_joueur = input("Choix invalide. Veuillez choisir parmi A, B ou C.")

        if choix_joueur in ['a', 'b', 'c']:

            if choix_joueur == 'a':
                choix_joueur = 'A'

            elif choix_joueur == 'b':
                choix_joueur = 'B'
            else:
                choix_joueur = 'C'

        if choix_joueur == x:
            print("Félicitations ! Vous avez trouvé la clé sous le bonneteau choisi.")
            time.sleep(4)
            reponse = True


        else:
            print("Dommage, la clé n'était pas sous ce bonneteau.")
            time.sleep(2)
            essaie += 1
            nb_essaie_restant = essaie - 1

            print("Il vous reste encore {} essaie".format(3 - essaie))
            time.sleep(4)

    if reponse == False:
        print("Vous avez perdu. La clé était sous le bonneteau : ", x)
        return False
    else :
        return True




bonneteau()
