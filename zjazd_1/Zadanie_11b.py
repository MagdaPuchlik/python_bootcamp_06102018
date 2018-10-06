x=int(input("Podaj pozycję gracza X:"))
y=int(input("Podaj pozycję gracza Y:"))

krawedz = int(input("Podaj krawedz:"))
margines = int(input("Podaj margines w% planszy:"))
margines = margines/100

marg2 = margines*krawedz
marg3 = krawedz*(1-margines)

if x<=marg2 and y<=marg2:
    print("w lewym dolnym rogu")
elif x>krawedz or y> krawedz or x<0 or y <0:
    print("poza obszarem plnaszy")
elif x<=marg2 and  marg2 <y< marg3:
    print("w lewej krawedzi")
elif x<=marg2 and marg3<= y <= krawedz:
    print("w lewym górnym rogu")
elif marg2 <x< marg3 and marg3 <= y :
    print("w gornej krawedzi")
elif marg3<= x <=krawedz and marg3<=y:
    print("w prawym górnym rogu")
elif marg3 > y >= marg2 and marg3 <= x <= krawedz:
    print(" w prawej krawedzi")
elif marg3 <= x <= krawedz and y<=marg2:
    print("w lewym dolnym rogu")
elif marg2<x<marg3 and  y <= marg2:
    print("w gornej krawedzi")
else:
    print("w centrum")