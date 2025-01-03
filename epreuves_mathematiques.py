"""
Épreuves Mathématiques - Fort Boyard

Description :
Ce fichier contient l'ensemble des fonctions nécessaires pour gérer les épreuves mathématiques
du jeu "Fort Boyard". Les épreuves proposées incluent :

1. Calcul de la factorielle.
2. Résolution d'équations linéaires.
3. Recherche de nombres premiers.
4. Calculs sur une liste de nombres (roulette mathématique).

Une fonction principale permet de sélectionner et lancer une épreuve au hasard.

Auteurs :
- Adnan MOUBARAC : Développement des épreuves roulette mathématique et math équations.
- Cylia GOUCEM : Développemetn des épreuves factorielles et nombre premier

Date de création : 05/12/2024
"""



# Import des bibliothèques nécessaires
import random
import time


"""
Role : # Calcul la factorielle d'un nombre
Paramètre : n (int) : Le nombre dont on veut calculer la factorielle.
Résultat retourné : La factorielle de n.
"""
def factorielle(nombre) :
    resultat_factorielle = 1 # # Initialisation à un car la factorielle est un produit.
    for i in range(1, nombre + 1):
        resultat_factorielle *= i # Multiplie x par i à chaque itération.
    return resultat_factorielle # Renvoie la factorielle

"""
Role : Propose à l'utilisateur de calculer la factorielle d'un nombre choisi aléatoirement
Paramètre : Aucun
Résultat retourné : Retourne True si la réponse de l'utilisateur est correcte.
                    Retourne False si la réponse est incorrecte.
"""
def epreuve_math_factorielle() :
    print("Es-tu prêt à multiplier les défis ? Voici la factorielle !")
    time.sleep(3)
    x = random.randint(1,10) # Choisit aléatoirement une variable x entre 1 et 10
    print(" Épreuve de Mathématiques: Calculer la factorielle de ",x)
    time.sleep(2)

    reponse_donnee  = int(input(" Votre réponse : ")) # Récupération de la réponse de l'utilisateur

    reponse_correcte = factorielle(x) # Calcul de la réponse correcte gràce à notre fonction factorielle


    if reponse_correcte == reponse_donnee: # Comparaison de la réponse
        print()
        print("Correct! Vous gagnez une clé")
        return True # La réponse à étè trouvé
    else :
        print()
        print("Désolé la réponse correcte était {}.".format(reponse_correcte))
        return False  # La réponse n'a pas étè trouvé



"""
Fonction pour vérifier si un nombre est premier
Role : Déterminer si un nombre donné est un nombre premier.
Paramètre : n (int) : Le nombre à vérifier.
Résultat retourné : Retourne True si n est un nombre premier.
                    Retourne False si n n'est pas un nombre premier.
"""
def est_premier(n):
    if n <= 1 :
        return False # Les nombres inférieurs ou égale à un ne sont pas premiers.
    for i in range(2,int(n**0.5) + 1 ) : # Boucle de deux jusqu'à la racine de n.
        if n % i == 0 : # Si est divisible par i.
            return False # n'est divisible par i, donc ce n'est pas un nombre premier
    return True  # Si aucune division n'est trouvée, n est premier


"""
Fonction qui permet de trouver le nombre premier le plus proche
Role : Trouver le plus proche nombre premier supérieur ou égal à un nombre donné.
Paramètre : n (int), le nombre à partir duquel on commence à vérifier.
Résultat retourné : Retourne le nombre premier le plus proche (n).
"""
def premier_plus_proche(n):
    while not est_premier(n):  # Boucle tant que n n'est pas un nombre premier.
        n += 1 # Incrémente n jusqu'à trouver un nombre premier.
    return n # Renvoie le nombre premier trouvé.



"""
Fonction pour l'épreuve des nombres premiers
Role : Propose au joueur de trouver le nombre premier le plus proche d'un nombre aléatoire généré.
Paramètre : Aucun
Résultat retourné : Renvoi TRUE si le joueur a donné la bonne réponse,
                    Renvoi False si la réponse est incorrecte
"""
def epreuve_math_premier() :
    print("Les nombres premiers t’attendent. Sauras-tu relever ce défi ?!")
    time.sleep(3)
    n = random.randint(10,20)
    print("Épreuve de Mathématiques: Trouver le nombre premier le plus proche de " + str(n) +".")
    time.sleep(2)
    x = int(input("Votre réponse : ")) # Demande au joueur de donner une réponse
    if x == premier_plus_proche(n) : # Vérifie si la réponse est correcte
        print()
        print("Correct! Vous gagnez une clé.")
        return True # Réussite de l'épreuve
    else :
        print()
        print("Désolé la réponse correcte était {}.".format(premier_plus_proche(n)))
        return False # Échec de l'épreuve




