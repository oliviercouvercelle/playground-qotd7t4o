def ma_fonction(a,b,c):
    if a**2-b**2-c**2==0 or b**2-a**2-c**2==0 or c**2-a**2-b**2==0:
        return 'RECTANGLE'
    else :
        return 'PAS RECTANGLE'
