
lista =[10,89,-5,4,8,55,33,56,42,-9,2,11]

print(lista)

a=0
b=0
print(min(lista))
print(max(lista))

for el in lista:
    a = a+1
    if el == max(lista):
        break
for el in lista:
    b= b+1
    if el == min(lista)
        break



#   inny sposób

# for i in indeksy:
#     if min_i ==None or liczby[i] < liczby[min_i]:
#         min_i =i
#     if max_i ==None or liczby[i] > liczby[max_i]:
#         max_i =i


#  liczby[min_i] , liczby[max_i] = liczby[min_i],liczby[max_i]


lista[a-1]=min(lista)
lista[b-1]=max(lista)

print(lista)