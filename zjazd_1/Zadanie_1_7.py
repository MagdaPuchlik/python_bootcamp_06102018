tekst = str(input("Podaj dowolny teskt:"))

il_a=0
il_e=0
il_i=0
il_o=0
il_u=0
il_y=0


for i in range(len(tekst)):
    if tekst[i] =="a":
        il_a +=1
    elif tekst[i] =="e":
        il_e +=1
    elif tekst[i] =="i":
        il_i +=1
    elif tekst[i] =="o":
        il_o +=1
    elif tekst[i] =="u":
        il_u +=1
    elif tekst[i] =="y":
        il_y +=1

out=f"""
Podsumowanie
litery a: {il_a}
litery e: {il_e}
litery i: {il_i}
litery o: {il_o}
litery u: {il_u}
litery y: {il_y}

"""

print(out)

#inny sposób

#tekst = str(input("Podaj dowolny teskt:"))
# samogloski ='aieouy'

# ile_samoglosek=0

# for znak in tekst:
#     if znak in samogloski:
#         ile_samoglosek=+1