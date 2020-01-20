"""
class Lion:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)

class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)

class Person:
    def __init__(self):
        self.name = "Bob"

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

x = 10
if x is None:
    print("x はNone")
else:
    print("xはNoneじゃない　：(")

x = None
if x is None:
    print("x はNone")
else:
    print("xはNoneじゃない　：(")


class Square:
    square_list = []

    def __init__(self, w):
        self.width = w
        self.square_list.append(self)
    
    def print_perimeter(self):
        print(self.width * 4)
        print(self.square_list)

    def change_size(self, w):
        self.width = w


s = Square(4)
s.print_perimeter()
s = Square(5)
s.print_perimeter()
s = Square(6)
s.print_perimeter()
"""

class Twonum:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def judgement(self):
        if self.width == self.len:
            return True
        else:
            return False


t = Twonum(2,3)
print(t.judgement())
t = Twonum(3,3)
print(t.judgement())
t = Twonum(4,3)
print(t.judgement())