import random

def factorielle(n) :
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x

print(factorielle(5))

def epreuve_math_factorielle() :
    x = random.randint(1,10)
    print(" Épreuve de Mathématiques: Calculer la factorielle de ",x)
    y = int(input((" Votre réponse : ")))

    reponse_correcte = factorielle(x)

    if reponse_correcte == y:
        print("Correct! Vous gagnez une clé")
        return True
    else :
        print("Désolé la réponse correcte était {}.".format(reponse_correcte))
        return False

    return y

print(epreuve_math_factorielle())
def epreuve_math_premier() :
    print(epreuve_math_premier)

def epreuve_roulette_mathematique() :
    print(epreuve_roulette_mathematique)

def epreuve_math() :
    print(epreuve_math)


l = [epreuve_math_factorielle, epreuve_math_premier, epreuve_roulette_mathematique]

print(random.choice(l))



