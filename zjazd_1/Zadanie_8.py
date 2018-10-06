szer = int(input("Podaje szerokość opakowania:"))
dl = int(input("Podaje długość opakowania:"))
gl = int(input("Podaj długość opakowania"))


obj = szer * dl *gl

if obj > 1000:
    print("Objętość jest większa niż 1L")
else:
    if obj == 1000:
        print("Objętość jest równa 1L")
    else:
        print("Objętość jest mniejsza niż 1L")
