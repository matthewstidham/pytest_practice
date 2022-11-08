#!/usr/bin/env python3
import decimal

class Pi:
    def __init__(self, stop):
        self.pi = 2 ** 0.5 / 2
        self.count = 1
        self.stop = stop
        self.root_two = 2 ** 0.5

    @staticmethod
    def numerator(inner):
        return (2 + inner) ** 0.5

    def calculator(self):
        value = self.root_two
        for count in range(self.stop):
            value = self.numerator(value)
            self.pi *= value / 2
            print(value, self.pi)


class TestClass:
    def test_value(self):
        pi = Pi(stop=100)
        pi.calculator()
        validation = Pi(stop=10_000)
        validation.calculator()
        rounding_value = 1000
        print(decimal.Decimal(str(pi.pi)).as_tuple().exponent)
        assert round(1 / pi.pi * 2, rounding_value) == round(1 / validation.pi * 2, rounding_value)


def main():
    pi = Pi(stop=10)
    pi.calculator()
    true_value = 1 / pi.pi * 2
    print(decimal.Decimal(str(pi.pi)).as_tuple().exponent)
    print(true_value)


if __name__ == "__main__":
    main()
