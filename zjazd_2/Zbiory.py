#podobne do słowników, ale zawierają jedynie klucze bez wartości do nich przypisanych
# zachopwuje przetrzymuje jedynie unikalne wartości

zbior = {1,2,3,4,1}

for i in zbior:
    print(i)

a = {1,2,3}
b= {3,4,5}

print(a|b) # suma
print(a-b) # roznica
print(a.difference(b))
print(a&b) # cześć wspólna
print(a.intersection(b))
print(a^b) # różnica symatryczna > wszystko to co nie jest częścią wspólną
print(a.symmetric_difference(b))

print(dir(a))