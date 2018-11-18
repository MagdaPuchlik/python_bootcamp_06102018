import datetime

now=datetime.datetime.today()
print(now)

print(now.year)
print(now.weekday())

x = datetime.datetime.strptime("2018-11-18", "%Y-%m-%d")
print(x)

my_birthday = datetime.datetime(1989,3,8)
print(my_birthday.weekday())
# dzień tygodnia od daty moich urodzin
print(now>my_birthday)

#poniżej wywołanie
for i in range(20):
    print(now + datetime.timedelta(hours=i))

my_birthday_2 = datetime.datetime(1990,2,15)
print(my_birthday_2.weekday())

roznica = now - my_birthday

print(roznica.days)