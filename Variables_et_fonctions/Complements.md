<h1> <center>Compléments de cours : Variables et opérations </center></h1>

Cette page est un complément du cours sur les variables et opérations pour approfondir ce qui a déjà été vu. Rien de ce qui suit n'est à proprement parler indispensable pour pouvoir programmer mais constitue des connaissances à avoir sur python soit pour gagner en temps et en lisibilité soit pour éviter des erreurs difficiles à déceler. Elle est donc à lire en entier au moins une fois.

# Première partie : Affectations de variables

Nous avons déjà vu comment affecter à des variables des valeurs. Il y a plusieurs façons d'améliorer ces affectations selon la situation.
+ Commençons par la technique la plus utile : l'incrémentation. Il va nous arriver très souvent de vouloir augmenter une variable d'une certaine valeur. Une façon de faire pour ajouter 3 à une variable x est :
  ```python
  x = x + 3
  ```
  Mais on peut synthétiser cette écriture sous la forme :
  ```python
  x += 3
  ```
  Cela peut sembler anecdotique mais quand on a beaucoup de variables avec des noms longs et peu agréables à écrire, on savoure le plaisir de n'avoir à les écrire qu'une fois grâce à cette notation.  
  Cette notation existe pour beaucoup d'opérations classiques. On peut soustraire une valeur à une variable (avec -=), multiplier (\*=), diviser (/=), mettre à la puissance (\*\*=), effectuer la division euclidienne (//=) ou le reste (%=) ...  
  Exemple (Vous pouvez modifier les exemples pour tester par vous même):
  ```python runnable
  x = 3
  x += 4
  print(x)
  x -= 1
  print(x)
  x *= 2
  print(x)
  x //= 3
  print(x)
  x **= 2
  print(x)
  ```
+ Supposons que nous voulions affecter à *a*, *b* et *c* la même valeur 3. Une façon de faire serait :
  ```python
  a = 3
  b = 3
  c = 3
  ```
  Mais on a en Python la possibilité de regrouper ces affectations en une seule en écrivant : 
  ```python
  a = b = c = 3
  ```
  Une remarque importante : si plus tard dans notre programme, on stocke dans *b* la valeur 4. Alors *a* et *c* resteront à la valeur 3. C'est dans la même logique que quand on écrit b=a+3 : Python calcule a+3 et stocke le résultat dans b. 
+ Supposons maintenant que nous voulions affecter à *a*, *b* et *c* des valeurs différentes. On a vu qu'on pouvait écrire :
  ```python
  a = 3
  b = 7
  c = 1
  ```
  Mais on a en Python la possibilité de regrouper ces affectations en une seule en écrivant : 
  ```python
  a, b, c = 3, 7, 1
  ```
  Python affecte à la première variable la première valeur, à la deuxième variable la deuxième valeur etc.
+ On peut améliorer encore cette dernière technique en utilisant stockant dans des variables des calculs utilisant ces mêmes variables. Par exemple : supposons que x=1 et y=4 et qu'on veuille maintenant stocker dans x le résultat de x+y et dans y le résultat de x-y. Pour cela, on écrirait simplement : 
  ```python
  x, y = 1, 4
  x, y = x + y, x - y
  ```
  Remarque importante : Ce que l'on vient de faire est très différent de :
  ```python
  x = 1
  y = 4
  x = x + y
  y = x - y
  ```
  Vous pouvez le constater en appuyant sur Run et observer les résultats :
  ```python runnable
  x, y = 1, 4
  x, y = x + y, x - y
  print("Résultat dans le premier cas : x =",x,"et y =",y)
  x = 1
  y = 4
  x = x + y
  y = x - y
  print("Résultat dans le second cas : x =",x,"et y =",y)
  ```
  Explications : Dans le premier cas, Python calcule x+y et x-y puis stocke en mémoire. Dans le second cas, on calcule d'abord x+y et on stocke dans x ce qui veut dire que x vaut maintenant 5 puis calcule x-y (avec x=5 donc) puis stocke dans y. Le résultat n'est donc pas le même.  
  Cette technique est très pratique par exemple pour intervertir les valeurs de certaines variables. Il suffit d'écrire `x, y = y, x`.

# Deuxième partie : Compléments sur la fonction `print`

