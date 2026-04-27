class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()


# dane wpisujesz tutaj
numbers = [1, 2, 3, 4, 5, 16, 21]

s = Stack()

for x in numbers:
    s.push(x)


while len(s.data) > 0:
    print(s.pop())