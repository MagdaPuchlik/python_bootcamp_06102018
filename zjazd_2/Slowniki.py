# Slowniki

my_dict ={
    "pierwsza":"a",
    "druga":"b"

}

my_dict['trzecia']='c' ## dodanie elementu do slownika

print(type(my_dict))
print(my_dict["pierwsza"]) #zwraca wartosc dla pierwszego elementu
print(my_dict.items()) #zwraca zawartosc slownika, nieuporządkowana, mogą byc w róznej kolejności zwracane
print(my_dict.keys()) #drukuje tylko klucze, czyli pierwsza kolumnę ze słownika
print(my_dict.values()) #drukuje tylko wartości ze slownika


produkt1 ={'nazwa':'Koper', "cena":3}
produkt2 ={'nazwa':'Kasza', "cena":1.99}

produkty = [produkt1,produkt2] #polaczenie dwoch elementow w slowniki

print("Produkty w lodowce:")
for p in produkty:
    print(p['nazwa'])
    
for k in produkt1:
    print(k,produkt1[k])