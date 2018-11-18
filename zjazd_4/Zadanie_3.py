import tkinter


def Oblicz_koszt():
    k = float(km.get())
    s = float(spalanie.get())
    c = float(cena.get())
    koszt.configure(text=(k/100)*s*c)


root = tkinter.Tk()

km = tkinter.Label(master=root, text="Ilość km")
km.grid(row=0, column=0)

km = tkinter.Entry(master=root)
km.grid(row=0, column=1)

spalanie = tkinter.Label(master=root, text="Spalanie na 100 km")
spalanie.grid(row=1, column=0)

spalanie = tkinter.Entry(master=root)
spalanie.grid(row=1, column=1)

cena = tkinter.Label(master=root, text="Cena paliwa za 1 l")
cena.grid(row=2, column=0)

cena = tkinter.Entry(master=root)
cena.grid(row=2, column=1)

koszt = tkinter.Label(master=root, text="Koszt paliwa")
koszt.grid(row=3, column=0)

koszt = tkinter.Label(master=root, text=" podaj powyższe wartości")
koszt.grid(row=3, column=1)

policz_button = tkinter.Button(master=root, text="Oblicz łączny koszt", command=Oblicz_koszt)
policz_button.grid(row=4, column=1)


root.title("Kalkulator kosztów paliwa")
root.mainloop()