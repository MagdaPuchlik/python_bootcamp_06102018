
min_ = None
max_ = None

a=1

while True:

    dane_wejsciowe= input("Podaj liczbę lub wpisz wyjdz by zakończyć:")
    if dane_wejsciowe == "wyjdz":
        break
#przerwanie działania kodu w momencie wpisania słowa wyjdz

    liczba =int(dane_wejsciowe)
#z wprowadzonych danych wejściowych tworzę liczbę

    if min_ is None or liczba < min_:
         min_ =liczba
    if max_ is None or liczba> max_:
        max_=liczba
#   wyjątek
    #przy None mogę zapisać is zamiast ==

    print(f"Podaj liczbę min:{min_}")
    print(f"Podaj liczbę max:{max_}")

if not min_:
    print("Nie znaleziono min")

if not max_:
    print("Nie znaleziono max")