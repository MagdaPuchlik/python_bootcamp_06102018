import tkinter


def sumuj():
    #pobieranie wartości z okienek
    a = float(a_entry.get()) #pobranie z przestrzeni globalnej zmiennych
    b = float(b_entry.get())
    wynik.configure(text=a+b)


root = tkinter.Tk() # główny obiket do któtego przypinaym inne obiekty

a_label = tkinter.Label(master=root, text="Parametr a") #master=root oznacza że root jest elementem nadrzędnym (parent)
a_label.pack()

a_entry = tkinter.Entry(master=root) #tworzenie okienka
a_entry.pack() #przypięcie, sprawia że się coś pojawia, powinnno się pojawić po każdym elemencie

b_label = tkinter.Label(master=root, text="Parametr b") #master=root oznacza że root jest elementem nadrzędnym (parent)
b_label.pack()

b_entry = tkinter.Entry(master=root)
b_entry.pack()

wynik_label = tkinter.Label(master=root, text="Wynik")
wynik_label.pack()

wynik = tkinter.Label(master=root, text="-")
wynik.pack()

policz_button = tkinter.Button(master=root, text="Policz", command=sumuj)
policz_button.pack()


root.title("Sumator") # nadanie nazwy dla "okienka"
root.mainloop() #główna pętla wychwytująca działania, jeżeli umieścimy coś po tym miejscu wówczas , to co jest po jest wykonane po zamknięciu wyżej utworzonego okienka
