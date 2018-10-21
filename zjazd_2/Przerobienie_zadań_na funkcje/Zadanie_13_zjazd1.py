#1 trzeba pobrac dane

def pobieranie_danych(ile_razy=7):

    temperatury = []

    for i in range(ile_razy):
        temp = int(input("podaj temperature:"))
        temperatury.append(temp)
    return temperatury

#3 ustalic min i max

def srednia_temp(temperatury):
    srednia_tempaeratura = int(sum(temperatury)/len(temperatury))
    return srednia_tempaeratura

def min_temp(temperatury):
    minimalna_temperautra = min(temperatury)
    return  minimalna_temperautra

def max_temp(temperatury):
    max_tempaertura = max(temperatury)
    return max_tempaertura

def prezentuj_dane(srednia_tempaeratura,minimalna_temperautra,max_tempaertura):

    print(f"srednia:{srednia_tempaeratura}")
    print(f"min:{minimalna_temperautra}")
    print(f"max:{max_tempaertura}")


dane = pobieranie_danych() # przypisanie do zmiennej dane , wszystkich wartości wprowadzonych na początku
sr = srednia_temp(dane)
min_t = min_temp(dane)
max_t =max_temp(dane)
prezentuj_dane(sr,min_t,max_t)






