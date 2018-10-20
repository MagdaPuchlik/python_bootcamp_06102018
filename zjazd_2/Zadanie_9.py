# # moj sposob
#
# produkt1 = {"nazwa":"ziemniaki","cena":0.99}
# produkt2 = {"nazwa":"marchewka","cena":2.99}
# produkt3 = {"nazwa":"pomidory","cena":5.99}
#
# produkty = [produkt1, produkt2,produkt3]
#
# cena =0
#
# for p in produkty:
#     print(p['nazwa'])
#     ilosc =int(input("podaj ilosc produktu:"))
#     cena1 = (p['cena']) * ilosc
#  #   cena = cena + cena1
#     print(f"Cena za produkt: {cena1}")
#     cena = cena + cena1
#     print(f"cena za calosc:{cena}")

pass

#    sposob z zajec

produkty={"ziemniaki":2, "bataty":4, "pomidory":6}
magazyn={"ziemniaki":10, "bataty":10, "pomidory":10}

koszyk=[]
rachunek = 0

while True:
    print("-"*40) #linia oddzielająca
    print("Nasz zielnik oferuje:")

    for produkt in produkty:
        print(f'-{produkt} - {produkty[produkt]} PLN')
    komenda=input(f"co chcesz zrobic?: [k]upić,[koniec] by przerwać zakupy")

    if komenda == 'koniec':
        break

    prod_wybrany = input("Co chcesz kupić?")

    if prod_wybrany not in produkty:
        print("Nie mamy takiego produktu!")
        continue

    ile_wybrany = float(input(f"ile chcesz kupić: [{prod_wybrany}]"))

    if ile_wybrany > magazyn[prod_wybrany]:
        print("nie mamy takiej ilosci w magazynie")
        decyzja = input(f"czy zwiększyc magazyn ? : [t]ak,[n]ie")

        if decyzja == 't':
            produkt_do_dadania = input("Jaki pordukt chcesz dodać?")

                if produkt_do_dadania not in produkty:
                        magazyn[produkt_do_dadania]=0
                        cena_nowego_prod = float(input("za ile to sprzedajemy?"))
                        produkty[produkt_do_dadania]=cena_nowego_prod

            ile_prod_dodajemy = float(input("ile tego dodać?"))
            magazyn[produkt_do_dadania]+=ile_prod_dodajemy

        else: continue

    else: magazyn[prod_wybrany] = magazyn[prod_wybrany]-ile_wybrany

    koszt = produkty[prod_wybrany]*ile_wybrany


    koszyk[prod_wybrany]=koszyk.get(prod_wybrany,0)+koszt
                #sprawdzam czy wybrany produkt był juuż wcześniej w koszyku , jezeli nie był to przypisumey mu wartość 0
                # natomiast jeżeli był do zostanie odnależiony i bieżacy koszt zostanie dodany na pozyji rachunku do
                # wcześniejszego


    rachunek += koszt
    koszyk[prod_wybrany] = koszt


print('='*40)

print(f"za zakupy zapłacisz:")
for product in koszyk:
    print(f" - {product} - {koszyk[product]} - PLN")
    suma+= koszyk[product]

print('='*40)
print(f"Suma:{suma} PLN")