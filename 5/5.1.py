"""
#Классная точка
class Point:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

#Классная точка 2.0
class Point:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y
    
    def length(self, other):
        return round(((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5, 2)
    
first_point = Point(2, -7)
second_point = Point(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))


#Не нажимай красную кнопку!
class RedButton:

    def __init__(self):
        self.press = 0

    def click(self):
        self.press += 1
        print("Тревога!")
    
    def count(self):
        return self.press
    
first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())


#Работа не волк
class Programmer:

    def __init__(self, name, position, time=0):
        self.name = name
        self.position = position
        self.time = time
        self.sum = 0
        if position == "Junior":
            self.salary = 10
        elif position == "Middle":
            self.salary = 15
        elif position == "Senior":
            self.salary = 20
    
    def work(self, time):
        self.time += time
        self.sum += self.salary * time
    
    def rise(self):
        if self.position == "Junior":
            self.position = "Middle"
            self.salary = 15
        elif self.position == "Middle":
            self.position = "Senior"
            self.salary = 20
        elif self.position == "Senior":
            self.salary += 1
    
    def info(self):
        return f"{self.name} {self.time}ч. {self.sum}тгр."
    
programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())


#Классный прямоугольник
class Rectangle:
    def __init__(self, first, second):
        (x1, y1), (x2, y2) = first, second
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        self.width = x2 - x1
        self.height = y2 - y1

    def area(self):
        return round(self.width * self.height, 2)

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)
    
rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.perimeter())
rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.area())


"""
#Классный прямоугольник 2.0
class Rectangle:
    def __init__(self, first, second):
        (x1, y1), (x2, y2) = first, second
        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))
        self.p1, self.p2 = [x1, y1], [x2, y2]
        self.width = x2 - x1
        self.height = y2 - y1

    def area(self):
        return round(self.width * self.height, 2)

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def get_pos(self):
        return (round(self.p1[0], 2), round(self.p2[1], 2))

    def get_size(self):
        return (round(self.width, 2), round(self.height, 2))

    def move(self, dx, dy):
        self.p1[0] += dx
        self.p1[1] += dy
        self.p2[0] += dx
        self.p2[1] += dy

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
        self.p1[1] = self.p1[1] + new_width
        self.p2[0] = self.p1[0] - new_height


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())

rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())
