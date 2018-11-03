class Employee:

    def __init__(self, imie, nazwisko,stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.register_time=0
        self.pay_salary()

    def czas(self,hours):
        self.register_time = hours

    def pay_salary(self):
        if self.register_time ==0:
            return 0
        elif self.register_time <8:
            to_pay = self.register_time * self.stawka
            self.register_time =0
            return to_pay
        else:
            to_pay2 = (self.register_time - 8)*self.stawka*2 +800
            self.register_time = 0
            return to_pay2


def test_employee():
    pracownik = Employee('Jan','Nowak',100.0)
    assert pracownik.imie == 'Jan'
    assert pracownik.nazwisko == 'Nowak'
    assert pracownik.stawka == 100.0


def test_pay_salary1():
    pracownik = Employee('Jan', 'Nowak', 100.0)
    assert pracownik.pay_salary() == 500


def test_pay_salary2():
    pracownik = Employee('Jan', 'Nowak', 100.0)
    assert pracownik.pay_salary() == 1200

def test_pay_salary3():
    pracownik = Employee('Jan', 'Nowak', 100.0)
    assert pracownik.pay_salary() == 0