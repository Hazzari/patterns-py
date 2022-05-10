class Person:
    def __init__(self, id_, name):
        self.id = id_
        self.name = name


class PersonFactory:
    id = 0

    @staticmethod
    def create_person(name):
        p = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return p
