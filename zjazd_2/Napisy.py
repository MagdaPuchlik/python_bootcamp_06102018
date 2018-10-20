napis = "to jest jakis napis"

print( "a" in napis) #szukanie jednego ciągu znaków w innym , zwraca wartość false lub true
print ("mama" in napis)

for litera in napis:
    print(litera)

print(dir(napis)) #mogę odczytąć jakie funkcje są do zastosowania z napisem