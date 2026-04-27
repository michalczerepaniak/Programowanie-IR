import numpy as np


class Resistor:
    def __init__(self, R=0):
        self.R = R

    def get_resistance(self):
        return self.__R

    def set_resistance(self, R):
        self.__R = R


def series(a, b):
    return Resistor(a.get_resistance() + b.get_resistance())


def parallel(a, b):
    r1 = a.get_resistance()
    r2 = b.get_resistance()

    if r1 == 0 or r2 == 0:
        return Resistor(0)

    return Resistor((r1 * r2) / (r1 + r2))


r1 = 1
r2 = 2

a = Resistor(r1)
b = Resistor(r2)

rs = series(a, b)
rp = parallel(a, b)

print(rs.get_resistance())
print(rp.get_resistance())