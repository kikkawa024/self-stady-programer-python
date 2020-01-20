"""
x = 2
y = 4
z = 8

xyz = x + y + z

print(xyz)


pop = [] #洋楽リスト
jpop = [] #Jpopリスト

def collect_songs():
    song = "曲名を入力してください："
    ask = "p か j のどちらかを入力して下さい。q で終わります："

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "p":
            p = input(song)
            pop.append(p)
        
        elif genre == "j":
            j = input(song)
            jpop.append(j)
        
        else:
            print("不正な値です。")
        
        print("pop songs: ", pop)
        print("jpop songs: ", jpop)

collect_songs()

#関数型プログラミング

def  increment():
    global a
    a += 1


def increment(a):
    return a + 1

increment(0)
increment(1)
print(increment(2))

#オブジェクト指向プログラミング
class Orange:
    #weight(重さ)はグラム
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")
    
    def rot(self, days, temp):
        #temp(温度)は摂氏
        self.mold = days * temp

orange = Orange(200, "orange")
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)

orl = Orange(10, "dark orange")
orl1 = Orange(4, "light orage")
orl2 = Orange(8, "dark orage")
orl3 = Orange(14, "yellow")

#orl.weight = 100
#orl.color = "light orange"

print(orl1.weight)
print(orl1.color)

print(orl2.weight)
print(orl2.color)

print(orl3.weight)
print(orl3.color)


class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def area(self):
        return self.width * self.len
    
    def change_size(self, w, l):
        self.width  = w
        self.len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle = Rectangle(20, 40)
print(rectangle.area())
rectangle.change_size(100, 200)
print(rectangle.area())

class Apple:
    def __init__(self, w, c, o, d):
        self.weight = w
        self.color = c
        self.origin = o
        self.day = d
        print("Create!")
     
apple = Apple(100, "light red", "青森", "2019/12/30")
print(apple.weight)
print(apple.color)
print(apple.origin)
print(apple.day)
"""
import math

class Circle:
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return self.radius * self.radius * math.pi

circle_area = Circle(10)   
print(circle_area.area())


