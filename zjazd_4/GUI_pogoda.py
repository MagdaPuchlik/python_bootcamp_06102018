import tkinter
import json
import urllib.request
import sys
from collections import namedtuple


Weather = namedtuple("Weather", ["location", "temperature", "air_pressure", "humidity"])

def nazwa_miasta():
    location_name = miasto.get()
    location_id = get_location_id(location_name)
    weather = get_location_weather(location_id)
    pogoda = print_weather(weather)


def get_location_id(location_name):
    url = f"https://www.metaweather.com/api/location/search/?query={location_name}"
    with urllib.request.urlopen(url) as f:
        results = json.loads(f.read())
        if results:
            return results[0]['woeid']


def get_location_weather(location_id):
    url = f"https://www.metaweather.com/api/location/{location_id}"
    with urllib.request.urlopen(url) as f:
        results = json.loads(f.read())

        location = results['title']
        temp = results['consolidated_weather'][0]['the_temp']
        humidity = results['consolidated_weather'][0]['humidity']
        air_pressure = results['consolidated_weather'][0]['air_pressure']

        weather = Weather(location, temp, air_pressure, humidity)
        return weather

def print_weather(weather):
    print(f"""
Pogoda w lokalizacji: {weather.location}
 - Temperatura: {weather.temperature}
 - Ciśnienie: {weather.air_pressure}
 - Wilgotność: {weather.humidity}
 """)

miasto = tkinter.Label(master=root, text="Podaj miasto")
miasto.pack()

policz_button = tkinter.Button(master=root, text="Pokaż pogodę", command=Oblicz_koszt)
policz_button.pack()

root = tkinter.Tk()