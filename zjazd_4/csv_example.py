import csv

wyniki=[]


with open("dane/titanic_train.csv") as csvfile:
    data = csv.reader(csvfile,delimiter=",")
    dlugosci ={}
    for row in data:
        dlugosci[row[1]]=dlugosci.get(row[1],0)+1
    print(dlugosci)


with open("dane/titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile,delimiter=",") #DictReader pozwala na zmianę w słownik
    dlugosci ={}
    for row in data:
        dlugosci[row['Survived']]=dlugosci.get(row["Survived"],0)+1
    przezylo = dlugosci['1']
    zginelo = dlugosci['0']

    wyniki.append(["przezylo z ogolu",round(100*przezylo/(przezylo+zginelo),2)])
    wyniki.append(["zginelo z ogolu",round(100*zginelo/(przezylo+zginelo),2)])
    print(f"przezylo z ogolu {round(100*przezylo/(przezylo+zginelo),2)}")
    print(f"zginelo z ogolu {round(100*zginelo/(przezylo+zginelo),2)}")

with open("dane/titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")  # DictReader pozwala na zmianę w słownik
    kobiety={}
    for row in data:
        if row['Sex']=='female':
            kobiety[row['Survived']] = kobiety.get(row["Survived"], 0) + 1
    przezylo = kobiety['1']
    zginelo = kobiety['0']

    wyniki.append(["przezylo z kobiet",round(100*przezylo/(przezylo+zginelo),2)])
    wyniki.append(["zginelo z kobiet",round(100*zginelo/(przezylo+zginelo),2) ])

    print(f"przezylo z kobiet {round(100*przezylo/(przezylo+zginelo),2)}")
    print(f"zginelo z kobiet {round(100*zginelo/(przezylo+zginelo),2)}")

with open("dane/titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")  # DictReader pozwala na zmianę w słownik
    mezczyzni={}
    for row in data:
        if row['Sex']=='male':
            mezczyzni[row['Survived']] = mezczyzni.get(row["Survived"], 0) + 1

    przezylo = mezczyzni['1']
    zginelo = mezczyzni['0']

    wyniki.append(["przezylo z mezczyzn",round(100*przezylo/(przezylo+zginelo),2)])
    wyniki.append(["zginelo z mezczyzn",round(100*zginelo/(przezylo+zginelo),2) ])


    print(f"przezylo z mezczyzn {round(100*przezylo/(przezylo+zginelo),2)}")
    print(f"zginelo z mezczyzn {round(100*zginelo/(przezylo+zginelo),2)}")

with open("dane/titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")  # DictReader pozwala na zmianę w słownik
    how_many_woman=0
    sum_woman_age =0
    how_many_man=0
    sum_man_age =0
    unique_age_values = set()

    for row in data:
        unique_age_values.add(row['Age'])
        if row["Age"]!="":
            if row['Sex']=='female':
                how_many_woman +=1
                sum_woman_age += float(row["Age"])
            if row['Sex']=='male':
                how_many_man +=1
                sum_man_age += float(row["Age"])

    wyniki.append(["Średnia wieku kobiet to", round(sum_woman_age/how_many_woman,2)])
    wyniki.append(["Średnia wieku mezczyzn to", round(sum_man_age/how_many_man,2)])

    print(f"Średnia wieku kobiet to {round(sum_woman_age/how_many_woman,2)}")
    print(f"Średnia wieku mezczyzn to {round(sum_man_age/how_many_man,2)}")


#tworzenie pliku csv z raportem, z listą wypisnaych wyników w liście wyniki
with open("report.csv","w", encoding='utf-8',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(wyniki)

