class Basket:
    def __init__(self):
        self.basket = set()

    def add_product(self,product,ilosc):
        self.ilosc = ilosc
        self.basket.add(product)

    def count_total_price(self):


class Product:

    def __init__(self, ID, nazwa, cena):
        self.ID = ID
        self.nazwa = nazwa
        self.cena = cena


def test_product():
    product = Product(1,'Woda',10.99)
    assert product.ID ==1
    assert product.nazwa == "Woda"
    assert product.cena == 10.99

def test_basket1():
    basket = Basket()
    product = Product(1,'Woda',10.00)
    basket.add_product(product,5)
    assert basket.count_total_price() == 50.00
