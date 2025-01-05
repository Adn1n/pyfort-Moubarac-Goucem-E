                                                    Fort boyart


### I - Présentation du projet 

**Titre** : ***Fort Boyard avec Python***

#### Contributeurs : 

- ***Adnan MOUBARAC :*** Vérification du code, réalisation des fonctions, rendre le code plus esthétique à l'aide des affichages, remplissage de ReadMe
- ***Cylia GOUCEM :*** Tests de chaques fonctions, l'ergonomie du code, réalisations des codes, remplissage de ReadMe


#### Description :

Fort Boyard Simulator est un projet qui recrée l’univers du célèbre jeu télévisé "Fort Boyard". 
Les joueurs doivent constituer une équipe et relever plusieurs types d'épreuves 
(mathématiques, hasard, logique, énigmes) pour collecter des clés. Une fois les clés obtenues, 
ils participent à une épreuve finale dans la salle du trésor pour tenter de gagner.



#### Fonctionnalités Principales :

Constitution d’une équipe de joueurs (jusqu’à 3 participants) avec des informations personnelles.

**Épreuves variées :**
- *Mathématiques :* Calculs de factorielle, équations linéaires, nombres premiers, roulette mathématiques.
- *Hasard :* Lancer de dés, bonneteau.
- *Logique :* Morpion.
- *Énigmes du Père Fouras :* Résolution d’énigmes mythiques.
- Sauvegarde des performances des joueurs dans un fichier.

**Épreuve finale :** Décodage du mot-clé pour accéder à la salle du trésor.
**Historique :** Permet d'afficher l'historique des parties 



#### Technologies Utilisées :

**Langage de programmation :** Python 

**Bibliothèques :**
- time : Pour implémenter des fonctions liées avec le temps.
- random : Pour générer des événements aléatoires.
- json : Pour gérer les données des épreuves et les sauvegardes.

**Outils :** PyCharm, Git/GitHub.



#### Installation :

- **Instructions pour cloner le dépôt Git**
1) Connectez-vous à votre compte GitHub.
2) Accédez au dépôt du projet et copiez l'URL du dépôt.

3) Dans PyCharm :
- Allez dans File > New Project from Version Control > Git.
- Collez l’URL du dépôt dans le champ correspondant.
- Sélectionnez un dossier local pour le projet.
- Cliquez sur Clone. Le projet sera importé dans PyCharm.


**Étapes pour configurer l’environnement de développement**



#### Utilisation :

Pour utiliser ce jeu avec PyCharm, il vous suffit de lancer le fichier 
main après avoir téléchargé tous les fichiers nécessaires au jeu, qui se trouve sur Github, 
sans apporter de modifications. Au fur et à mesure de votre progression dans le 
jeu, vous devrez partager vos réponses directement dans le terminal.



### II - Documentation Technique

#### Algorithme du jeu :

1)  L'utilisateur compose une équipe de joueurs.
2) **Menu principal :** Choix d'épreuves (mathématiques, hasard, logique, etc.).
3) **Épreuves :** Chaque épreuve renvoie un résultat (succès ou échec).
4) **Clés collectées :** Une fois trois clés obtenues, passage à l'épreuve finale.
5) **Épreuve finale :** Décodage du mot-clé pour gagner.
6) **Sauvegarde :** Les performances des joueurs sont sauvegardées.


#### Détails des fonctions implémentées :

- Épreuves mathématiques


1) ***def factorielle(nombre)*** :

Role : Calcul la factorielle d'un nombre 

Paramètre : n (int) : Le nombre dont on veut calculer la factorielle.

Résultat retourné : La factorielle de n.


2) ***def epreuve_math_factorielle() :***

Role : Propose à l'utilisateur de calculer la factorielle d'un nombre choisi aléatoirement

Paramètre : Aucun

Résultat retourné : Retourne True si la réponse de l'utilisateur est correcte.
                    Retourne False si la réponse est incorrecte.


3) ***def est_premier(n):***

Role : Déterminer si un nombre donné est un nombre premier.

Paramètre : n (int) : Le nombre à vérifier.

Résultat retourné : Retourne True si n est un nombre premier.
                    Retourne False si n n'est pas un nombre premier.


