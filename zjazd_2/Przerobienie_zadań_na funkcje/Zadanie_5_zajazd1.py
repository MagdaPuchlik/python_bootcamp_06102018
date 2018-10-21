def pobranie_danych():

    m_A = str(input("Podaj nazwę miasta A:"))
    m_B = str(input("Podaj nazwę miasta B:"))
    dystans = int(input(f"Dystans  {m_A} - {m_B}:"))
    cena = float(input(f"Jaka jest cena paliwa?:"))
    spal = float(input(f"Jakie jest spalanie?:"))

    return m_A,m_B,dystans,cena,spal #w tym miejscu do wyniku funckji pobieramy tylko zmienne z inputów

def obliczanie_kosztu(dystans,cena,spal):
    koszt = int(dystans / 100 * cena * spal)
    return koszt # zwracamy koszt przy pomocv argumentow pobranych w pierwszej funkcji

def drukuj_wynik(m_A,m_B,dystans,cena,spal):
    koszt = obliczanie_kosztu(dystans,cena,spal) #uzywamy wcześniejszej funkcji (powyżej stworzonej)
            #przypisujemy jej wynik dla wybranych argumentów do zmiennej koszt, uzytej póżniej w outupcie

    out = f"""

    Miasto A :{m_A}
    Miasto B: {m_B}
    Dystans {m_A} - {m_B}: {dystans}
    Cena paliwa: {cena}
    Spalanie na 100 km: {spal}

    Koszt paliwa na trasie {m_A}-{m_B} to {koszt} PLN

    """
    return (out)

dane = pobranie_danych()

print(drukuj_wynik(*dane))



