import json

# tworze pythononyw obiekt

meble =["krzesło","szafa","komoda","stół"]
print(type(meble))

meble_as_json = json.dumps(meble) #json tworzy nam z listy string
print(type(meble_as_json))

print(meble_as_json)

odczytane_z_jsona_meble =json.loads(meble_as_json)
print(type(odczytane_z_jsona_meble))
print(odczytane_z_jsona_meble)

with open("meble.json","w")as f:
    json.dump(meble,f)

# dumps
# dump : potrzebuje dwóch parametrów, tworzy plik jsonowy w pythonie ,  przy pomocy nazwy zmiennej oraz nazwy pliku

# load > odczytuje obiekt juz pythonowy
# loads

with open("meble.json") as f:
    meble = json.load(f)
    print(meble)

with open("meble.json") as f:
    meble = json.load(f)
    meble.append("taboret")

print(meble)

# with open("meble.json", "w") as f: #w tym miejscu nadpisuję plik
#     json.dump(meble,f)