# Скалярный объект может маскироваться под группу
from abc import ABC
from collections.abc import Iterable
from typing import Union


class Connectable(Iterable, ABC):
    def connect_to(self: Union['Neuron', 'NeuronLayer'], other: Union['Neuron', 'NeuronLayer']):
        if self == other:
            return
        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    """Строительный блок для нейросети."""

    def __init__(self, name: str):
        self.name: str = name
        self.inputs: list = []
        self.outputs: list = []

    def __str__(self):
        return f'{self.name}, ' \
               f'{len(self.inputs)} inputs, ' \
               f'{len(self.outputs)} outputs'

    def __iter__(self):
        # Превращение в коллекцию из 1 элемента.
        yield self

    # def connect_to(self, other: 'Neuron'):
    #     self.outputs.append(other)
    #     other.inputs.append(self)


class NeuronLayer(list, Connectable):
    def __init__(self, name: str, count: int):
        super().__init__()
        self.name: str = name
        for x in range(0, count):
            self.append(Neuron(f'{name}-{x}'))

    def __str__(self):
        return f'{self.name} with {len(self)} neurons'


if __name__ == '__main__':
    neuron1 = Neuron('n1')
    neuron2 = Neuron('n2')
    layer1 = NeuronLayer('L1', 3)
    layer2 = NeuronLayer('L1', 4)

    neuron1.connect_to(neuron2)
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)

    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)

    """
    n1, 0 inputs, 4 outputs
    n2, 4 inputs, 0 outputs
    L1 with 3 neurons
    L1 with 4 neurons
    """
