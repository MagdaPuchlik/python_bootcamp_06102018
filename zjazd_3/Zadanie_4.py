class Basket(object):
    def __init__(self):
        self.products = []

    def __str__(self):
        return "Basket"

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

def test_create_basket():
    basket = Basket()
    assert str(basket) =="Basket"
    assert basket.products == []

def test_add_product_to_basket():
    basket = Basket()
    product = Product(1,'Woda',10.99)
    basket.add_basket(product,5)