"""
Принцип подстановки Барбары Лисков
"""


class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width


    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height:{self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


# нарушение принципа LSP
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        _width = _height = value


def use_it(rect):
    w = rect.width
    rect.height = 10  # unpleasant side effect
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rect.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)

"""
Можно убрать вообще класс square
а в Rectangle задать частный случай для квадрата
Например:
class Rectangle:
    def __init__(self, width, height=None):
        self._height = height
        self._width = width
        if not height:
            self._height = width

"""
