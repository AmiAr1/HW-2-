class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if type(other) == int:
            print(f'{other}({self.numerator}/{self.denominator})')
        elif type(other) == float:
            print(f'{self.numerator / self.denominator + other}')

    def __sub__(self, other):
        if type(other) == int:
            print(f'{other - self.numerator / self.denominator}')
        elif type(other) == float:
            print(f'{self.numerator / self.denominator - other}')

    def __mul__(self, other):
        if type(other) == int:
            print(f'{other * self.numerator}/{1 * self.denominator}')
        elif type(other) == float:
            print(f'{self.numerator / self.denominator * other}')

    def __floordiv__(self, other):
        if type(other) == int:
            self.denominator *= other
            print(f'{self.numerator // self.denominator}')
        elif type(other) == float:
            print(f'{(self.numerator / self.denominator) // other}')


F = Fraction(10,2)
F.__add__(5)