def formatuj( *args,**kwargs): # *args podzili nam wszystko na tuple, kwargs to wykorzystanie slowniak
                                #ważna jest kolejność najpierw są args pózniej są kwergs

    out =[]

    for text in args:
        for k in kwargs:
            text = text.replace(f"${k}",str(kwargs[k]))
        out.append(text)

    return "\n".join(out)


x = ("koszt &cena PLN","koszt &cena USD","sumarycznie $cena",'podatek:$podatek')
y = {"cena":10, "podatek":0.23}

print(formatuj(*x,*y)) #pomimo tego , że daję gwiazdkę w funkcji (definmiując ją) to póżniej wywołując ją też muszę
                        #dodać gwiazdkę

def test_formatuj():
    assert formatuj(
        'koszt $cena PLN',
        'koszt $cena brutto',
        cena = 10
    ) == "koszt 10 PLN\nkoszt 10 brutto"

def test_formatuj():
    assert formatuj(
        'koszt $cena PLN',
        'koszt $cena brutto',
        "sumarycznie $cena",
        'podatek:$podatek',
        cena = 10,          #elementy kwargsów, podawane są jako słownik
        podatek = 0.23
    ) == "koszt 10 PLN\nkoszt 10 brutto\nsumarycznie 10\npodatek:0.23"