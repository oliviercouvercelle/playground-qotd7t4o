def ma_fonction(n):
    ligne=[1]
    for i in range(n):
        ligne_temporaire=[1]
        for j in range(1,len(ligne)):
            ligne_temporaire.append(ligne[j-1]+ligne[j])
        ligne_temporaire.append(1)
        ligne=list(ligne_temporaire)
    return ligne
