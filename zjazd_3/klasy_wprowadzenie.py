x= 1
napis='napis'
y=1.2
slownik={}

def foo():
    pass

print(type(x),type(napis),type(y),type(slownik), type(foo))

#każda za zmiennych przypisana jest do jakieś klasy mówi nam o tym otwarcie polecenie type

# np. x jest instancją klasy int
# napis jest instancją klasy str

# instancja klasy = obiekt danej klasy
# atrybuty klasy
# metody klasy


###### TWORZENIE KLASY

### class Animal() <- nawias może być ale nie musi tzn, że możemy to zapisać:
# class Animal:


# definicja klasy
class Animal:

    nazwa = "fauna"  # atrybut klasowy, czyli odnosi się do każdego elementu/instancji klasy
    licznik =0

# przypisywanie metod

    def __init__(self,gatunek): # inicjalizacja , tu umieszczamy wszystkie atrybuty nawet z wartością none
                                # jeżeli mają się pojawić poniżej w metodach
                                # pierwszy argument w nawiasie wskazuje na instancję

        self.gatunek = gatunek  # self oznacza że odnosimy się do konkretnej instacji , tu mamy atrybuty instancji obiektu
        self.zwieksz_licznik()
        self.stan ='nic nie robi' #atrybut instancji

    def __str__(self):  #dzięki tej przy wywołaniu print(azor) łądnie wyświetla nazwę
        return "Animal"

    def idz(self):
        self.stan = 'idzie'

    def stoj(self):
        self.stan = 'stoi'

    @classmethod
    def zwieksz_licznik(cls):
        cls.licznik += 1

### dziedziczenie ,poniżej leniwe zwierzęta dziedziczą z klasy Animal

class LeniweZwierzeta(Animal):
    def idz(self):
        self.stan = 'lezy'
        print('chyba żartuejsz')


### poniżej przypisanie obiektu (instancji) do klasy / tworzenie instacji danej klasy

azor = Animal("Canis Familiaris")
rudolf = Animal("Rangifer tarandus")

print(type(azor))  #main w wywołanym w kodz
print(azor)
print(azor.gatunek) # wypisanie atrybutu
print(rudolf.gatunek)


print(Animal.licznik)

print(dir(azor))
azor.idz()
print(azor.stan)

garfield = LeniweZwierzeta('Felis catus')

print(dir(garfield))
garfield.idz()

LeniweZwierzeta.idz(garfield)
print(garfield.stan)
print(azor.stan)