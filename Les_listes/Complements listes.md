<h1> <center>Cours sur les listes (Suite)</center></h1>

# Liens entre listes et les parties précédentes du cours.

+ Lien avec la structure conditionnelle if... else... :  
  Supposons que je retrouve des piles, je veux alors les retirer de ma liste de courses si je les avaient notées et que je viens de me rappeler que j'ai besoin d'une brosse car elle a encore disparue de la salle je vais donc la rajouter si elle n'y est pas déjà. Cela donnerait un code comme ceci :
  ```python
  if  "piles" in ma_liste_de_courses:
      ma_liste_de_courses.remove("piles")
  if "brosse" not in ma_liste_de_courses :
      ma_liste_de_courses.append("brosse")
  ```

+ Lien avec la boucle for :
  - On peut énumérer les éléments d'une liste dans une boucle pour répéter des opérations pour chaque élément de la liste.
    Par exemple si je veux afficher les carrés des nombres d'une liste :
    ```python runnable
    liste_nombres = [1, 3, 7]
    for nombre in liste_nombres :
        print(nombre**2)
    ```
  
  - Des fois, quand on énumère dans une boucle for, on a besoin à la fois de l'élément dans notre liste mais aussi de son indice.  
    On peut utiliser la fonction `enumerate` et alors faire comme ceci :
    ```python runnable
    liste = [ 1, 4, 9, 3, 1, 2 ]
    for indice, element in enumerate(liste):
      print("Le nombre n°",indice, "est", element)
    ```

+ Lien avec les chaines de caractères :

  - `texte.split(separateur)` : Crée une liste des mots du texte qui sont compris entre les separateur. Si on met juste  `.split()`,  il prend comme séparateur un espace. Donnons des exemples pour clarifier :
    ```python runnable
    print("ab-cd-e/fg-h-ij kl".split( "-" ))
    print("Deux mots, un-autre-mot , Unmot".split())
    ```
    Remarquez bien dans les deux exemples qu'il ne considère comme séparateur que ce qu'on lui donne comme séparateur entre parenthèse (un espace si on ne lui donne rien).
    
  - `separateur.join(liste)` : L'exact contraire de split(). Crée un texte à partir d'une liste de mots en intercalant entre chaque mot le separateur.
    ```python runnable
    print(" / ".join( ["Janvier", "Février", "Mars", "Avril" ]))
    print(" <=> ".join( [ "x² - 1 = 0", "x² = 1", "x = 1 ou x = -1"]))
    print("".join([ "3", ".", "1", "4", "1", "5", "9" ]))
    ```
    On remarquera sur le dernier exemple qu'une chaine vide nous permet de coller tous les éléments de la liste.
    
# Listes en compréhension

Une des forces de Python : la possibilité de créer une liste à partir d'autres en rajoutant des conditions à la volée et le tout en une ligne !  
Donnons des exemples :
Pour augmenter de 3 tous les éléments d'une liste de nombres :
```python runnable
ma_liste_de_nombres = [1, 2, 3, 4, 5]
print([ n + 3 for n in ma_liste_de_nombres ])
```
Remarque : j'aurais pu mettre écrire directement `[ n+3 for n in range(1,6)]`.

Si je veux la somme des carrés des entiers de 1 à 10, je peux par exemple faire :
```python runnable
print(sum( [ n**2 for n in range(1,11) ] ))
```

Si je veux les longueurs des mots d'une liste de mots :
```python runnable
ma_liste_de_mots = [ "Cosinus", "Sinus", "Tangente", "Cotangente" ]
print([ len(mot) for mot in ma_liste_de_mots])
```
Et si pour cette même liste, je veux rajouter hyperbolique à chaque mot :
```python runnable
ma_liste_de_mots = [ "Cosinus", "Sinus", "Tangente", "Cotangente" ]
print([ mot +" hyperbolique" for mot in ma_liste_de_mots ])
```

