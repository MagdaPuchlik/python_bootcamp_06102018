a=1
suma=0
dni =7

min_ = None
max_= None

while a<=dni:
    temp = int(input("podaj temperature:"))
    suma=suma+temp

else:
    if numer_dnia==1:
        min_=temp
        max_=temp
    else:
        if temp < min_:
            min_ = temp
        if temp > max_:
            max_=temp

    dni = dni + 1

srednia = suma/dni
print(srednia)