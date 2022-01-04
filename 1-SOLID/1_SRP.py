"""
Принцип единственной ответственности
"""


class Journal:
    """ Ответственность журнала добавлять, хранить, удалять записи
    """

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self) -> str:
        return '\n'.join(self.entries)

    # # Далее нарушение единой ответственности

    # def save(self, filename):
    #     """ Сохранение журнала
    #     """
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename): pass
    #
    # def low_from_web(self, uri): pass


# Лучшая практика - вынести в менеджер

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        """ Сохранение журнала
        """
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

    def load(self, filename): pass

    def low_from_web(self, uri): pass


j = Journal()
j.add_entry('Мучился изучая паттерны')
j.add_entry('Ужинал плотно')

# print(j)

file = r'journal.txt'

p = PersistenceManager()
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
