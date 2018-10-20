tekst = input("podaj napis:")

slownik={}

for litera in tekst:

    # if litera not in slownik:
    #     slownik[litera]=1
    # else:
        slownik[litera] = slownik.get(litera,0)+1


for litera in slownik:
    print(f" - '{litera}' występuje {slownik[litera]} razy ")