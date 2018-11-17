
import json

pracownicy ={}


    komenda=input(f"co chcesz zrobic?: [d]odaj,[w]ypisz by przerwać zakupy")

    if komenda == 'd':

        with open("employees.json") as f:
            pracownicy = json.load(f)

        imie = input(f"Imie:")
        nazwisko = input(f"Nazwisko:")
        rok = int(input(f"Rok urodzenia:"))
        Pensja = int(input(f"Pensja:"))

        liczba = len(pracownicy)+1

        napis = f"{imie} {nazwisko} - rok:{rok}, pensja:{Pensja} PLN"

        pracownicy[liczba] = napis

        with open("employees.json", "w")as f:
            json.dump(pracownicy, f)

        with open("employees.json") as f:
            pracownicy = json.load(f)
            print(pracownicy)

    if komenda == 'w':
        # print(pracownicy.items())

        with open("employees.json") as f:
            pracownicy = json.load(f)
            print(pracownicy)

