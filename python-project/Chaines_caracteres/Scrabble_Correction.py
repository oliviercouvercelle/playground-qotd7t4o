def ma_fonction(tirage):
    if len(tirage)==7:
        compteur_voyelles=0
        compteur_consonnes=0
        for lettre in tirage:
            if lettre in 'AEIOUY':
                compteur_voyelles+=1
            else :
                compteur_consonnes+=1
        if compteur_voyelles>=2 and compteur_consonnes>=2:
            return 'VALIDE'
        else:
            return 'NON VALIDE'
    else:
        return 'NON VALIDE'
