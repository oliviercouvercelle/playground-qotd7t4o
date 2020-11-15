# Etude d'un systeme proie-prédateur (Modèle discret de Lotka-Volterra)
`Difficulté : Moyenne`

### Modélisation

Considérons deux espèces : une proie (des lièvres par exemple) et un prédateur (des lynx par exemple). On suppose qu'à ce jour, il y a 53000 proies et 9000 prédateurs et on se demande comment vont évoluer les populations de ces deux espèces. On suppose qu'il n'y a aucune autre intervention extérieur.

Une modélisation possible pour ce genre de système a été proposé par Lotka et Volterra. Pour des explications, on pourra par exemple regarder [ici](http://mathematiques.ac-bordeaux.fr/lycee2010/voie_generale/Stage_spe_TS/annexe12_modele_proie_predateur_de_volterra.pdf). 

Si on note $`u_n`$ la population de proies et $`v_n`$ la population de prédateurs à l'instant ***n***, alors peut modéliser leur évolution par :
```math
\left\{\begin{array}{l}u_{n+1}=(1+a-bv_n).u_n \\ v_{n+1}=(1-c+du_n).v_n\end{array}\right.
```
Nous allons prendre pour valeur a=0.09, b=0.00001, c=0.25 et d=0.000005.

Créez deux fonctions ***u*** et ***v*** qui prennent en entrée ***n*** et renvoie respectivement les valeurs de $`u_n`$ et $`v_n`$

> Entrée : Un entier ***n*** .

> Sortie : Deux fonctions ***u*** et ***v*** qui renvoie (avec `return`) respectivement les valeurs de $`u_n`$ et $`v_n`$.

@[Système de Lotka-Volterra]({"stubs": ["Les_fonctions/Volterra.py"], "command": "python3 Les_fonctions/Volterra_Test.py"})

---

### Représentation graphique

Pour voir graphiquement l'évolution des populations, copiez collez vos fonctions ***u*** et ***v*** dans la fenêtre ci-dessous.
Ne surtout pas modifier ce qui apparait déjà, c'est pour améliorer les performances de calcul. Nous verrons plus tard pourquoi il est indispensable de le faire et comment on le fait.

Vous pouvez modifier la valeur du minimum et maximum de ***n*** affiché. Pour des valeurs comme 500 par exemple, il faudra modifier un peu vos fonctions ***u*** et ***v*** pour coller à la réalité : Si la population tombe à 0, elle ne peut plus varier ensuite.

@[Système de Lotka-Volterra]({"stubs": ["Les_fonctions/Volterra_plot.py"], "command": "python3 Les_fonctions/Volterra_plot_Test.py"})
