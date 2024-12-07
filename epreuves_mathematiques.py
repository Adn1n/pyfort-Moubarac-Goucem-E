import random
import time

def factorielle(n) :
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x

def epreuve_math_factorielle() :
    print("Es-tu prêt à multiplier les défis ? Voici la factorielle !")
    time.sleep(3)
    x = random.randint(1,10)
    print(" Épreuve de Mathématiques: Calculer la factorielle de ",x)
    time.sleep(2)
    y = int(input(" Votre réponse : "))

    reponse_correcte = factorielle(x)
    reponse_donnee = y

    if reponse_correcte == reponse_donnee:
        print("Correct! Vous gagnez une clé")
        return True
    else :
        print("Désolé la réponse correcte était {}.".format(reponse_correcte))
        return False
    return reponse_donnee




def est_premier(n):
    if n <= 1 :
        return False
    for i in range(2,int(n**0.5) + 1 ) :
        if n % i == 0 :
            return False
    return True


def premier_plus_proche(n):
    while not est_premier(n):
        n += 1
    return n

def epreuve_math_premier() :
    print("Les nombres premiers t’attendent. Sauras-tu relever ce défi ?!")
    time.sleep(3)
    n = random.randint(10,20)
    print("Épreuve de Mathématiques: Trouver le nombre premier le plus proche de " + str(n) +".")
    time.sleep(2)
    x = int(input("Votre réponse : "))
    if x == premier_plus_proche(n) :
        print("Correct! Vous gagnez une clé.")
        return True
    else :
        print("Désolé la réponse correcte était {}.".format(premier_plus_proche(n)))
        return False






def epreuve_roulette_mathematique() :
    print("La roulette des nombres est en marche. Prépare-toi à être surpris !")
    time.sleep(3)
    l = []
    reponse_1 = 0
    reponse_2 = 1
    for i in range(6):
        x = random.randint(1, 20)
        l.append(x)

    print("Nombres sur la roulette :", l)

    y = random.choice(["+", "-", "*"])

    if y == "+":
        for i in range(6):
            reponse_1 += l[i]
        print("Calculez le résultat en combinant ces nombres avec une addition.")
        time.sleep(2)
    elif y == "-":
        reponse_1 = l[0]
        for i in range(1, 6):
            reponse_1 -= l[i]
        print("Calculez le résultat en combinant ces nombres avec une soustraction.")
        time.sleep(2)
    else:
        for i in range(6):
            reponse_2 *= l[i]
        print("Calculez le résultat en combinant ces nombres avec une multiplication.")
        time.sleep(2)

    reponse_utilisateur = int(input("Votre réponse : "))

    if reponse_utilisateur == reponse_1 or reponse_utilisateur == reponse_2:
        print("Bonne réponse! Vous avez gagné une clé.")
        return True
    else:
        if y == "+" or y == "-":
            print("Désolé la bonne réponse était {}.".format(reponse_1))
        else:
            print("Désolé la bonne réponse était {}.".format(reponse_2))
        return False



def resoudre_equation_lineaire() :

    a = random.randint(0,10)
    b = random.randint(0,10)
    solution = round(-b/a,2)

    return(a,b,solution)



def epreuve_math_equation() :
    print("Les mystères des équations t’appellent. Vas-tu les déchiffrer ?")
    time.sleep(3)

    a,b,solution = resoudre_equation_lineaire()

    print("Épreuve de Mathématiques: Résoudre l'équation {}x + {} = 0".format(a,b))
    time.sleep(2)
    reponse = int(input(" Quelle est la valeur de x au centième prés : "))

    if reponse == solution :
        print("Correct! Vous gagnez une clé.")
        return True
    else :
        print("Désolé la réponse correcte était {}".format(solution))
        return False






def epreuve_math() :
    print("Prêt pour un challenge mathématique ? L’aventure commence maintenant !")
    time.sleep(5)

    print("L’heure du défi a sonné ! Une des épreuves suivantes te sera attribuée au hasard : factorielle, nombres premiers, roulette mathématique ou équations.")
    time.sleep(7)

    print("Roulement de tambour… Découvrons ensemble quel défi te sera attribué !")
    time.sleep(3)

    epreuves = [epreuve_math_factorielle, epreuve_math_premier, epreuve_roulette_mathematique,epreuve_math_equation]
    x = random.choice(epreuves)()
    if x == True :
        return True
    else :
        return False

epreuve_math()





