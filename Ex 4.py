
# 2) a)
def recursive_puissance(x: float, n: int)-> float:
    if n == 0: # condition d'arrêt
        return 1
    else:
        return x * recursive_puissance(x, n - 1) # appel récursif
    
assert recursive_puissance(2, 0) == 1, "Le test 1 n'est pas bon"
assert recursive_puissance(2, 3) == 8, "Le test 2 n'est pas bon"


def puissance(x: int, n: int)-> float:
    resultat = 1
    for i in range(n):
        resultat = x * resultat
    return resultat

assert puissance(2, 0) == 1, "Le test 1 n'est pas bon"
assert puissance(2, 3) == 8, "Le test 2 n'est pas bon"