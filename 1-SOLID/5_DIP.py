""" Принцип инверсии зависимостей
"""
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


# решение ->

class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


# class Relationships:
class Relationships(RelationshipBrowser):  # low-level (имеет дело с хранением)

    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == 'John' and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:  # high-level module
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #
    #     # # Тут нарушение принципа:
    #     # # Реализация Research зависит от реализации Relationships
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'У Джона есть ребенок по имени {r[2].name}')

    # Устранение зависимости
    def __init__(self, browser: Relationships) -> None:
        for p in browser.find_all_children_of('John'):
            print(f'У Джона есть ребенок по имени {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
