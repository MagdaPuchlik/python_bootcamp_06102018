def wiecej_niz(napis, liczba):

    zbior={} # tu tworze słownik
    zwrot =set() # tu tworzę zbior
    for litera in napis:
        litera = litera.lower()
        zbior[litera]=zbior.get(litera,0)+1

    print(zbior)

    for key,value in zbior.items():
        if value > liczba:
            zwrot.add(key)

    return zwrot



def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("",0)==set()

def test_wiecej_ni_dla_niepustego_napisu():
    assert wiecej_niz("aaaaabbb",2) =={'a','b'}

def test_wiecej_ni_dla_niepustego_napisu_duze_male_litery():
    assert wiecej_niz("aaaAAAAaabbb",4) =={'a'}