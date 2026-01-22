"""
#Классная точка 3.0
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, other):
        return round(((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 2:
            x, y = args
        elif len(args) == 1:
            x, y = args[0][0], args[0][1]
        else:
            x, y = 0, 0
        super(PatchedPoint, self).__init__(x, y)

point = PatchedPoint()
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)

first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))


#Классная точка 4.0
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, other):
        return round(((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 2:
            x, y = args
        elif len(args) == 1:
            x, y = args[0][0], args[0][1]
        else:
            x, y = 0, 0
        super(PatchedPoint, self).__init__(x, y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"
    
print(PatchedPoint.mro()) #Цепочка наследования 
point = PatchedPoint()
print(point)
point.move(2, -3)
print(repr(point))

first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(*map(str, (first_point, second_point)))
print(*map(repr, (first_point, second_point)))


#Классная точка 5.0
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, other):
        return round(((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 2:
            x, y = args
        elif len(args) == 1:
            x, y = args[0][0], args[0][1]
        else:
            x, y = 0, 0
        super(PatchedPoint, self).__init__(x, y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"
    
    def __add__(self, delta):
        return PatchedPoint(self.x + delta[0], self.y + delta[1])

    def __iadd__(self, delta):
        self.move(delta[0], delta[1])
        return self
    
point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)

first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)


#Дроби v0.1
class Fraction:
    def __init__(self, *args):
        if len(args) == 2:
            self.num = args[0]
            self.den = args[1]
        else:
            self.num = int(args[0][:args[0].find("/")])
            self.den = int(args[0][args[0].find("/") + 1:])
        nod = self.__nod(self.num, self.den)
        self.__rdc(nod)

    def __nod(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __rdc(self, nod):
        self.den = self.den / nod
        self.num = self.num / nod

    def numerator(self, a=0):
        if a == 0:
            return int(abs(self.num))
        else:
            self.num = a
            nod = self.__nod(self.num, self.den)
            self.__rdc(nod)

    def denominator(self, a=0):
        if a == 0:
            return int(abs(self.den))
        else:
            self.den = a
            nod = self.__nod(self.num, self.den)
            self.__rdc(nod)

    def __str__(self):
        return f"{int(self.num)}/{int(self.den)}"

    def __repr__(self):
        return f"Fraction({int(self.num)}, {int(self.den)})"


fraction = Fraction(3, 9)
print(fraction, repr(fraction))
fraction = Fraction('7/14')
print(fraction, repr(fraction))

fraction = Fraction(3, 210)
print(fraction, repr(fraction))
fraction.numerator(10)
print(fraction.numerator(), fraction.denominator())
fraction.denominator(2)
print(fraction.numerator(), fraction.denominator())


#Дроби v0.2

class Fraction:
    def __init__(self, *args):
        if len(args) == 2:
            self.num = args[0]
            self.den = args[1]
        else:
            self.num = int(args[0][:args[0].find("/")])
            self.den = int(args[0][args[0].find("/") + 1:])
        nod = self.__nod(self.num, self.den)
        self.__rdc(nod)

    def __nod(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __rdc(self, nod):
        self.den = self.den / nod
        self.num = self.num / nod

    def numerator(self, a=0):
        if a == 0:
            return int(abs(self.num))
        else:
            if self.num < 0:
                self.num = -a
            else:
                self.num = a
            nod = self.__nod(self.num, self.den)
            self.__rdc(nod)

    def denominator(self, a=0):
        if a == 0:
            return int(abs(self.den))
        else:
            if self.den < 0:
                self.den = -a
            else:
                self.den = a
            nod = self.__nod(self.num, self.den)
            self.__rdc(nod)

    def __str__(self):
        return f"{int(self.num)}/{int(self.den)}"

    def __repr__(self):
        return f"Fraction('{int(self.num)}/{int(self.den)}')"
    
    def __neg__(self):  
        return Fraction(-self.num, self.den)
    
 
a = Fraction(1, 3)
b = Fraction(-2, -6)
c = Fraction(-3, 9)
d = Fraction(4, -12)
print(a, b, c, d)
print(*map(repr, (a, b, c, d)))

a = Fraction('-1/2')
b = -a
print(a, b, a is b)
b.numerator(-b.numerator())
a.denominator(-3)
print(a, b)
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())


"""
#Дроби v0.3
class Fraction:
    def __init__(self, *args):
        if len(args) == 2:
            self.num = args[0]
            self.den = args[1]
        else:
            self.num = int(args[0][:args[0].find("/")])
            self.den = int(args[0][args[0].find("/") + 1:])
        nod = self.__nod(self.num, self.den)
        self.__rdc(nod)

    def __nod(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __rdc(self, nod):
        self.den = self.den / nod
        self.num = self.num / nod

    def numerator(self, a=0):
        if a == 0:
            return int(abs(self.num))
        else:
            if self.num < 0:
                self.num = -a
            else:
                self.num = a
            nod = self.__nod(self.num, self.den)
            self.__rdc(nod)

    def denominator(self, a=0):
        if a == 0:
            return int(abs(self.den))
        else:
            if self.den < 0:
                self.den = -a
            else:
                self.den = a
            nod = self.__nod(self.num, self.den)
            self.__rdc(nod)

    def __str__(self):
        return f"{int(self.num)}/{int(self.den)}"

    def __repr__(self):
        return f"Fraction('{int(self.num)}/{int(self.den)}')"
    
    def __neg__(self):  
        return Fraction(-self.num, self.den)
    
    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __iadd__(self, other):
        self.num = self.num * other.den + other.num * self.den
        self.den = self.den * other.den
        nod = self.__nod(self.num, self.den)
        self.__rdc(nod)
        return self
    
    def __isub__(self, other):
        self.num = self.num * other.den - other.num * self.den
        self.den = self.den * other.den
        nod = self.__nod(self.num, self.den)
        self.__rdc(nod)
        return self
    

a = Fraction(1, 3)
b = Fraction(1, 2)
c = a + b
print(a, b, c, a is c, b is c)

a = Fraction(1, 8)
c = b = Fraction(3, 8)
b -= a
print(a, b, c, b is c)