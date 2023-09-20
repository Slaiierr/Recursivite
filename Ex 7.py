def recursive_puissance(x: float, n: int) -> float:
    if n == 0:  # condition d'arrêt
        return 1
    else:
        return x * recursive_puissance(x, n - 1)  # appel récursif


print(recursive_puissance(2, 900))
print(recursive_puissance(2, 986))  # dernier calcul que python peut faire
# arret de python car trop d'appel récursif (débordement de pile)
print(recursive_puissance(2, 987))
