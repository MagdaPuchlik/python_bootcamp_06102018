def przywitaj_sie():    # definiuje własną funckję

    print("przywitałem się") # dzięki temu wpisowi za każdymr azem przy wywowału funkcji będzie też wywoałny ten print
    return 1            # przypiosuje jakiś wynik do mojej funkcji

x = przywitaj_sie()    # tu do x przypisuję 1

print(x)
print(type(przywitaj_sie()))
print(przywitaj_sie())

def podanie_imon(imie, wiek, wzrost, waga):
    print("witaj",imie)
    if wzrost >178:
        print("dragal")
    if waga > 80:
        print('paczek')
    if wiek > 38:
        print("starzec")


lista_osob = [
    {
        'imie':"Rafał",
        'wiek': 22,
        'wzrost':171,
        'waga':80,
    },
    {
        'imie': "Aga",
        'wiek': 56,
        'wzrost': 155,
        'waga': 55,
    }
]

for osoba in lista_osob:
    przywitaj_sie(osoba['imie'], osoba['wiek'],osoba['wzrost'],osoba['waga'])