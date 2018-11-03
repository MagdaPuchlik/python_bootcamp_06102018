
class dog:

    def __init__(self):
        self.energy = 10

    def bark(self):
        self.energy -=1

    def sleep(self):
        self.energy += 2


    def get_energy(self):
        return self.energy




pies = dog()
pies.bark()
print(pies.energy)


def test_dog():
    pies = dog()

    assert pies.get_energy()==10
    pies.bark()
    pies.bark()
    assert pies.get_energy()==8