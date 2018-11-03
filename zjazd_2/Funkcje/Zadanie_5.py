def silnia(liczba):

    wynik =1

    for x in range(1,liczba+1):
        wynik = wynik*x

    return wynik

print(silnia(5))

def test_silnia_dla_liczby():
    assert silnia(5)==120
def test_silnia_dla_1():
    assert silnia(1)==1
