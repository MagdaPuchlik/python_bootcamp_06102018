class Company:

    def __init__(self,nazwa):




    def give_firma(self, company):
        self.firma = company

    def give_liczba(self, size):
        self.licza = size

    def pay_salary(self):
        to_pay = super().pay_salary()
        return to_pay * self.liczba