4) ***def premier_plus_proche(n):***

Role : Trouver le plus proche nombre premier supérieur ou égal à un nombre donné.

Paramètre : n (int), le nombre à partir duquel on commence à vérifier.

Résultat retourné : Retourne le nombre premier le plus proche (n).


5) ***def epreuve_math_premier() :***

Role : Propose au joueur de trouver le nombre premier le plus proche d'un nombre aléatoire généré.

Paramètre : Aucun

Résultat retourné : Renvoi TRUE si le joueur a donné la bonne réponse,
                    Renvoi False si la réponse est incorrecte


6) ***def epreuve_roulette_mathematique() :***

Role : Demande au joueur de calculer le résultat d'une opération (addition, soustraction, multiplication) appliquée à une liste de nombres aléatoires.

Paramètre : Aucun

Résultat retourné : Renvoie True si la réponse du joueur est correcte,
                    Renvoie False si la réponse est incorrecte.


7) ***def resoudre_equation_lineaire() :***

Role : Génère une équation linéaire de la forme ax + b = 0, et calcule sa solution.

Paramètre : Aucun

Résultat retourné : Renvoie un tuple (a, b, solution), où a et b sont les coefficients générés
et solution est la solution de l'équation arrondie au centième.


8) ***def epreuve_math_equation() :***

Role : Demande au joueur de résoudre une équation linéaire de la forme ax + b = 0.

Paramètre : Aucun

Résultat retourné : Renvoie True si le joueur a donné la bonne solution.
                    Renvoie False si la réponse est incorrecte.


9) ***def message_intro_math () :***

Role : Affichage introduction.

Paramètre : Aucun

Résultat retourné : Aucun (Affichage)


10) ***def epreuve_math() :***

Role : Permet de lancer une épreuve au hasard

Paramètre : Aucun

Résultat retourné : Renvoie les résultats de l'épreuve choisie



- Épreuve Hasards 


1) ***def message_bienvenue():***

Role : Affiche un message d'accueil et les règles du jeu du bonneteau.

Paramètre : Aucun

Résultat retourné : Aucun (Affichage)


2) ***def bonneteau() :***

Role : Simule le jeu du bonneteau où le joueur doit deviner sous quel bonneteau se trouve la clé.

Paramètre : Aucun

Résultat retourné : True si le joueur trouve la clé, False sinon


3) ***def message ():***

Role : Présente le contexte et les règles du jeu de lancer de dés.

Paramètre : Aucun

Résultat retourné : Aucun (Affichage)


4) ***def jeu_lance_des() :***

Role : Simule une partie où le joueur et le maître du jeu s'affrontent avec des lancers de dés.

Paramètre : Aucun

Résultat retourné : True si le joueur obtient un 6 en premier,
                    False si le maître du jeu gagne ou si c'est un match nul.


5) ***def message_debut ():***

Role : Affiche un message d'introduction aux épreuves

Paramètre : Aucun

Résultat retourné : Aucun (Affichage)


6) ***def epreuve_hasard() :***

Role : Choisit aléatoirement entre le jeu du bonneteau ou le lancer de dés et lance l'épreuve choisie.

Paramètre : Aucun

Résultat retourné : True si le joueur réussit l'épreuve choisie,
                    False sinon


- Énigme Pére Fouras 

1) ***def intro () :***

Role : Affiche un texte d'introduction et les règles pour l'épreuve des énigmes du Père Fouras.

Paramètre : Aucun

Résultat retourné : Aucun (Affichage)


2) ***def charger_enigmes() :***

Role : Charge et retourne les énigmes depuis un fichier JSON contenant les données des énigmes.

Paramètre : Aucun

Résultat retourné : Liste des énigmes sous forme de dictionnaires.


3) ***def enigme_pere_fouras() :***

Role : Simule une épreuve d'énigmes où le joueur à trois essais pour trouver la bonne réponse.

Paramètre : Aucun

Résultat retourné : True si le joueur trouve la bonne réponse à l'énigme.
                    False si le joueur échoue après avoir épuisé ses trois essais.



- Épreuve Logique

1) ***def afficher_grille(grille) :***

