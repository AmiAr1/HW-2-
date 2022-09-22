# class Fraction:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#
#     def __add__(self, other):
#         if type(other) == int:
#             print(f'{other}({self.numerator}/{self.denominator})')
#         elif type(other) == float:
#             print(f'{self.numerator / self.denominator + other}')
#
#     def __sub__(self, other):
#         if type(other) == int:
#             print(f'{other - self.numerator / self.denominator}')
#         elif type(other) == float:
#             print(f'{self.numerator / self.denominator - other}')
#
#     def __mul__(self, other):
#         if type(other) == int:
#             print(f'{other * self.numerator}/{1 * self.denominator}')
#         elif type(other) == float:
#             print(f'{self.numerator / self.denominator * other}')
#
#     def __floordiv__(self, other):
#         if type(other) == int:
#             self.denominator *= other
#             print(f'{self.numerator // self.denominator}')
#         elif type(other) == float:
#             print(f'{(self.numerator / self.denominator) // other}')
#
#
# F = Fraction(10,2)
# F.__add__(5)
class Car:

    def __init__(self, title, model, speed):
        self.title = title
        self.model = model
        self.speed = speed


    def start_engine(self):
        print(f"\n{self.title} {self.model} engine started!")

    def stop_engine(self):
        print(f"\n{self.title} {self.model} engine stoped!")



car1 = Car("Bugatti", "Chiron Super Sport", "490 км/ч")
car1.start_engine()
car1.stop_engine()
from create_car import Car


def car_info(self):
    super(Car).__init__(title, model)
    print(f"\nInfo:\n"
          f"title: {self.title}, model: {self.model}, color: {self.speed}")


