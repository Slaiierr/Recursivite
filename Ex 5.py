def somme_tab(liste: list)-> float:
    if len(liste) == 1:
        return liste[0]
    else:
        element = liste.pop(0)
        return element + somme_tab(liste)
    
assert somme_tab([4, 5, 6]) == 15, "Le test 1 n'est pas validé"
assert somme_tab([-6]) == -6, "Le test 2 n'est pas validé"