Rôle : Afficher la grille actuelle du jeu avec des séparateurs pour les lignes et les colonnes.

Paramètre : 
grille : La liste 2D représentant l'état actuel de la grille (3x3)

Résultat retourné : Aucun (affichage).


2) ***def verifier_victoire(grille, symbole) :***

Rôle : Détecter si un joueur a aligné trois symboles identiques horizontalement, verticalement ou en diagonale.

Paramètres :
1) grille : La liste 2D représentant l'état actuel de la grille (3x3).
2) symbole : Le symbole du joueur à vérifier ('X' ou 'O').

Résultat retourné : 
1) True si le joueur a gagné.
2) False sinon.


3) ***def coup_maitre(grille,symbole) :***

Rôle : Identifier le coup optimal pour gagner, bloquer le joueur, ou jouer aléatoirement si aucune priorité n'est trouvée.

Paramètres :
1) grille : La liste 2D représentant l'état actuel de la grille (3x3).
2) symbole : Le symbole du Maître du Jeu ('O').

Résultat retourné :
1) Un tuple (ligne, colonne) correspondant aux coordonnées de la case choisie.


4) ***def tour_joueur(grille) :***

Rôle : Permettre au joueur de saisir ses coordonnées et place son symbole sur la grille.

Paramètre :
1) grille : La liste 2D représentant l'état actuel de la grille (3x3).

Résultat retourné : Aucun (modifie la grille).


5) ***def tour_maitre(grille) :***

Rôle : Utiliser la fonction coup_maitre pour décider et jouer le coup du Maître du Jeu.

Paramètre :
1) grille : La liste 2D représentant l'état actuel de la grille (3x3).

Résultat retourné : Aucun (modifie la grille).


6) ***def grille_complete(grille):***

Rôle : Déterminer si toutes les cases de la grille sont occupées.

Paramètre :
1) grille : La liste 2D représentant l'état actuel de la grille (3x3).

Résultat retourné :
1) True si la grille est pleine.
2) False sinon.


7) ***def verifier_resultat(grille):***

Rôle : Vérifie si un joueur a gagné ou si la grille est pleine (match nul).

Paramètre :
1) grille : La liste 2D représentant l'état actuel de la grille (3x3).

Résultat retourné :
1) True si la partie est terminée.
2) False sinon.


8) ***def message_de_bienvenue() :***

Rôle : Présenter les règles du jeu et motiver les joueurs.

Paramètre : Aucun

Résultat retourné : Aucun (affichage).


9) ***def jeu_tictactoe() :***
10) 
Rôle : Alterner les tours entre le joueur et le Maître du Jeu jusqu'à la fin de la partie.

Paramètre : Aucun

Résultat retourné :
1) True si le joueur gagne.
2) False si le Maître du Jeu gagne ou en cas de match nul.



- Épreuve finale


1) ***def premier_caractere_majuscule(chaine) :***

Role : Met en majuscule la première lettre d'une chaîne tout en maintenant les autres lettres en minuscule

Paramètre : la chaîne de caractères à transformer (chaine)

Résultat retourné : la chaîne avec la première lettre en majuscule (premier_lettre + reste)


2) ***def intro_enigmes():***

Role : Affiche l'introduction du jeu pour l'utilisateur

Paramètre : Aucun

Résultat retourné : Aucun (Affichage)


3) ***def salle_De_Tresor () :***

Role : Simule une épreuve où le joueur à trois essais pour trouver la bonne réponse.

Paramètre : Aucun

Résultat retourné : True si le joueur trouve la réponse, False sinon



- Fonction utiles 


1) ***def introduction() :***

Rôle : Affiche un message d'accueil au joueur et explique le but du jeu.

Paramètres : Aucun

Résultat retourné : Aucun


2) ***def premier_caractere_majuscule(chaine) :***

Rôle : Met en majuscule la première lettre d'une chaîne tout en maintenant les autres lettres en minuscule.

Paramètre : la chaîne de caractères à transformer (chaine)

Résultat retourné : la chaîne avec la première lettre en majuscule (premier_lettre + reste)


3) ***def lettre_majuscule(chaine) :***

Rôle : Met en majuscule la première lettre de chaque mots de la chaîne tout en maintenant les autres lettres en minuscule.

