from abc import abstractmethod

class Transport:
    def __init__(self, name, price, year, speed):
        self.name = name
        self.price = price
        self.year = year
        self.speed = speed

    @abstractmethod
    def print(self):
        print(f'name: {self.name}')
        print(f'price: {self.price}')
        print(f'year: {self.year}')
        print(f'speed: {self.speed}')


class Plane(Transport):
    def __init__(self, name, price, year, speed, weight):
        super().__init__(self, name, price, year, speed)
        self.weight = weight

    def print(self):
        super().print()
        print(f'name: {self.weight}')


class Car(Transport):
    def __init__(self, name, price, year, speed, type):
        super().__init__(self, name, price, year, speed)
        self.type = type

    def print(self):
        super().print()
        print(f'name: {self.type}')


class Sheep(Transport):
    def __init__(self, name, price, year, speed, length):
        super().__init__(name, price, year, speed)
        self.length = length

    def print(self):
        super().print()
        print(f'name: {self.length}')


sheep = Sheep('Carolina', 10_000_000, 2, 45, 450)
sheep.print()