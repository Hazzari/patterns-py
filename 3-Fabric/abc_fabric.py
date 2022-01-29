from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('Наш чай очень вкусный!')


class Coffee(HotDrink):
    def consume(self):
        print('Наш кофе очень вкусный!')


# Не обязательный класс в Python
class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Кладем в чашку чай, заливаем кипятком,'
              f'налить {amount}ml, наслаждаться напитком!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Насыпаем в чашку кофе, заливаем кипятком,'
              f'налить {amount}ml, наслаждаться напитком!')
        return Coffee()


def make_drink(type_):
    if type_ == 'tea':
        return TeaFactory().prepare(200)
    elif type_ == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        Tea = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks:')
        for f in self.factories:
            print(f[0])

        s = input(f'Please pick drink (0-{len(self.factories) - 1}): ')
        idx = int(s)
        s = input(f'Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


if __name__ == '__main__':
    hdm = HotDrinkMachine()
    hdm.make_drink()
    # entry = input('Какой вы хотите напиток?')
    # drink = make_drink(entry)
    # drink.consume()
