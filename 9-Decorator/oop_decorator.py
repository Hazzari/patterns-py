# Проблема - не позволяет получать доступ к ниже лежащим фигурам.

from abc import ABC


class Shape(ABC):
    def __str__(self):
        return ''


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'Круг радиусом {self.radius}.'


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'Квадрат со стороной {self.side}.'


class ColoredShape(Shape):
    """Декоратор."""

    def __init__(self, shape, color):
        if isinstance(shape, ColoredShape):
            raise Exception('Cannot apply same decorator twice')
        self.color = color
        self.shape = shape

    def __str__(self):
        return f'{self.shape} с цветом {self.color}.'


class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f'{self.shape} с {self.transparency * 100.0}% прозрачности'


if __name__ == '__main__':
    circle = Circle(3)
    print(circle)

    red_circle = ColoredShape(circle, 'red')
    print(red_circle)

    red_half_transparent_circle = TransparentShape(red_circle, 0.5)

    print(red_half_transparent_circle)
