m_A = str(input("Podaj nazwę miasta A:"))
m_B = str(input("Podaj nazwę miasta B:"))
pytanie = (f"Dystans  {m_A} - {m_B}:")

odl = int(input(pytanie))
cena = 4.55
spal = 5.5
koszt = int(odl / 100 * cena * spal)

out = F"""

Miasto A :{m_A}
Miasto B: {m_B}
Dystans {m_A} - {m_B}: {odl}
Cena paliwa: {cena}
Spalanie na 100 km: {spal}

Koszt paliwa na trasie {m_A}-{m_B} to {koszt} PLN

"""

print(out)
