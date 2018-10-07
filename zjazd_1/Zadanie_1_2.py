
suma =0
liczby =[]

while len(liczby) <10:

    liczba = int(input("podaj liczbę:"))
    liczby.append(liczba)

    srednia = sum(liczby)/len(liczby)

    print(liczby)
    print(f"Podałeś już:{sum(liczby)} liczb \nŚrednia: {srednia}")


    if len(liczby)==10:
        print("Podałeś 10 liczb")
        break