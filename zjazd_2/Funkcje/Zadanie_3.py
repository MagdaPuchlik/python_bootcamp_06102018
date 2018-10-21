
def policz_znaki(napis, arg1='<', arg2='>'):

    poziom =0
    dlugosc =0


    for znak in napis:
        if znak == arg1:
            poziom+=1
        elif znak == arg2:
            poziom-=1
        else:
            dlugosc+=poziom

    return dlugosc



def test_dla_braku_nawiasu():
    assert policz_znaki("")==''
def test_dla_jednego_nawiasu():
    assert policz_znaki('dla <tego> tekstu')==4
def test_dla_nawiasu_jednego_wskazanego():
    assert policz_znaki('dla [dluzszego] tesktu','[',']')==9
def test_dla_nawiasu_zagniezdzonego_wiele_razy():
    assert policz_znaki('dla [dlu[zsz]ego] tesktu','[',']')==12


