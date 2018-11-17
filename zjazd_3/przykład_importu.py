# import Zadanie_6
#
# #u góry polecenie daje błąd jeżeli folder zjazd_3 gdzie jest ten plik nie jest oznaczony jako "sources root"
#
#
#
# v1 = Zadanie_6.Vector(1,2)
# v2 = Zadanie_6.Vector(1,2)
#
# #dzięki zaimportowaniu mmodułu (zadanie6) można się odwołać do jego elementów z krropką
#
# print(v1+v2)



from Zadanie_6 import Vector

#tu importuję nie cały moduł ale tylko klasę
# dzięki temu póżniej do klasy mogę się odwoływać w poniższy sposób (bez uzywania nazwy modułu), tylko bezpośrednio do klasy

# v1 = Vector(1,2)
# v2 = Vector(1,2)


from Zadanie_6 import *

# tu importuję wszystko ale tego się nie robi , ponieważ może to nadpisywać /przysłaniać obiekt np. słownik czy inne obiekty

 można się odwoływać do obiketów poprzez aliasowanie ich

#np
#from Zadanie_6 import Vector, dict as pisany_slownik
#pusty_slownik = dict()
# print(type(pusty_slownik))

# moduł to każdy plik po lewej, folder modułów (plików) to paczka, w paczce musi byc plik init by folder był nazywany paczką