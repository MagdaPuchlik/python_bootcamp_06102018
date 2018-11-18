import re

text=()

with open("input.txt") as f:
    text = f.read()


#znalezienie kodów pocztowych
pattern=re.compile("^\d{2}-\d{3} | \d{2}-\d{3} | \d{2}-\d{3}$")

# ^ oznacza początek tekstu (że szukamy czegoś od samego początku)
# | oznacza lub
# $ oznacza koniec tekstu (że to czego szukmy jest na końcu)
# . oznacza dowolny znak
# \. oznacza kropkę (slashem) poprzedza się znaki specjalne, w tym kropkę

print("Kody pocztowe:" + "," .join(pattern.findall(text)))

zbior1 = set()

pattern2=re.compile("[\w+-\w+\@\w+\.\w+\.\w+")

# alternatywa [\w\.-]+@[\w\.]+
# [\w\.-]+ takie wyrażenie oznacza że posuzkiwana jest grupa znaków (w nawiasie kwadratowym) a znak + oznacza że może powtórzyć się wiele razy

for patt1 in pattern2.findall(text):
    zbior1.add(patt1)
print("Emaile:"+",".join(pattern2.findall(text)))
print(f"ilosc elementow:{len(zbior1)}")


pattern3=re.compile("\d{2}.\w{3}.\d{4}")
print("Daty: " +",".join(pattern3.findall(text)))