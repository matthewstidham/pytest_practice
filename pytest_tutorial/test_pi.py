#!/usr/bin/env python3

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


def main():
    print("Hello world")
    pi = Pi(stop=10)
    print(pi.pi)
    pi.calculator()
    print(1 / pi.pi * 2)


if __name__ == "__main__":
    main()
