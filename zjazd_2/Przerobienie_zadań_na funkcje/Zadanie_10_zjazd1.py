def pobranie_danych():

    a=int(input("Podaje liczbę a:"))
    b=int(input("Podaj liczbę b:"))
    oper = str(input("Podaj rodzaj operacji:"))

    return a,b,oper

def dzialanie(a,b,oper):
    wynik =0

    if oper=="+":
        wynik = a+b
    elif oper =="-":
        wynik = a-b
    elif oper=="*":
        wynik = a*b
    elif oper=="/":
        wynik = a/b
    else:
        raise ValueError("Nieprawidłowa wartość dla parametru typ operacji")

    return wynik


def prezentuj_wynik():
    dane = pobranie_danych()
    try:
        koniec = dzialanie(*dane)
    except ValueError:
        wynik = "operacja niestandardowa"
    print(koniec)

prezentuj_wynik()