from random import randint

def losowanie(dol, gora):

    return randint(dol,gora), randint(dol,gora)

g_x , g_y = losowanie()
s_x , s_y = losowanie()

a=0

def min_liczba_ruchow(g_x,g_y,s_x ,s_y):
   return abs(g_x - s_x) + abs(g_y - s_y)


# print(f"Położenie gracza: x = {g_x}, y = {g_y}")
# print(f"Położenie skarbu: x = {s_x}, y = {s_y}")

def zmiana_pozycji_gracza(g_y,g_x):

    ruch = str(input("Podaj w jakim kierunku [w/s/a/d] ma przesunąć się gracz:"))

    a=a+1

    if ruch == "w":
        g_y=g_y+1
    elif ruch == "s":
        g_y = g_y-1
    elif ruch == "a":
        g_x=g_x-1
    elif ruch == "d":
        g_x=g_x+1

    return g_x,g_y


def sprawdzenie()


    print(f"Położenie gracza: x = {g_x}, y = {g_y}")

    if g_x>10 or g_y>10 or g_x <1 or g_y <1:
        print("Gracz poza planszą wyjście z gry")
        break

    if g_x == s_x and g_y == s_y:
        print("Skarb został odnaleziony, gratulacje!")
        break

    l_ruchow_po = abs(g_x - s_x) + abs(g_y - s_y)

    if l_ruchow_po > min_liczba_ruchow(g_x,g_y,s_x ,s_y):
        print(f"Oddalasz się od skarbu, wykonałeś:{a} ruchów")
    elif l_ruchow_po <= min_liczba_ruchow(g_x,g_y,s_x ,s_y):
        print(f"Jesteś coraz bliżej skarbu, wykonales: {a} ruchów")

    if l_ruchow_po > 2* min_liczba_ruchow(g_x,g_y,s_x ,s_y):
        g_x, g_y = losowanie()
        s_x, s_y = losowanie()
        min_liczba_ruchow(g_x, g_y, s_x, s_y)