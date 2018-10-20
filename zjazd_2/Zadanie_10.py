tekst = input("podaj napis:")

slownik=[]

for litera in tekst:
    if slownik[litera] not in slownik:
        slownik[litera]=1
    else:
        slownik[litera] = slownik.get(litera,1)+1