On peut même rajouter des conditions :
Si je veux la liste des carrés des nombres pairs inférieurs à 15 (je rappelle qu'un nombre n est pair si et seulement si n%2==0) :
```python runnable
print([ n**2 for n in range(16) if n%2==0])
```

Si je veux récupérer la première lettre des mots d'une liste commençant par une voyelle :
```python runnable
ma_liste_de_mots= ["maths", "info", "python", "exposant", "alpha", "fonction", "parabole", "equilateral", "orthogonal", "cercle", "isocèle" ]
print([ mot[0] for mot in ma_liste_de_mots if mot[0] in "aeiouy"])
```
Quelques explications rapides sur cet exemple : `mot[0]` récupère la première lettre de `mot`. Pour vérifier que c'est une voyelle, je vérifie qu'elle appartient à "aeiouy". Voir le cours sur les chaines de caractères.

# Compléments : Problèmes de copies de listes
Quand on manipule souvent les listes, à un moment donné, on tombe sur le problème suivant :
```python runnable
ma_liste=[ 1, 2, 3]
sauvegarde= ma_liste
ma_liste[0]=4
print(sauvegarde)
```
Le problème ne saute peut-être pas aux yeux mais pourtant : J'ai une liste que je veux modifier mais avant je la sauvegarde (dans la variable `sauvegarde`). Puis je modifie le premier terme de ma liste d'origine et en affichant ma sauvegarde, je vois que ma sauvegarde est modifiée aussi !  
Le problème vient du fait que ma liste d'origine est stockée quelque part et toutes les variables qui y font référence renvoient vers ce seul et même stockage. Donc si je modifie d'un coté, ca modifie pour tout le monde.
Pour éviter ce problème, il suffit lors de la sauvegarde d'écrire `sauvegarde= list(ma_liste)` ou bien `sauvegarde= ma_liste.copy()`. Cela créera une vraie copie de notre liste qui sera sans lien avec celle d'origine.

# Listes de listes :
Dans une liste, on peut mettre beaucoup de choses différentes et entre autre des listes ce qui est bien pratique si on veut stocker comme dans un tableau.
Par exemple une grille de morpion pourrait s’écrire : ```grille = [["O", "X", "O"], ["O", "X", "X"], ["X", "O", "O"]]```
Pour récupérer l'élément de la deuxième ligne troisième colonne il suffit que j'écrive grille[1][2] car les listes commencent à 0 donc il faut penser à décaler d'un cran et de plus, grille[1] est la liste ["O", "X", "X"], c'est donc naturel que pour récupéré le troisième élément, on écrive grille[1][2].
Les listes de listes servent souvent à représenter un tableau mais on n'est pas obligé de s’arrêter à une profondeur de deux. On peut faire des listes de listes de listes...


# QCM

Voici quelques QCM pour voir si vous avez bien compris. N'hésitez pas à relire ce qui précède si vous avez un doute.

###### QCM 1
```python
liste = [ "T", "e", "x", "t", "e" ]
for i, c in enumerate(liste):
    print(i,c)
```  
?[Que va afficher ce programme (Les "/" représentent des retours à la ligne ? ]
-[x] 0 T / 1 e / 2 x / 3 t / 4 e 
-[ ] "Texte"
-[ ] T / e / x / t / e
-[ ] 1T / 2e / 3x / 4t/ 5e

---

###### QCM 2
```python
texte = "Un chasseur sachant chasser doit savoir chasser sans son chien."
print(texte.split())
```  
?[Que va afficher ce programme ? ]
-[ ] [Un, chasseur, sachant, chasser, doit, savoir, chasser, sans, son, chien.]
-[ ] "Unchasseursachantchasserdoitsavoirchassersanssonchien."
-[x] ["Un", "chasseur", "sachant", "chasser", "doit", "savoir", "chasser", "sans", "son", "chien."]
-[ ] "Un,chasseur,sachant,chasser,doit,savoir,chasser,sans,son,chien."

---

###### QCM 3
```python
texte = "Un chasseur sachant chasser doit savoir chasser sans son chien."
print(texte.split("t"))
```  
?[Que va afficher ce programme ? ]
-[x] ["Un chasseur sachan"," chasser doi", " savoir chasser sans son chien."]
-[ ] "Un chasseur sachan, chasser doi, savoir chasser sans son chien."
-[ ] ["Un chasseur sachant"," chasser doit", " savoir chasser sans son chien."]
-[ ] ["Un", "chasseur", "sachant", "chasser", "doit", "savoir", "chasser", "sans", "son", "chien."]

---

###### QCM 4
```python
liste = [ "06", "18", "54", "23", "34" ]
print(".".join(liste))
```  
?[Que va afficher ce programme ? ]
-[ ] "06 18 54 23 34"
-[ ] "0618542334"
-[x] "06.18.54.23.34"
-[ ] "06-18-54-23-34"

---

###### QCM 5
```python
liste = [ "06", "18", "54", "23", "34" ]
print("".join(liste))
```  
?[Que va afficher ce programme ? ]
-[ ] "06 18 54 23 34"
-[x] "0618542334"
-[ ] "06.18.54.23.34"
-[ ] "06-18-54-23-34"

---

###### QCM 6
```python
print([n**3 for n in range(5)])
```  
?[Que va afficher ce programme ? ]
-[ ] [0, 3, 6, 9, 12] 
-[ ] [0, 1, 2 ,3, 4]
-[x] [0, 1, 8, 27, 64]
-[ ] [0, 1, 4, 9, 16]

---

###### QCM 7
```python
print(...)
```  
?[Que faut-il mettre à la place des ... pour afficher la liste des carrés des entiers de 5 à 10 compris c'est à dire [25, 36, 49, 64, 81, 100] ? ]
-[x] [n**2 for n in range(5,11)]
-[ ] [n for n in range(5**2,10**2)]
-[ ] [n**2 for n in range(5,10)]
-[ ] list(range(5,11))**2

---

###### QCM 8
```python
liste=["maths", "info", "python", "exposants", "alpha", "fonctions", "parabole", "equilateral", "orthogonal", "cercles", "isocèle" ]
print(...)
```  
?[Que faut-il mettre à la place des ... pour afficher la liste des mots de la liste donnée qui se terminent par un "s" ? ]
-[ ] [ mot for mot in liste ]
-[ ] [ mot for mot in liste if mot[4]=="s"]
-[ ] [ mot for mot in liste if mot[0]=="s"]
-[x] [ mot for mot in liste if mot[-1]=="s"]


---

###### QCM 9
```python
grille= [[1,2,3],[4,5,6],[7,8,9]]
print(grille[2][1])
```  
?[Que va afficher ce programme ? ]
-[ ] 4
-[x] 8
-[ ] 2
-[ ] 6

<!--

# Entrainement 

### Exercice 1

Pour le nombre `n` donné dans la fenêtre ci-dessous, énumérez ses chiffres.

Pour l'affichage, on utilisera `print` et les chiffres seront affichés en allant à la ligne à chaque fois.

@[Exercice 1]({"stubs": ["Chaines_caracteres/chaine_exo_1bis.py"], "command": "python3 Chaines_caracteres/chaine_exo_1bis_Test.py"})

---

### Exercice 2

Pour le texte donné dans la fenêtre ci-dessous, créer un programme qui affiche le nombre de voyelle.

Pour l'affichage, on utilisera `print`.

@[Exercice 2]({"stubs": ["Chaines_caracteres/chaine_exo_2.py"], "command": "python3 Chaines_caracteres/chaine_exo_2_Test.py"})

---

### Exercice 3

Pour le texte donné dans la fenêtre ci-dessous, créer un programme qui affiche l'indice de tous les "e" dans ce texte.

Pour l'affichage, on utilisera `print` et les indices seront affichés en allant à la ligne à chaque fois.

@[Exercice 3]({"stubs": ["Chaines_caracteres/chaine_exo_1.py"], "command": "python3 Chaines_caracteres/chaine_exo_1_Test.py"})

-->
