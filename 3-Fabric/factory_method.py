from enum import Enum
from math import sin, cos


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     """ Плохой вариант"""
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a * sin(b)
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'x:{self.x} y:{self.y}'

    # Когда фабричных методов становится слишком много можно сгруппировать их в отдельную сущность
    class PointFactory:
        @staticmethod
        def new_cartesian_point(x, y):
            point = Point(x, y)
            point.x = x
            point.y = y
            return point

        @staticmethod
        def new_polar_point(rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory()
    # Фабрика - все что угодно что создает объекты


if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.factory.new_polar_point(5, 6)
    p3 = Point.factory.new_cartesian_point(2, 3)
    print(p)
    print(p2)
    print(p == p3)
