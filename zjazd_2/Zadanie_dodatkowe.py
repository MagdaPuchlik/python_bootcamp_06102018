# tupla = [11,24,2,5,6]
#
# # print(len(tupla))
#
#
# for x in range(0,len(tupla)):
#     x_min = min(tupla[x:])
#     x_max = max(tupla[x:])
#     if tupla[x] == x_min:
#         z = x
#     if tupla[x]== x_max:
#         y = x
#
#     if tupla[z] == tupla[x]:
#             continue
#         else:
#             tupla[x] ==x_min
#             tupla[y]== x_max
#     print(tupla)


# z zajęc

liczby= [11,24,2,5,6]

print(f"Przed:{liczby}")

for i in range(len(liczby)):
    index_minimum =i
    print('i',i,'liczby:',liczby[i:])
    for j in range(i+1,len(liczby)):
        if liczby[j] < liczby[index_minimum]:
            index_minimum = j
    liczby[i], liczby[index_minimum] = liczby[index_minimum],liczby[i]

print(f"Po:{liczby}")