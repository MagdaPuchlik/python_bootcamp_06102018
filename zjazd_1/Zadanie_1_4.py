
podzielne=[]

for i in range(101):

    if i%3==0 or i%5==0:
        podzielne.append(i)
print(podzielne)
print(f"Wystąpilo:{len(podzielne)}")