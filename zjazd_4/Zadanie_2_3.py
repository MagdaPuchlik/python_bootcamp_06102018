import json
import urllib.request


def pogoda(miasto):

    dane_miasta={}
    lokalizacja={}

    with urllib.request.urlopen(f"https://www.metaweather.com/api/location/search/?query={miasto}") as f:
        dane_miasta = json.loads(f.read())

    woeid = int(dane_miasta[0]['woeid'])

    with urllib.request.urlopen(f"https://www.metaweather.com/api/location/{woeid}/") as f:
        lokalizacja = json.loads(f.read())

    return dane_miasta, lokalizacja


print(pogoda("London"))