Nous avons vu comment afficher la valeur d'une variable en utilisant la fonction `print`. Nous allons voir que nous pouvons améliorer cette affichage.
+ Afficher un texte : Pour Python, tout ce qui est entre guillemets (ou apostrophes) est considéré comme du texte (Informatiquement, c'est plus précisément une chaine de caractère). Donc si on veut afficher un texte, il suffit de le mettre entre guillemets et l'afficher avec print ce qui donnerait par exemple : 
  ```python runnable
  print("Bonjour")
  print("Hello World !")
  ```
+ Afficher plusieurs variables d'affilée : On remarquera dans l'exemple précédent que Python va à la ligne chaque fois qu'on utilise `print`. Il peut être utile d'afficher sur une seule ligne des données. Pour cela il suffit simplement de les séparer par des virgules à l'intérieur de la fonction print. On peut ainsi afficher des variables, du texte ou un mélange de tout cela.  
  Par exemple :
  ```python runnable
  x = 3
  y = 3*x**2-1
  print("Pour x =", x,"la valeur de 3x²-1 est",y)
  ```
  On remarquera que les *x* qui sont dans les guillemets ne sont pas remplacés par la valeur de x contrairement au *x* hors guillemets qui lui l'est. 
+ Un peu plus anecdotique, il peut arriver qu'on utilise plusieurs fois la fonction `print` mais qu'on ne veuille pas aller à la ligne ou bien qu'on veuille rajouter quelque chose en fin de phrase. Pour cela, il faut préciser dans la fonction `print` ce qu'on veut à la fin en écrivant `print("Le texte ou des variables", end="Ce qu'on veut mettre à la fin")`. De base, quand on ne met rien, on a `end = "\n"` car \n dans un texte est remplacé automatiquement par un retour à la ligne. Donc si on ne veut pas de retour à la ligne, il suffit d'écrire `print("texte", end="")`.  
Par exemple si on veut coller deux résultats pour n'afficher qu'un nombre :
```python runnable
debut=12
fin=345
print(debut,end="")
print(fin)
```
Exemple de modification de fin de phrase avec print et d'utilisation de \n dans un texte:
```python runnable
print("ABC\nDE",end=" *hic!*\n")
print("FG\nHI",end=" *hic!*\n")
print("J\nK\nL\nM\nN\nO", end=" *hic!*\n")
print("PQRSTUVWXYZ", end =" *BOUM !*")
```

# Troisième partie : Les nombres en Python et les erreurs d'arrondi

Les nombres ne sont pas tous traités de la même façon par Python. Les calculs avec les entiers sont beaucoup plus naturels pour Python que ceux avec les décimaux (que l'on appelle flottants en informatique). Prenons un exemple : 
```python runnable
x=2**100
print(x)
y=2.0**100
print(y)
print(x+1-x)
print(y+1-y)
```
Analysons les résultats : Dans un premier temps, on a stocké dans x la valeur de 2 puissance 100 (calcul avec des entiers). Dans  un deuxième temps, on a stocké dans y la valeur de 2 puissance 100 mais en calculant avec 2.0 c'est à dire un nombre flottant. Mathématiquement, il n'y a aucune différence mais dans la façon dont Python gère les deux, il y a une énorme différence. On peut le voir en effectuant les calculs x+1-x et y+1-y. Mathématiquement, le résultat est 1 mais dans le deuxième cas, Python obtient 0. La raison est simple : Python ne peut pas stocker une infinité de chiffres après la virgule donc il n'en garde qu'une partie en mémoire donc dès qu'on manipule des nombres qui ont plus de chiffres que le nombre de chiffres que Python a en mémoire, cela crée des erreurs d'arrondi. Par exemple 2 puissance 100 possède 31 chiffres. Si python garde en mémoire (par exemple) les 20 premiers chiffres et qu'on ajoute 1, le nombre obtenu sera pour python le même que si on n'ajoute pas 1 puisque ce 1 s'ajoute dans les chiffres non gardés en mémoire. Donc quand on resoustrait y, on retombe sur 0. Par contre quand on travaille avec des entiers, les calculs sont exacts.   
On peut le voir encore plus facilement en tapant : 
```python runnable
print(0.1+0.1+0.1)
```
On voit que le résultat n'est pas 0.3 ! Cette petite erreur qui semble ridicule peut vite grossir si on continue à faire des calculs ensuite. Le problème va surtout se poser si on veut par exemple vérifier si le résultat d'un calcul vaut 0.3. Pour Python on aura 0.1+0.1+0.1 différent de 0.3.  
Moralité : Eviter d'utiliser les nombres flottants pour des calculs trop long, complexes précis et pour tester si des résultats sont égaux ou pas.

Si on veut faire des calculs plus précis, on pourra s'intéresser au module Decimal.  
Pour plus de précision sur ces erreurs d'arrondi, on pourra regarder [la doc python](https://docs.python.org/fr/2/tutorial/floatingpoint.html)

  
# Quatrième partie : QCM

Voici quelques QCM pour voir si vous avez bien compris. N'hésitez pas à relire ce qui précède si vous avez un doute.

###### QCM 1
```python
a, b = 5, 2
b, a = a+1, b-a
print(a, b)
```  
?[Quelles valeurs sera affichée si on execute le programme ci-dessus ? ]
-[ ] 6 -3
-[ ] -4 6
-[ ] 3 -3 
-[x] -3 6

---

###### QCM 2
```python
a = 4
b = 2
b *= 3
a += b
print(a)
```  
?[Quelle valeur sera affichée si on execute le programme ci-dessus ? ]
-[x] 10
-[ ] 3
-[ ] 9
-[ ] 6

---

###### QCM 3
```python
a = b = 3
c = 2
b **= 2
b, c, a = a + c, a + b, b + c
print(a)
```
?[Quelle valeur sera affichée si on execute le programme ci-dessus ? ]
-[ ] 5
-[ ] 8
-[x] 11
-[ ] 17 

---

# A vous !

###### Exercice 1 :

Le but de cet exercice est de suivre un programme de calcul en partant d'un entier ***n*** qui sera donné automatiquement.

Appuyez sur Run et suivez les instructions qui s'affichent.

N'effacez pas ce que vous avez fait juste. Il faut rajouter au fur et à mesure en dessous.

Quand on demande d'afficher, c'est avec `print`.

@[Programme de calcul]({"stubs": ["Variables_et_fonctions/Programme_calcul3.py"], "command": "python3 Variables_et_fonctions/Programme_calcul3_Test.py"})

