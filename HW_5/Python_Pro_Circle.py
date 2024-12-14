import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    # def contains(self, point):
    #     distance = math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
    #     return distance <= self.radius

    def __contains__(self, point):
        distance = math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
        return distance <= self.radius


# circle = Circle(0, 0, 3)
#
# point = Point(1, 2)
#
# print(circle.contains(point))

p1 = Point(1, 2)
c1 = Circle(1, 2, 10)
print(p1 in c1)

p2 = Point(12, 2)

print(p2 in c1)
