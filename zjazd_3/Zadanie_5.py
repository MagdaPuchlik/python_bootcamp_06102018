class CashMachine:
    def __init__(self):
        self.is_available = False
        self.cash = []

    def put_money(self,money):
        self.cash.append(money) # lub self.cash.extend(cash) wtedy też argument w def zmieniam na cash

    def is_available(self):
        if len(self.cash) != 0:
            return True

    #lub return bool(self.bills) -> co oznacza bool?


    def withdraw_money(self, amount):
        withdraw = []

        for ca in sorted(self.cash,reverse=True):
            if sum(withdraw) + ca <= amount:
                withdraw.append(ca)

        if sum(withdraw) == amount:
            for bill in withdraw:
                self.cash.remove(bill)
            return withdraw
        return []

def test_1():
    cash_mashine = CashMachine()

def test_2():
    assert cash_mashine.is_available == False

def test_3():
    cash_mashine = CashMachine()
    cash_mashine.put_money([200,100,100,50])
    assert cash_mashine.is_available() == True

def test_4():
    cash_mashine = CashMachine()
    cash_mashine.put_money([200,100,100,50])
    assert cash_mashine.withdraw_money(150) == [100,50]

def test_5():
    cash_mashine = CashMachine()
    cash_mashine.put_money([200,100,100,50])
    assert cash_mashine.withdraw_money(150) == [100,50]
    assert cash_mashine.withdraw_money(150) == []