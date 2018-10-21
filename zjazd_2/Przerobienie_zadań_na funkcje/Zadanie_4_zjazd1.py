
def naleznosc(cena,waga):
    return cena * waga



def drukuj_metke(cena,waga):

    wynik= f"""
    Cena za kg: {cena}
    Waga: {waga}
    Naleznosc : {naleznosc(cena,waga)}
    """

    return wynik

print(wynik)

def test_drukuj_metke():
    assert drukuj_metke(10,2.5)== """
    Cena za kg: 10
    Waga: 2.5
    Naleznosc : 25
    """