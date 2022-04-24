# Функциональные декораторы встроенные в Python.

import time
from functools import wraps


def time_it(func):
    @wraps(func)
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'Имя функции - {func.__name__}. Затрачено времени {int((end - start) * 1000)}ms')

        return result

    return wrapper


@time_it
def some_op():
    """Какая-то функция выполняющая долгие операции."""
    print('Начинаем операцию')
    time.sleep(1)
    print('Выполнено')
    return 123


if __name__ == '__main__':
    # some_op()
    # time_it(some_op)()
    res = some_op()
    print('Результат выполнения функции', res)
    help(some_op)
