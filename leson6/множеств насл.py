# class A:
#     def method(self):
#         print('Its method in class A')
#
#
# class B:
#
#     def method_g(self):
#         print('Its method in class A')
#
#
# class C(A, B):
#     pass
#
#
# exm_c = C()
# exm_c.method()
# exm_c.method_g()
# print(exm_c)
#
#
# class A:
#
#     def metod_a(self):
#         print("digwuif")
#
#


import random
from typing import Union, List


class Arrays:
    def __init__(self):
        self.nesting = random.randint(50, 150)
        self.arrays = self.get_array(1)

    def get_array(self, step) -> Union[List[list], int]:
        if step <= self.nesting:
            return [self.get_array(step + 1)]
        else:
            return random.randint(1_000, 100_000)


nested_arrays = Arrays()
nested_arrays.get_array()

#
# class Solution:
#
#     def get_num(self, arrays: list) -> int:
#         # """
#                    решение
#               """


# Solution().get_num(nested_arrays.arrays)
#
# внутри класса Solution есть метод get_num() который принимает arrays - это массив с рандомной вложенностью от 50 до
# 150 и в самом последнем вложенном массиве есть рандомное число от 1_000 - 100_000
#
# Ваша задача состоит в том что бы достать это число не используя цикл))
#
# если хотите подсказку напишите ПОДСКАЗКА)
#
# Deadline: 24.06.2022
