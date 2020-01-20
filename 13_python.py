"""
 class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def area(self):
        return self.width * self.len

r = Rectangle(4, 2)
print(r.area())

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]
    
    def change_data(self, index, n):
        self.nums[index] = n

data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)

class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"
    
    def public_method(self):
        # client が使ってもよい
        pass # pass文は、文が必須な構文で何もしない場合に使う

    def _unsafe_method (self):
        # client は使うべきじゃない
        pass # pass文は、文が必須な構文で何もしない場合に使う


# ポリモーフィズムなしでさまざまな形状を描写する
shapes = [trl, sql, crl]
for a_sharpe in shapes:
    if isinstance(a_sharpe, Triangle):
        a_sharpe.draw_triangle()
    if isinstance(a_sharpe, Square):
        a_sharpe.draw_square()
    if isinstance(a_sharpe, Circle):
        a_sharpe.draw_circle()

# ポリモーフィズムを実装して描写する
shapes = [trl, swl, crl]
for a_sharpe in shapes:
    a_sharpe.draw()

class  Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def print_size(self):
        print("{} by {}".format(self.width, self.len))

class Square(Shape):
    def area(self):
        return self.width * self.len
    
    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))

a_square = Square(20, 20)
#print(a_square.area())
a_square.print_size()

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name)

#1
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l
    
    def print_perimeter(self):
        print((self.width + self.length) * 2)

    def change_size(self, w, l):
        self.width = w
        self.length = l

r = Rectangle(4,5)
r.print_perimeter()
r.change_size(6,7)
r.print_perimeter()


class Square:
    def __init__(self, w):
        self.width = w
    
    def print_perimeter(self):
        print(self.width * 4)

    def change_size(self, w):
        self.width = w

s = Square(4)
s.print_perimeter()
s.change_size(6)
s.print_perimeter()


class Sharpe:
    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a sharpe")

sharpe = Sharpe()
sharpe.what_am_i()
"""

class Horse:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

take = Rider("Take Yutaka")
horse = Horse("DeepInpact",take)
print(horse.owner.name)


