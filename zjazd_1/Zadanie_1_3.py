lista =[10,89,-5,4,8,55,33,56,42,-9,2,11]

#for licznik, zmienna in enumerate (lista,100)
   # print(licznik,zmienna**2)
ujemne = 0
dodatnie=0

for liczba in lista:
    if liczba < 0:
        ujemne += 1
    if liczba > 0:
        dodatnie +=1


print(f"Masz {ujemne} licz ujemnych oraz {dodatnie} liczb dodatnich")


for el in lista:
    if el < 0:
        dodatnie.append(el)
    elif el >0:
        ujemne.append(el)