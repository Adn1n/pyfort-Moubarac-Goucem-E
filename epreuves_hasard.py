# Import des bibliothèques nécessaires
import random
import time

# Message de bienvenue et présentant les règles.
#Role : Affiche un message d'accueil et les règles du jeu du bonneteau.
# Paramètre : Aucun
# Résultat retourné : Aucun (Affichage)
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

# Fonction principal de l'épreuve de bonneteau
# Role : Simule le jeu du bonneteau où le joueur doit deviner sous quel bonneteau se trouve la clé.
# Paramètre : Aucun
# Résultat retourné : True si le joueur trouve la clé, False sinon

def bonneteau() :
    liste = ['A','B','C'] # Liste des bonneteaux disponibles
    liste_valeur_possible = ['A', 'B', 'C', 'a', 'b', 'c']# Inclut des lettres minuscules pour gérer les entrées insensibles à la casse
    message_bienvenue()
    print("Choisissez entre l'un des trois bonneteau disponible : " + " ".join(liste))
    essaie = 1  # Compteur d'essais
    reponse = False # Variable qui permet de suivre les résultats du joueur

    # Boucle principale
    while essaie <= 2 and reponse == False: # Le joueur a deux essais maximum

        x = random.choice(liste) # La clé est placée aléatoirement

        choix_joueur = input("Choisissez un bonneteau : ")
        print()
        # Vérification de l'entrée du joueur
        while choix_joueur not in liste_valeur_possible:
            print("Choix invalide. Veuillez choisir parmi A, B ou C.")
            choix_joueur = input()
            print()

        # Convertit les minuscules en majuscules
        if choix_joueur in ['a', 'b', 'c']:

            if choix_joueur == 'a':
                choix_joueur = 'A'

            elif choix_joueur == 'b':
                choix_joueur = 'B'
            else:
                choix_joueur = 'C'

        # Vérification si le joueur a trouvé la clé
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


            print("Il vous reste encore {} essaie".format(3 - essaie))
            print()
            time.sleep(4)

    # Résultat final
    if reponse == False:
        print("Vous avez perdu. La clé était sous le bonneteau : ", x)
        print()
        return False
    else :
        return True



# Fonction affichant les règles du jeu du lancer de dés
# Role : Présente le contexte et les règles du jeu de lancer de dés.
# Paramètre : Aucun
# Résultat retourné : Aucun (Affichage)
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

#Fonction permettant de simuler un lancer de dés
# Role : Attend que l'utilisateur appuie sur Entrée pour simuler un lancer de dés.
# Paramètre : Aucun
# Résultat retourné : Aucun

def lance_de():
    print("Appuyez sur la touche 'Entrée' pour lancer vos dés.")
    input()


# Fonction principale pour le jeu du lancer de dés
# Role : Simule une partie où le joueur et le maître du jeu s'affrontent avec des lancers de dés.
# Paramètre : Aucun
# Résultat retourné : True si le joueur obtient un 6 en premier,
#                     False si le maître du jeu gagne ou si c'est un match nul.
def jeu_lance_des() :

    message()
    de = [1, 2, 3, 4, 5, 6] # Liste contenant les faces disponibles

    match = False  # Indique si un joueur a obtenu un 6
    essaie = 1 # Compteur d'essais

    # Boucle principale
    while essaie <= 3 and match == False: # Chaque joueur possède 3 essais
        tpl_1 = () # Lancers du joueur
        tpl_2 = () # Lancers du maître du jeu
        print("Il vous reste encore {} essaie.".format(4 - essaie))
        lance_de() # Fonction d'affichage pour le joueur
        # Lancer des dés pour le joueur
        de_joueur1 = random.choice(de)
        de_joueur2 = random.choice(de)
        tpl_1 = de_joueur1, de_joueur2

        print("Vous avez lancé les dés : {} et {}.".format(de_joueur1, de_joueur2))
        print()
        time.sleep(3)

        # Vérification si le joueur a obtenu un 6
        if 6 in tpl_1: # Regarde s'il y a un 6 dans le tuple du joueur
            match = True # La partie est terminé
            print("Félicitations ! Vous avez remporté la partie, la clé est à vous !")
            print()
            time.sleep(2)
            return True # Le joueur a remporté la partie
        else:
            print("Le jeu n’est pas terminé ! Laissez-vous une autre chance !")
            print()
            time.sleep(2)

            print("C'est maintenant au tour du maître du jeu de lancer les dés...")
            print()
            time.sleep(4)
            # Lancer des dés pour le maître du jeu
            de_maitre1 = random.choice(de)
            de_maitre2 = random.choice(de)
            tpl_2 = (de_maitre1, de_maitre2)

            print("Le maître du jeu a lancé les dés : {} et {}.".format(de_maitre1, de_maitre2))
            print()
            print()
            time.sleep(3)

            # Vérification si le maître du jeu a obtenu un 6
            if 6 in tpl_2:
                match = True # La partie est terminé
                print("Le maître du jeu a remporté la partie, la clé est à lui !")
                time.sleep(2)
                return False # Le joueur a perdu la perdu

        essaie += 1 # Incrémentation du compteur d'essais

    # Si la partie est un match donc ce massage s'affiche
    if match == False:
        print("Aucun joueur n'a obtenu un 6 après trois essais...")
        print()
        time.sleep(2)
        print("C'est un match nul ! Aucun gagnant cette fois.")
        time.sleep(2)
        print("La partie est terminée, merci d'avoir joué !")
        time.sleep(2)
        return False

# Message de bienvenue dans les épreuvres hasards
# Role : Affiche un message d'introduction aux épreuves
# Paramètre : Aucun
# Résultat retourné : Aucun (Affichage)
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


# Épreuve du hasard
# Role : Choisit aléatoirement entre le jeu du bonneteau ou le lancer de dés et lance l'épreuve choisie.
# Paramètre : Aucun
# Résultat retourné : True si le joueur réussit l'épreuve choisie,
#                     False sinon

def epreuve_hasard() :

    print()

    message_debut ()
    epreuves = [bonneteau,jeu_lance_des]  # Liste des épreuves possibles
    epreuves_choisie = random.choice(epreuves)() # Choix aléatoire de l'épreuve

    # Permet de savoir si le joueur a remporté l'épreuve ou pas
    if epreuves_choisie == True :
        return True
    else :
        return False



