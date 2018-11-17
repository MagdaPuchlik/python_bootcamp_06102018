import json
import urllib.request

with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/A?format=json") as f:
    kursy = json.loads(f.read())

rates = kursy[0]['rates']
for r in rates:
    print(f"-{r['code']} - {r['mid']}")

print(rates)

kwota = int(input(f"Jaką kwotę chcesz wymienić"))
waluta = str(input(f"Jaką walutę chcesz wymienić"))

for r in rates:
    if r['code'] == waluta:
        wynik = r['mid']*kwota

        print(wynik)