Paramètre : la chaîne de caractères à transformer (chaine)

Résultat retourné : la chaîne avec la première lettre en majuscule de chaque mots (résultat)


4) ***def composer_equipe() :***

Rôle : Permet au joueur de créer une équipe de 1 à 3 joueurs, définissant leurs noms, professions, et désignant un leader.

Paramètres : Aucun

Résultat retourné : Une liste de dictionnaires représentant les joueurs et le nombre de joueurs.


5) ***def choisir_joueur(liste_equipe) :***

Rôle : Permet de sélectionner un joueur de l'équipe pour une épreuve.

Paramètres : liste_equipe (liste des joueurs disponibles)

Résultat retourné : Le dictionnaire correspondant au joueur sélectionné.


6) ***def menu_epreuves() :***

Rôle : Affiche un menu permettant de choisir une épreuve parmi celles disponibles.

Paramètres : Aucun

Résultat retourné : Aucun


7) ***def heure():***

Rôle : Récupère l'horodatage actuel sous le format "YYYY-MM-DD HH:MM:SS".

Paramètres : Aucun

Résultat retourné : 
1) Une chaîne de caractères contenant la date et l'heure actuelles formatées.


8) ***def ajouter_historique(joueur, epreuve, resultat, cles):***

Rôle : Enregistre les informations sur une partie dans un fichier d'historique.

Paramètres : 
1) joueur (str) : Nom du joueur.
2) epreuve (str) : Nom de l'épreuve réalisée.
3) resultat (str) : Résultat de l'épreuve ("Gagné", "Perdu", etc.).
4) cles (int) : Nombre de clés obtenues.

Résultat retourné : Aucun


9) ***def affichage_historique():***

Rôle : Affiche les entrées du fichier d'historique ligne par ligne.

Paramètres : Aucun

Résultat retourné : Aucun


- Main


1) ***def nb_de_cles(dico) :***

Rôle : Calcule le nombre total de clés gagnées par l'équipe.

Paramètres : 
1) dico (list[dict]) : Liste de dictionnaires représentant les joueurs, où chaque dictionnaire contient les clés gagnées.

Résultat retourné :
1) cle (int) : Nombre total de clés gagnées par l'équipe.


2) ***def introduction() :***

Rôle : Affiche un message introductif pour présenter les règles et l'objectif du jeu.

Paramètres : Aucun

Résultat retourné : Aucun


3) ***def jeu() :***

Rôle : Gère le déroulement principal du jeu Fort Boyard.

Paramètres : Aucun

Résultat retourné :
1) True si l'équipe réussit à ouvrir la salle du trésor.
2) False si l'équipe échoue à ouvrir la salle du trésor.



#### Gestion des Entrées et Erreurs :

- Gestion des Entrées 

Le code met en place plusieurs mécanismes pour gérer et valider les entrées des utilisateurs.
Ces validations garantissent que les valeurs saisies respectent les attentes et évitent les erreurs 
d'exécution.

1) Menus et Choix d'Options :

Les menus, comme celui des épreuves (menu_epreuves()), vérifient que l'entrée est un entier correspondant à une option valide.
Exemple : Si l'utilisateur entre une valeur non valide (ex : lettre ou chiffre hors plage), le programme demande une nouvelle saisie.

2) Coordonnées dans le Morpion :

La fonction tour_joueur(grille) vérifie si les coordonnées saisies par le joueur
respectent les limites de la grille (1 à 3 pour les lignes et colonnes).
Si la case sélectionnée est déjà occupée, un message est affiché, et le joueur doit entrer de nouvelles coordonnées.


- Gestions des Erreurs

1) Calculs :

Dans resoudre_equation_lineaire, le coefficient a est généré pour éviter la division par zéro.

2) Liste Vide dans l'IA du Morpion :

La fonction coup_maitre(grille, symbole) vérifie que des cases libres existent avant d'utiliser random.choice.
Cela évite une erreur si la liste est vide.


- Bugs connus 

1) Saisie incorrecte non gérée explicitement :

Si l'utilisateur entre une valeur non valide (par exemple, texte au lieu d'un nombre dans une épreuve),
une exception ValueError peut être levée.


