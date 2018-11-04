login = {}
user_total_time = {}

with open("Dane/logs.txt") as f:
    for line in f:
        user,typ,czas = line.split(';') # podział pliku według znaku ";"
        czas = int(czas)
        if typ == 'LOGIN':
            login[user]=czas
        if typ=='LOGOUT':
            user_total_time[user] = user_total_time.get(user,0)+czas - login[user]

def sort_key(x):
    return x[1]


print("czas przebywania w systemie:")
for item in sorted(user_total_time.items(), key = sort_key, reverse=True):
    print(item)

    # sortuję przy pomocy funkcji sort_key

#alterantywa dla    key = sort_key
#                   key = lambda x:x[1]