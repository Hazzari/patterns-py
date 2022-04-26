

import random
import string


class User:
    def __init__(self, name):
        self.name = name


class User2:
    """
    Сохраняем не строки, а только индексы для частей строки.
    А затем части строки сохраняются в статической переменной,
    потом что бы получить полное имя мы просто берем элементы их sгчваtrings
    для каждого индекса. Хранятся только индексы - целые числа
    """
    strings = []

    def __init__(self, full_name):

        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.names = [get_or_add(x)
                      for x in full_name.split(' ')]

    def __str__(self):
        return ' '.join([self.strings[x] for x in self.names])


def random_string():
    chars = string.ascii_lowercase
    return ''.join(
        [random.choice(chars) for _ in range(12)]
    )


if __name__ == '__main__':
    users = []

    first_names = [random_string() for _ in range(100)]
    last_names = [random_string() for _ in range(100)]

    for first in first_names:
        for last in last_names:
            users.append(User2(f'{first} {last}'))

    print([str(x) for x in users])
