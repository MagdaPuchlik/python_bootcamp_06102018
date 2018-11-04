class BasketEntry:


    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.price * self.quantity


class Basket(object):
    def __init__(self):
        self.entries = []

    def __str__(self):
        return "Basket"

    def add_product(self,product,quantity):
        basket_entry = BasketEntry(product,quantity)
        self.entries.append(basket_entry)

    def count_total_price(self):
        sum_ = 0
        for e in self.entries:
            sum_ += e.count_price()
        return sum_

    def generate_report(self): #ważne jest gdzie umieszczamy

        temp=""
        for entry in self.entries:
            temp += f"- {entry.product.name}({entry.product.ID}), cena: {entry.product.price} x {entry.quantity}"

        output = '''Produkty w koszyku:
        {}   
        W sumie: {}
        '''
        total_price = self.count_total_price()
        return output.format(temp,total_price) # funkcja format pozwala na uzupełnienie outputu (szablonu) w pustych miejscach, uzupełnia po kolei

class Product:

    def __init__(self, ID, name, price):
        self.ID = ID
        self.name = name
        self.price = price


    def print_info(self):
        return f'- "{self.name}", cena:{self.price}'

def test_product():
    product = Product(1,'Woda',10)
    assert product.ID ==1
    assert product.name == "Woda"
    assert product.price == 10

def test_create_basket():
    basket = Basket()
    assert str(basket) =="Basket"
    assert basket.entries == []

def test_add_product_to_basket():
    basket = Basket()
    product = Product(1,'Woda',10)
    basket.add_product(product,5)
    assert len(basket.entries)== 1

# test dla zliczenia wartości koszyka

def test_basket_count_total_price():
    basket = Basket()
    product = Product(1,'Woda',10)
    basket.add_product(product,5)
    assert basket.count_total_price() == 50

def test_basket_entry():
    be = BasketEntry(Product(1,"Woda",2),5)
    assert be.count_price()==10

def test_basket_generate_report():
    basket = Basket()
    product = Product(1,'Woda',10)
    basket.add_product(product,5)
    assert basket.generate_report()=='''Produkty w koszyku:
    - Woda(1), cena: 10 x 5
    W sumie: 50
    '''