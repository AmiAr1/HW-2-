
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def person_info(self):
        print(f"\nинфо сотрудника: \n"
              f"first name: {self.first_name}\n"
              f"last name: {self.last_name}\n"
              f"age: {self.age}")
