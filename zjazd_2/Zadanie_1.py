def czy_jest_pierwsza(x):

    for dzielnik in range(2,x):
        if x%dzielnik==0:
            return False
    return True

liczba=int(input(f"podaj liczbę:"))
print(czy_jest_pierwsza(liczba))