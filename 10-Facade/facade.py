# Нужен простой API для пользователя


class Buffer:
    def __init__(self, width=30, height=20):
        self.width = width
        self.height = height
        self.buffer = [' '] * (width * height)

    def __getitem__(self, item):
        # Индексация для того что бы получить символ в определенной позиции в буфере
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.buffer += text
        print(self.buffer)


class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index):
        return self.buffer[index + self.offset]

    def append(self, text):
        self.buffer.write(text)


# Фасад

class Console:
    def __init__(self):
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    def write(self, text):
        self.current_viewport.buffer.write(text)

    def get_char_at(self, index):
        return self.current_viewport.get_char_at(index)


if __name__ == '__main__':
    c = Console()

    # Делаем простым, сложные механики систем.
    c.write('Hello')

    # Даем так же низкоуровневые инструменты для продвинутых пользователей.
    ch = c.get_char_at(0)