"""
Fonction pour l'épreuve de la roulette mathématique
Role : Demande au joueur de calculer le résultat d'une opération (addition, soustraction, multiplication) appliquée à une liste de nombres aléatoires.
Paramètre : Aucun
Résultat retourné : Renvoie True si la réponse du joueur est correcte,
                    Renvoie False si la réponse est incorrecte.
"""
def epreuve_roulette_mathematique() :
    print("La roulette des nombres est en marche. Prépare-toi à être surpris !")
    time.sleep(3)

    l = [] # Liste pour stocker les nombres aléatoires
    variable_1 = 0 # Variable pour le résultat des additions ou soustractions
    variable_2 = 1 # Variable pour le résultat des multiplications

    for i in range(6):
        x = random.randint(1, 20) # Génère un nombre aléatoire entre 10 et 20
        l.append(x)

    print("Nombres sur la roulette :", l)

    y = random.choice(["+", "-", "*"]) # Choisit une opération mathématique au hasard

    # Effectue le calcul correspondant
    if y == "+":
        for i in range(6):
            variable_1 += l[i] # Additionne tous les nombres de la liste
        print("Calculez le résultat en combinant ces nombres avec une addition.")
        time.sleep(2)
    elif y == "-":
        variable_1 = l[0] # Initialise avec le premier élément
        for i in range(1, 6):
            variable_1 -= l[i] # Soustrait les autres nombres
        print("Calculez le résultat en combinant ces nombres avec une soustraction.")
        time.sleep(2)
    else:
        for i in range(6):
            variable_2 *= l[i] # Multiplie tous les nombres
        print("Calculez le résultat en combinant ces nombres avec une multiplication.")
        time.sleep(2)

    reponse_utilisateur = int(input("Votre réponse : ")) # Demande la réponse au joueur

    # Vérifie si la réponse est correcte
    if reponse_utilisateur == variable_1 or reponse_utilisateur == variable_2:
        print()
        print("Bonne réponse! Vous avez gagné une clé.")
        return True
    else:
        if y == "+" or y == "-":
            print()
            print("Désolé la bonne réponse était {}.".format(variable_1))
        else:
            print()
            print("Désolé la bonne réponse était {}.".format(variable_2))
        return False



"""
Fonction pour résoudre une équation linéaire
Role : Génère une équation linéaire de la forme ax + b = 0, et calcule sa solution.
Paramètre : Aucun
Résultat retourné : Renvoie un tuple (a, b, solution), où a et b sont les coefficients générés
et solution est la solution de l'équation arrondie au centième.
"""
def resoudre_equation_lineaire() :

    a = random.randint(1,10) # Coefficient de x (évite 0 pour ne pas diviser par 0)
    b = random.randint(0,10)  # Constante
    solution = round(-b/a,2) # Calcule la solution arrondie au centième
    return a,b,solution  # Renvoie les paramètres de l'équation et la solution



"""
Fonction pour l'épreuve de résolution d'équation
Role : Demande au joueur de résoudre une équation linéaire de la forme ax + b = 0.
Paramètre : Aucun
Résultat retourné : Renvoie True si le joueur a donné la bonne solution.
                    Renvoie False si la réponse est incorrecte.
"""
def epreuve_math_equation() :
    print("Les mystères des équations t’appellent. Vas-tu les déchiffrer ?")
    time.sleep(3)

    a,b,solution = resoudre_equation_lineaire() # Génère une équation

    print("Épreuve de Mathématiques: Résoudre l'équation {}x + {} = 0".format(a,b))
    time.sleep(2)
    reponse = int(input(" Quelle est la valeur de x au centième prés : "))

    if reponse == solution :
        print()# Vérifie si la réponse est correcte
        print("Correct! Vous gagnez une clé.")
        return True
    else :
        print()
        print("Désolé la réponse correcte était {}".format(solution))
        return False


"""
Fonction qui permet d'afficher une introduction pour l'épreuve de mathématiques
Role : Affichage introduction.
Paramètre : Aucun
Résultat retourné : Aucun (Affichage)
"""
def message_intro_math () :
    print("Prêt pour un challenge mathématique ? L’aventure commence maintenant !")
    time.sleep(5)
    print(
        "L’heure du défi a sonné ! Une des épreuves suivantes te sera attribuée au hasard : factorielle, nombres premiers, roulette mathématique ou équations.")
    time.sleep(5)
    print()
    print("Roulement de tambour… Découvrons ensemble quel défi te sera attribué !")
    time.sleep(3)
    print()

"""
Fonction principale pour choisir une épreuve mathématique au hasard
Role : Permet de lancer une épreuve au hasard
Paramètre : Aucun
Résultat retourné : Renvoie les résultats de l'épreuve choisie
"""
def epreuve_math() :

    print("Prêt pour un challenge mathématique ? L’aventure commence maintenant !")
    time.sleep(5)
    print("L’heure du défi a sonné ! Une des épreuves suivantes te sera attribuée au hasard : factorielle, nombres premiers, roulette mathématique ou équations.")
    time.sleep(3)
    print()
    print("Roulement de tambour… Découvrons ensemble quel défi te sera attribué !")
    time.sleep(3)
    print()


    # Liste des épreuves disponibles.
    epreuves = [epreuve_math_factorielle, epreuve_math_premier, epreuve_roulette_mathematique, epreuve_math_equation]
    epreuve_choisie = random.choice(epreuves)()  # Choisit une épreuve au hasard et l'exécute

    if epreuve_choisie :  # Si l'épreuve est réussie
        return True
    else :
        return False




