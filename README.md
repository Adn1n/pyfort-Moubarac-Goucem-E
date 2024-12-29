                                                    Fort boyart

### I - Présentation du projet 

**Titre** : ***Fort Boyard avec Python***

#### Contributeurs : 

- ***Adnan MOUBARAC :*** Vérification du code, réalisation des fonctions, rendre le code plus esthétique à l'aide des affichages, Remplissage de ReadMe
- ***Cylia GOUCEM :*** Tests de chaques fonctions, L'ergonomie du code, réalisations des codes, Remplissage de ReadMe


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
- *Logique :* Morpion, bâtonnets.
- *Énigmes du Père Fouras :* Résolution d’énigmes mythiques.
- Sauvegarde des performances des joueurs dans un fichier JSON.

**Épreuve finale :** Décodage du mot-clé pour accéder à la salle du trésor.



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






### II - Documentation Technique

#### Algorithme du jeu :

1)  L'utilisateur compose une équipe de joueurs.
2) **Menu principal :** Choix d'épreuves (mathématiques, hasard, logique, etc.).
3) **Épreuves :** Chaque épreuve renvoie un résultat (succès ou échec).
4) **Clés collectées :** Une fois trois clés obtenues, passage à l'épreuve finale.
5) **Épreuve finale :** Décodage du mot-clé pour gagner.
6) **Sauvegarde :** Les performances des joueurs sont sauvegardées.


#### Détails des fonctions implémentées :




#### Gestion des Entrées et Erreurs :





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

3) Énigmes du Père Fouras (17/12/2024) :
Intégration des énigmes à partir d’un fichier JSON et gestion des réponses des joueurs.

4) Fonctions Utiles (17/12/2024) :
Création des fonctions pour gérer les joueurs, les clés, et le menu des épreuves.
Implémentation de la sauvegarde des données pour permettre un suivi des parties.

5) Épreuves logiques (29/12/2024) :
Développement des jeux comme le morpion et les bâtonnets.

6) Fichier Principal (main.py) (28/12/2024) :
Coordination de tous les modules pour créer une expérience de jeu fluide.
Tests finaux pour garantir le bon fonctionnement de l’ensemble.


   

#### Répartition des Tâches :






### IV - Test set Validation

#### Stratégies de Test :
