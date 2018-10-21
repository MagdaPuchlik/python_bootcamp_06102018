def podzielna_przez_2(x):
    return x%2 ==0

print(podzielna_przez_2(12))
print(podzielna_przez_2(11))

y=lambda x:x%2 ==0
print(y(2))
print(y(5))

#lub

# z = podzielna_przez_2(x)
# print(z(2))
# print(z(4))


def podzielna_przez_3(x):
    return x%3 ==0
    
def wybierz(dane, warunek):

    out =[]
    for element in dane:
        if warunek(element):
            out.append(element)
    return(out)

lista =[1,2,3,4,5,6,7,8,9,122,123]
print(wybierz(lista,podzielna_przez_2))
print(wybierz(lista),lambda x:x%3 ==0)
print(wybierz(lista,podzielna_przez_3)) # nie podaję tu nawiasów ponieważ nazwa funkcji umieszxczana jest w wyższej pętli
                                    # zamiast słowa warunek

