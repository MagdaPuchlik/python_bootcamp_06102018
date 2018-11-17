import json
import urllib.request

miasto = str(input("dla jakiego miasta chcesz podać pogodę"))

with urllib.request.urlopen(f"https://www.metaweather.com/api/location/search/?query={miasto}") as f:
    dane_miasta = json.loads(f.read())

    print(dane_miasta)

    woeid = int(dane_miasta[0]['woeid'])

with urllib.request.urlopen(f"https://www.metaweather.com/api/location/{woeid}/") as f:
    lokalizacja = json.loads(f.read())

    print(lokalizacja)