# Calcul approché d'aires par la méthode des rectangles.
`Difficulté : Moyenne`

### Présentation

Le but de cette fiche est de présenter la méthode des rectangles pour calculer l'aire sous une courbe représentative d'une fonction. Pour simplifier la présentation, on supposera ici que nos fonctions sont toutes positives sur l'intervalle sur lequel on les considère.

Définissons d'abord ce qu'est l'aire sous la courbe représentative d'une fonction sur un intervalle [a,b] : C'est tout simplement l'aire comprise entre la courbe représentative, l'axe des abscisses et les droites x=a et x=b.

![Illustration](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Aire_sous_la_courbe.svg/220px-Aire_sous_la_courbe.svg.png)

Présentons à présent la méthode des rectangles pour calculer l'aire sous la courbe représentative d'une fonction ***f*** sur un intervalle [a,b].  
L'idée est d'approcher l'aire sous la courbe par des rectangles dont l'aire est facilement calculables comme sur la figure ci-dessous.
![Illustration](http://informatique.coursgratuits.net/methodes-numeriques/img/analnu69.jpg)
Pour cela, on procède comme suit :
1. On commence par choisir le nombre ***n*** de rectangles qu'on veut sous la courbe. Plus le nombre sera grand, plus la surface formée par les rectangles sera proche de l'aire sous la courbe.
1. On répartit sur [a,b] ***n+1*** points de la façon équitable suivante : $`x_0=a`$ et $`x_{n+1}=x_n+\frac{b-a} n`$.
1. On construit le premier rectangle de largeur $`\frac{b-a} n`$ entre $`x_0`$ et $`x_1`$ sur l'axe des abscisses et de hauteur $`f(x_0)`$. Son aire est donc de $`\frac{b-a}n \times f(x_0)`$
1. On contruit le deuxième rectangle juste à coté de même largeur $`\frac{b-a} n`$ mais qui  cette fois ci est entre $`x_1`$ et $`x_2`$ sur l'axe des abscisses et de hauteur $`f(x_1)`$. Son aire est donc de $`\frac{b-a}n \times f(x_1)`$
1. On continue ainsi jusqu'à arriver au dernier rectangle qui finira en b donc commencera à $`x_{n-1}`$. Son aire sera $`\frac{b-a}n \times f(x_{n-1})`$

Finalement, l'aire de tous ces rectangles ainsi construits sera : $`\frac{b-a}n \left(f(x_0)+f(x_1)+\dots+f(x_{n-1})\right)`$.

Dans la fenêtre ci-dessous, vous avez juste à appuyer sur Run pour voir une illustration. Vous pouvez modifier les paramètres pour voir les conséquences.

@[Illustration de la méthode des rectangles]({"stubs": ["Maths/Methode_rectangles_illustration.py"], "command": "python3 Maths/Methode_rectangles_illustration_Test.py"})

---

### A vous de jouer

Créez un programme qui prend en entrée ***f***, ***a***, ***b*** et ***n*** et affiche (avec `return`) l'aire calculée par la méthode des rectangles.

> Entrée : Une fonction ***f***, les bornes de l'intervalle ***a*** et ***b*** et le nombre de subdivisions ***n***.

> Sortie : L'aire calculée avec la méthode des rectangles et affichée avec `return`. L'erreur admise pour passer les tests est de 0.05 par rapport à la valeur exacte.

@[Méthode des rectangles]({"stubs": ["Maths/Methode_rectangles.py"], "command": "python3 Maths/Methode_rectangles_Test.py"})

---

### Amélioration possible

On peut améliorer sensiblement la méthode précédente pour qu'elle donne une meilleure approximation de l'aire cherchée en prenant simplement $`f\left(\frac{x_i+x_{i+1}}2\right)`$ au lieu de $`f(x_i)`$ à chaque étape comme hauteur des rectangles. Cela revient à prendre le rectangle qui passe par le point sur la courbe au milieu de chaque intervalle plutôt que sur le bord.  
Graphiquement cela correspond à ces rectangles :
![milieu](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Int%C3%A9gration_num_rectangles.svg/300px-Int%C3%A9gration_num_rectangles.svg.png)

Copiez collez votre programme précédent dans la fenêtre ci-dessous et modifier le pour qu'il calcule l'aire en utilisant le point au milieu de chaque intervalle.

Vous pourrez constater la nette amélioration de la précision par ce simple petit changement. L'erreur admise pour passer les tests est de 0.001 par rapport à la valeur exacte.

@[Méthode des rectangles avec point au milieu]({"stubs": ["Maths/Methode_rectangles_milieu.py"], "command": "python3 Maths/Methode_rectangles_milieu_Test.py"})

