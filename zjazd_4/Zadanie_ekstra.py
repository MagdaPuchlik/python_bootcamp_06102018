"""
Stwórz sferę
s = sfera(10)
s.promien #10

"""
import math

class Sfera:

    def __init__(self,r):
        self.promien = r

    def pow(self):
        return 4* math.pi * self.promien**2

    def obj(self):
        return (4/3)*math.pi*math.pow(self.promien,3)

s=Sfera(10)

print(s.obj())
print(s.pow())