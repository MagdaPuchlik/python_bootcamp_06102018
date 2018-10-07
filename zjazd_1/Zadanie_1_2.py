
suma =0

while True:

    liczba = int(input("podaj liczbę:"))
    liczby =[]
    liczby.append(liczba)


    suma = suma + liczba
    srednia = suma/sum(liczby)

    print(liczby)
    print(f"Podałeś już:{sum(liczby)} liczb \nŚrednia: {srednia}")


    if sum(liczby)==10:
        print("Podałeś 10 liczb")
        break