2) Saisie d'équation non arrondie :
Dans epreuve_math_equation, si l'utilisateur entre une réponse correcte mais non arrondie 
(ex : 0.333 au lieu de 0.33), cela est considéré comme incorrect.






### III - Journal de Bord

#### Chronologie du Projet :


Le développement du projet s’est déroulé en plusieurs étapes bien définies,
avec une répartition claire des tâches entre les membres de l’équipe. Voici les étapes clés :

- Préparation de l’environnement de travail (05/12/2024) :
Installation des outils nécessaires, tels que PyCharm pour le développement et GitHub.

- Répartition des tâches (05/12/2024) :

- Développement des modules d’épreuves :

1) Épreuves mathématiques (05/12/2024) :
Implémentation des jeux de calcul

2) Épreuves de hasard (07/12/2024) :`
Création des épreuves bonneteau et lancer de dés.
Problèmes rencontrer : Lors de la saisie pour le bonneteau bien s'assurer la saisie de l'utilisateur 
et aussi faire en sorte que la saisie en minuscule est accepté

3) Énigmes du Père Fouras (17/12/2024) :
Intégration des énigmes à partir d’un fichier JSON et gestion des réponses des joueurs.
Problèmes rencontrer : Lors du chargement des données au début.

4) Fonctions Utiles (17/12/2024) :
Création des fonctions pour gérer les joueurs, les clés, et le menu des épreuves.
Implémentation de la sauvegarde des données pour permettre un suivi des parties.
Problèmes rencontrer : Lors de l'attribution du leader car il fallait deja qu'il n'y a qu'un seul leader.
Ainsi par la suite, s'il n'y a pas de leader attribuer automatiquement au premier candidat cette fonction

5) Épreuves logiques (29/12/2024) :
Développement des jeux comme le morpion.

6) Épreuve finale (25/12/2024) :
Création d'une dernière énigme avec des indices affichés à la suite s'il le joueur ne trouve pas la réponse.

7) Fichier Principal (main.py) (28/12/2024) :
Coordination de tous les modules pour créer une expérience de jeu fluide.
Tests finaux pour garantir le bon fonctionnement de l’ensemble.


   
#### Répartition des Tâches :

- ***Cylia GOUCEM*** 

1) Développement des épreuves factorielles et nombre premier *(Mathématique)*
2) Développement du jeu de lance dés et de l'ergonomie *(Hasard)*
3) Développement principal, l'ergonomie *(Énigme Pére Fouras)*
4) Développement principal *(Morpion)*
5) Développement principal, ergonomie *(Salle de trésor)*
6) Développement principal, ergonomie *(Fonction utiles)*
7) Développement principal, gestion des clés. *(Main)*


- ***Adnan MOUBARAC***

1) Développement des épreuves roulette mathématique et math équations. *(Mathématique)*
2) Développement des messages de bienvenues, et l'épreuve de bonneteau *(Hasard)*
3) Développement principal, l'ergonomie *(Énigme Pére Fouras)*
4) Développement principal, ergonomie *(Morpion)*
5) Développement principal, ergonomie *(Salle de trésor)*
6) Développement principal, messages de bienvenus *(Fonction utiles)*
7) Développement principal, logique de jeu, gestion des clés. *(Main)*


### IV - Test set Validation

#### Stratégies de Test :

Notre stratégie de test face à un dysfonctionnement du code consistait 
à adopter une approche en plusieurs étapes :

1) **Création d’un environnement de test isolé :** 

Nous avons commencé par copier le programme dans un fichier distinct, 
nommé test.py. Ce fichier servait de terrain d’expérimentation pour 
identifier et corriger les problèmes sans impacter directement le code principal.

2) **Débogage avec des impressions ciblées :**

Nous avons utilisé des instructions print pour afficher le contenu du code bloc par bloc. 
Cette méthode nous a permis de localiser précisément l’endroit où se situait le problème dans le programme.

Par exemple, lors de l’élaboration de notre code principal,
nous avons rencontré des difficultés initiales, 
notamment avec la composition de l’équipe et le fonctionnement du dictionnaire retourné.
Grâce à notre approche structurée, nous avons pu résoudre ces problèmes efficacement.

