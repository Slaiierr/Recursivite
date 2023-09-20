def inverser(ch: str) -> str:
    n = len(ch)  # n = taille
    if n <= 1:
        return ch[0]
    else:
        return inverser(ch[1:]) + ch[0]


print(inverser("aBc45f !"))
