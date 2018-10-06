a=int(input("Podaje liczbę a:"))
b=int(input("Podaj liczbę b:"))
oper = str(input("Podaj rodzaj operacji:"))

suma = a+b
roz = a-b
mno = a*b
dziel =a/b

if oper=="+":
    print(f"wynik:{suma}")
elif oper =="-":
    print(f"wynik:{roz}")
elif oper=="*":
    print(f"wynik:{mno}")
elif oper=="/":
    print(f"wynik:{dziel}")
else:
    raise ValueError("Nieprawidłowa wartość dla parametru typ operacji")


#można stosować słowo tymczasowe pass , które pozwala przejść dalej w komendzie (pozwala na twoprzenie szkieletu komnedy)
#np
# if oper=="+":
#       pass
# elif