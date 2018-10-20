
zbior=set({})
liczby = set(range(2,101,2))

# for x in range (1, 100):
#     if x%2 ==0:
#         liczby.add(x)

while True:
    liczba = int(input("Podaj liczbę:"))

    zbior.add(liczba)

    komenda=input(f"co chcesz zrobic?: [w]isywac,[k]oniec by przerwać")

    if komenda == 'k':
        break

print(liczby)
print(zbior)

print(f" czesc wspolna zbiorów to: {zbior.intersection(liczby)}")
print(f"jest to łacznie: {len(zbior.intersection(liczby))} liczb")