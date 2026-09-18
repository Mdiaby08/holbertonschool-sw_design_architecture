#!/usr/bin/env python3

class Beverage:
    def cost(self):
        raise NotImplementedError

    def description(self):
        raise NotImplementedError


class Coffee(Beverage):
    def cost(self):
        return 50

    def description(self):
        return "Coffee"


class BeverageDecorator(Beverage):
    def __init__(self, inner):
        self._inner = inner


class MilkDecorator(BeverageDecorator):
    def cost(self):
        return self._inner.cost() + 10

    def description(self):
        return self._inner.description() + " + milk"


class SugarDecorator(BeverageDecorator):
    def cost(self):
        return self._inner.cost() + 5

    def description(self):
        return self._inner.description() + " + sugar"


class CaramelDecorator(BeverageDecorator):
    def cost(self):
        return self._inner.cost() + 15

    def description(self):
        return self._inner.description() + " + caramel"


def main():
    # Coffee + milk
    drink1 = MilkDecorator(Coffee())
    print(drink1.description(), drink1.cost())

    # Coffee + sugar + milk
    drink2 = MilkDecorator(SugarDecorator(Coffee()))
    print(drink2.description(), drink2.cost())

    # Coffee + sugar + milk + caramel
    drink3 = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(drink3.description(), drink3.cost())


if __name__ == "__main__":
    main()
