import random


#random.seed(3) # każdy uzytkownik pYthona wpisując tę trójkę będzie miał taką samą liczbę

print(random.random())
print(random.randrange(1,100))
print(random.randint(1,100))

pets=["cat","dog","fish","kuna"]

print(random.choice(pets))