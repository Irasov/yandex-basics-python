"""
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