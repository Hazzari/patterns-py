class GraphicObject:
    """Удержание группы объектов."""

    def __init__(self, color: str = None):
        self.color = color
        self._name = 'Base Group'
        self.children = []

    def _print(self, items: list, depth: int):
        items.append('*' * depth)
        if self.color:
            items.append(self.color)
        items.append(f'{self.name}\n')

        for child in self.children:
            child._print(items, depth + 1)  # noqa

    @property
    def name(self):
        return self._name

    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)


class Circle(GraphicObject):
    @property
    def name(self):
        return 'Circle'


class Square(GraphicObject):
    @property
    def name(self):
        return 'Square'


if __name__ == '__main__':
    drawing = GraphicObject()
    drawing.children.append(Square('Red'))
    drawing.children.append(Circle('Green'))

    group = GraphicObject()

    group.children.append(Circle('Blue'))
    group.children.append(Square('Blue'))
    drawing.children.append(group)

    print(drawing)
