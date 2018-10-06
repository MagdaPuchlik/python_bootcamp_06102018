x=int(input("Podaj pozycję gracza X:"))
y=int(input("Podaj pozycję gracza Y:"))

krawedz = int(input("Podaj krawedz:"))
margines = int(input("Podaj margines planszy:"))


if x<=margines and y<=margines:
    print("Gracz znajduje się w lewym dolnym rogu")
elif x>krawedz or y> krawedz or x<0 or y <0:
    print("Gracz znajduje się poza obszarem plnaszy")
elif x<=margines and  margines <y< (krawedz-margines):
    print("gracz znajduje się w lewej krawedzi")
elif x==margines and (krawedz-margines)<= y <= krawedz:
    print("gracz znajduje się w lewym górnym rogu")
elif margines<x<(krawedz-margines) and (krawedz-margines)< y <= krawedz:
    print("gracz znajduje się w gornej krawedzi")
elif (krawedz-margines)<= x <=krawedz and (krawedz-margines)<=y<=krawedz:
    print("Gracz znajduje się w prawym górnym rogu")
elif krawedz-margines> y >= margines and (krawedz - margines) <= x <= krawedz:
    print("gracz znajduje się w prawej krawedzi")
elif (krawedz - margines) <= x <= krawedz and y<=margines:
    print("Gracz znajduje się w lewym dolnym rogu")
elif margines<x<(krawedz-margines) and  y <= margines:
    print("gracz znajduje się w gornej krawedzi")
else:
    print("Gracz znajduje się w centrum")