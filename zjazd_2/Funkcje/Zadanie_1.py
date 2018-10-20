def czy_jest_pierwsza(liczba):

    for dzielnik in range(2, liczba):
        if liczba%dzielnik==0:
            return False
    return True

def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_jest_pierwsza(7)
    assert czy_jest_pierwsza(17)
    assert czy_jest_pierwsza(19)

def test_czy_jest_pierwsza_dla_liczby_nie_pierwszej():
    assert not czy_jest_pierwsza(4)
    assert not czy_jest_pierwsza(16)
    assert not czy_jest_pierwsza(24)


# słowko ASSERT
# dziala na dwa ssposoby
    #assert true - nic się nie dzieke
    #awsser fasle - nastepuje assert error

    # dązymy do tego, żeby po prawej stronie od słówka assert było True, musza być operacje logiczne