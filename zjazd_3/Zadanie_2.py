class Employee:

    def __init__(self, imie, nazwisko,stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.time = 0
        self.pay_salary()

    def register_time(self,hours):
        self.time += hours

    def pay_salary(self):
        if self.time ==0:
            return 0
        elif self.time <=8:
            to_pay = self.time * self.stawka
            self.time =0
            return to_pay
        else:
            to_pay = (self.time - 8)*self.stawka*2 +800
            self.time = 0
            return to_pay

    def __str__(self):
        return f"Pracownik {self.imie} {self.nazwisko}"


class PremiumEmployee(Employee):

    def __init__(self, imie, nazwisko,stawka):
        super().__init__(imie, nazwisko, stawka) #pobieram wszystko z inita klasy z której dziedziczę czyli z Employee
        self.ekstra = 0 #dodaję brakującą metodę

    def give_bonus(self, bonus):
        self.ekstra = bonus

    def pay_salary(self):
        to_pay = super().pay_salary()
        return to_pay + self.ekstra

class Company:

    def __init__(self,nazwa):
        self.nazwa = nazwa
        self.employees = set()

    def add_employee(self,employee):
        self.employees.add(employee)

    def size(self):
        return len(self.employees)

    def pay_all_salary(self):
        sum_ =0
        for e in self.employees:
            sum_ += e.pay_salary()
        return sum_


def test_employee():
    pracownik = Employee('Jan','Nowak',100.0)
    assert pracownik.imie == 'Jan'
    assert pracownik.nazwisko == 'Nowak'
    assert pracownik.stawka == 100.0


def test_pay_salary1():
    pracownik = Employee('Jan', 'Nowak', 100.0)
    pracownik.register_time(5)
    assert pracownik.pay_salary() == 500


def test_pay_salary2():
    pracownik = Employee('Jan', 'Nowak', 100.0)
    pracownik.register_time(10)
    assert pracownik.pay_salary() == 1200

def test_pay_salary3():
    pracownik = Employee('Jan', 'Nowak', 100.0)
    pracownik.register_time(0)
    assert pracownik.pay_salary() == 0

def test_pay_salary4():
    pracownik = Employee('Jan', 'Nowak', 100.0)
    pracownik.register_time(5)
    pracownik.register_time(5)
    assert pracownik.pay_salary() == 1200

def test_premium():
    pracownik = PremiumEmployee('Jan', 'Nowak', 100.0)
    pracownik.register_time(5)
    pracownik.give_bonus(1000.0)
    assert pracownik.pay_salary()==1500.0

def test_company():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    google = Company("google")
    google.add_employee(employee)
    assert google.size()==1
    assert google.pay_all_salary==500
    assert google.pay_all_salary==0

    employee2 = Employee('JKrzysztof', 'Nowak', 200.0)
    employee2.register_time(5)
    employee.register_time(5)
    google.add_employee(employee2)
    assert google.pay_all_salary==1500
