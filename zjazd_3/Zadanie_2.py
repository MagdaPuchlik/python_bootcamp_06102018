class Employee:

    def __init__(self, imie, nazwisko,stawka):
        self.imie = imie
        self.nazwiko = nazwisko
        self.stawka = stawka



def test_employee():
    pracownik = Employee('Jan','Nowak',100.0)
    assert pracownik.imie == 'Jan'
    assert pracownik.nazwisko == 'Nowak'
    assert pracownik.stawka == 100.0


