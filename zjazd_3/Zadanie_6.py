class Vector:

    def __init__(self,x,y):
        self.x =x
        self.y =y

#przeciążenie wbudowanych operatorów, wszystko co to jest poniżej na filoteotow to budowane operatory
    #__add__ dodawanie
    #__sub__ odejmowanie
    #__mul__ mnożenie
    #__eq__ równość
    #__lt__ mniejsze niż

    def __add__(self, other):
        return Vector(self.x + other.x,self.y + other.y)

    def __sub__(self, other):
        szer1 = self.x - other.x
        dl1 = self.y - other.y

        return Vector(szer1,dl1)

    def __mul__(self, other):
        return Vector(self.x*other, self.y*other)

    def __eq__(self, other):
        return self.x == other.x and self.y ==other.y

    def length(self):
        return ((self.x**2+self.y**2)**0.5)

    def __lt__(self, other):
        return self.length()<other.length()


def test_1():
    vector1 = Vector(1,2)
    vector2 = Vector(1,2)
    result = vector1 + vector2
    assert result.x == 2
    assert result.y == 4



def test_2():
    vector1 = Vector(1,2)
    vector2 = Vector(1,2)
    result = vector1 - vector2
    assert result.x == 0
    assert result.y == 0

def test_3():
    vector1 = Vector(1, 2)
    assert vector1 * 5 == Vector(5,10)

def test_4():
    vector1 = Vector(1,2)
    vector2 = Vector(1,2)
    assert vector1 == vector2

def test_5():
    vector = Vector(2,2)
    assert vector.length() ==(2**2+2**2)**0.5

def test_6():
    vector1 = Vector(1,3)
    vector2 = Vector(1,2)
    assert not(vector1<vector2)
    assert vector2 < vector1