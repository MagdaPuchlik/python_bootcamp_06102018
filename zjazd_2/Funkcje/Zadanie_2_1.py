def wiecej_niz(napis, liczba):

    zbior={} # tu tworze słownik
    zwrot =set() # tu tworzę zbior
    napis = napis.lower()
    for litera in napis:
        litera = litera.lower()
        if napis.count(litera)> liczba:
            zwrot.add(litera)

    return zwrot



def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("",0)==set()

def test_wiecej_ni_dla_niepustego_napisu():
    assert wiecej_niz("aaaaabbb",2) =={'a','b'}

def test_wiecej_ni_dla_niepustego_napisu_duze_male_litery():
    assert wiecej_niz("aaaAAAAaabbb",4) =={'a'}