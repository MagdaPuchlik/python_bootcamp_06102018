def wiecej_niz(napis, liczba):
    return{znak for znak in napis if napis.lower().count(znak) > liczba}


def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("",0)==set()

def test_wiecej_ni_dla_niepustego_napisu():
    assert wiecej_niz("aaaaabbb",2) =={'a','b'}

def test_wiecej_ni_dla_niepustego_napisu_duze_male_litery():
    assert wiecej_niz("aaaAAAAaabbb",4) =={'a'}