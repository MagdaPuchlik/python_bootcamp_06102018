
import json

try:
    with open("pracownicy.json")as f:
        pracownicy = json.load(f)
except FileNotFoundError:
    pracownicy=[]

# try oraz except to przykład obsługi wyjątków

komenda=input(f"co chcesz zrobic?: [d]odaj,[w]ypisz by przerwać zakupy")

if komenda == 'd':

        imie = input(f"Imie:")
        nazwisko = input(f"Nazwisko:")
        rok = int(input(f"Rok urodzenia:"))
        Pensja = int(input(f"Pensja:"))

        pracownik = {
            "imie": imie,
            "nazwisko":nazwisko,
            "rok urodzenia":rok,
            "pensja":Pensja,
        }

        pracownicy.append(pracownik)
        with open("pracownicy.json","w") as f:
            json.dump(pracownicy,f)

elif komenda == "w":
        print("Pracownicy:")
        for i, pracownik in enumerate(pracownicy, start=1):
            print(f"[{i}] {pracownik['imie']}{pracownik['nazwisko']} - rok: {pracownik['rok urodzenia']} , pensja {pracownik['pensja']} PLN")
else:
        print("Dokonano złego wyboru")