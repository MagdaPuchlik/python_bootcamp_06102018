tekst = str(input("Podaj tekst:"))

gdzie_m: int =0
gdzie_w =0
dl =0
a=0


for i in range(len(tekst)):
    if tekst[i]=="<":
        gdzie_m =  i
    elif tekst [i]=='>':
        gdzie_w = i

if gdzie_m ==0 and gdzie_w ==0:
    print("Nie ma nawiasów")
    print(f"{gdzie_m},{gdzie_w}")
else:
    dl = gdzie_w - gdzie_m-1
    print(f"Dlugosc tekstu to: {dl}")
