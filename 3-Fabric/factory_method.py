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

    def __str__(self):
        return f'x:{self.x} y:{self.y}'

    # Когда фабричных методов становится слишком много можно сгруппировать их в отдельную сущность
    class PointFactory:
        def new_cartesian_point(self, x, y):
            point = Point(x, y)
            point.x = x
            point.y = y
            return point

        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory()
    # Фабрика - все что угодно что создает объекты


if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.factory.new_polar_point(3, 4)
    print(p)
    print(p2)
