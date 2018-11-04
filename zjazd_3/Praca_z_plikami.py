
#dawnyt sposób otwierania plikó w Pythonie
    # wada - trzeba pamiętać o tym że plik trzeba zamknąć
file = open("Dane/emails.txt")
print(file.read())
file.close()


#specjalny zapis > KONTEKST MENEDZERA

with open("Dane/emails.txt") as f:
    print(f) # < to wcięcie powoduje że plik jednocześnie jest zamknięty, czyli działą jedynie pod wcięciem

# w tym przypadku otwarcie pliku nie zadziała
print(f.read())

with open("Dane/emails.txt") as f:
    print(f.read())

with open("Dane/nowy_plik.txt",'w',encoding='utf-8') as f: # litera "w" pozwala na zapisanie pliku
    f.write('jakis tekst')                                  # litera "r" pozwala jedynie na odczytanie pliku

with open("Dane/nowy_plik.txt",'r',encoding='utf-8') as f:
    print(f.read())