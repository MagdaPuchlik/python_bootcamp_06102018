tupla = (11,24,2,5,6)

# print(len(tupla))

m_min=0
m_max=0

for x in range(1,len(tupla)):
    x_min = min(tupla[x:])
    x_max = max(tupla[x:])
    if tupla[x] == x_min:
        m_min =x
    if tupla[x]== x_max:
        m_max =x

    if tupla[m_min] == tupla[x]:
        continue
    else:
        tupla[x] ==x_min
        tupla[m_min]== x_max
    print(tupla)


