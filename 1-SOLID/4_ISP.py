"""
Принцип Разделения интерфейса
"""


class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrint(Machine):
    def print(self, document): pass

    def fax(self, document): pass

    def scan(self, document): pass


class OldFashionPrinter(Machine):
    """
    Проблемы:
    """

    def print(self, document):
        # OK
        print('print text')

    def fax(self, document):
        """Клиент может думать что в этом старом принтере есть функция факса"""
        pass  # noop

    def scan(self, document):
        """Можно возмещаться что принтер не умеет сканировать"""
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')


# Лучший вариант:
from abc import abstractmethod


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class Fax:
    @abstractmethod
    def fax(self, document):
        pass


class NewPrinter(Printer):
    def print(self, document):
        print(document)


class PhotoCopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        print(f'Сканирование документа {document}')


class MultiFunctionDevice(Printer, Scanner):  # , Fax, etc
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)


""" Разделять интерфейсы на отдельные"""
