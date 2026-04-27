import numpy as np


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def circumference(self):
        return 2 * np.pi * self.r

    def intersection(self, other):
        d = np.hypot(self.x - other.x, self.y - other.y)

        if d == 0 and self.r == other.r:
            return float("inf")
        if d > self.r + other.r or d < abs(self.r - other.r):
            return 0
        if d == self.r + other.r or d == abs(self.r - other.r):
            return 1
        return 2


# dane wpisujesz tutaj
x1, y1, r1 = 0, 0, 2
x2, y2, r2 = 3, 0, 2

c1 = Circle(x1, y1, r1)
c2 = Circle(x2, y2, r2)

print(c1.circumference())
print(c2.circumference())

res = c1.intersection(c2)
print("inf" if np.isinf(res) else res)