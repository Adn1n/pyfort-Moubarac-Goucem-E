import random
import time


def message_bienvenue():
    print("Bienvenue dans le jeu du Bonneteau !")
    print()
    time.sleep(2)
    print("Le but du jeu est simple : une clé est cachée sous l’un des trois bonneteaux (A, B ou C).")
    time.sleep(4)
    print("Votre mission est de deviner sous quel bonneteau se trouve la clé.")
    print()
    time.sleep(4)
    print("Attention : après chaque tentative, la clé changera de place.")
    time.sleep(4)
    print("Vous n’avez que deux essais. Réfléchissez bien et bonne chance !")
    print()
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
        print()

        while choix_joueur not in l:
            print("Choix invalide. Veuillez choisir parmi A, B ou C.")
            choix_joueur = input()
            print()

        if choix_joueur in ['a', 'b', 'c']:

            if choix_joueur == 'a':
                choix_joueur = 'A'

            elif choix_joueur == 'b':
                choix_joueur = 'B'
            else:
                choix_joueur = 'C'

        if choix_joueur == x:
            print("Félicitations ! Vous avez trouvé la clé sous le bonneteau choisi.")
            print()
            time.sleep(4)
            reponse = True


        else:
            print("Dommage, la clé n'était pas sous ce bonneteau.")
            print()
            time.sleep(2)
            essaie += 1
            nb_essaie_restant = essaie - 1

            print("Il vous reste encore {} essaie".format(3 - essaie))
            print()
            time.sleep(4)

    if reponse == False:
        print("Vous avez perdu. La clé était sous le bonneteau : ", x)
        print()
        return False
    else :
        return True




def message ():
    print("Bienvenue dans le jeu du lancer de dés !")
    print()
    time.sleep(2)
    print("Dans ce jeu, vous affrontez le maître du jeu dans une série de lancers de dés.")
    time.sleep(3)
    print("Chaque joueur lance deux dés par tour. Le premier à obtenir un 6 sur l’un de ses dés remporte la partie.")
    print()
    time.sleep(4)
    print("Vous avez un maximum de trois essais pour tenter votre chance !")
    time.sleep(4)
    print("Si aucun joueur n'obtient un 6 après trois essais, la partie se termine sur une égalité.")
    print()
    time.sleep(3)
    print("Êtes-vous prêt à relever le défi ? Trois essais, deux dés, et un objectif : obtenir un 6. Bonne chance !")
    print()
    time.sleep(4)


def lance_de():
    print("Appuyez sur la touche 'Entrée' pour lancer vos dés.")
    input()


def jeu_lance_des() :
    message()


    de = [1, 2, 3, 4, 5, 6]

    match = False
    essaie = 1

    while essaie <= 3 and match == False:
        tpl_1 = ()
        tpl_2 = ()
        print("Il vous reste encore {} essaie.".format(4 - essaie))
        lance_de()
        de_joueur1 = random.choice(de)
        de_joueur2 = random.choice(de)
        tpl_1 = de_joueur1, de_joueur2

        print("Vous avez lancé les dés : {} et {}.".format(de_joueur1, de_joueur2))
        print()
        time.sleep(3)

        if 6 in tpl_1:
            match = True
            print("Félicitations ! Vous avez remporté la partie, la clé est à vous !")
            print()
            time.sleep(2)
            return True
        else:
            print("Le jeu n’est pas terminé ! Laissez-vous une autre chance !")
            print()
            time.sleep(2)

            print("C'est maintenant au tour du maître du jeu de lancer les dés...")
            print()
            time.sleep(4)
            de_maitre1 = random.choice(de)
            de_maitre2 = random.choice(de)
            tpl_2 = (de_maitre1, de_maitre2)

            print("Le maître du jeu a lancé les dés : {} et {}.".format(de_maitre1, de_maitre2))
            print()
            print()
            time.sleep(3)

            if 6 in tpl_2:
                match = True
                print("Le maître du jeu a remporté la partie, la clé est à lui !")
                time.sleep(2)
                return False

        essaie += 1

    if match == False:
        print("Aucun joueur n'a obtenu un 6 après trois essais...")
        print()
        time.sleep(2)
        print("C'est un match nul ! Aucun gagnant cette fois.")
        time.sleep(2)
        print("La partie est terminée, merci d'avoir joué !")
        time.sleep(2)
        return False

def message_debut ():
    print("Bienvenue dans l'arène du hasard ! ")
    time.sleep(3)
    print("Un jeu t'attend, mais lequel ? Va-t-on tester ta chance avec un lancer de dés ou avec un bonneteau ?")
    print()
    time.sleep(4)
    print("Roulement de tambour… Quel défi te sera attribué ? Lancer de dés ou Bonneteau ?")
    print()
    print()
    time.sleep(4)


def epreuve_hasard() :

    message_debut ()
    epreuves = [bonneteau,jeu_lance_des]
    x = random.choice(epreuves)()

    if x == True :
        return True
    else :
        return False

epreuve_hasard()

