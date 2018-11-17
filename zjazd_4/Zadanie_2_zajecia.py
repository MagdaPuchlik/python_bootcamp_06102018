import json
import urllib.request
import sys


weather

def get_location_id(location_name):

    url =f"https://www.metaweather.com/api/location/search/?query={location_name}"
    with urllib.request.urlopen(url) as f:
        results = json.loads(f.read())
        if results:
            return results[0]['woied']





if __name__= "__main__":
    location_id = get_location_is(sys.argv[1])
    weather= get_location_weather(location_id)
    print(weather['consolidated_weather'])