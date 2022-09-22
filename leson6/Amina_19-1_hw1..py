class Car:

    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f"\n{self.title} {self.model} engine started!")

    def stop_engine(self):
        print(f"\n{self.title} {self.model} engine stoped!")

    def info(self):
        print(f"\nAll Info:\n"
              f"title: {self.title}, model: {self.model}, weight: {self.weight},\n"
              f"hp: {self.hp}, nm:{self.nm}, max_speed: {self.max_speed}, color: {self.color}")


car1 = Car("bmw", "x7", "2580kg", "390kw", "750nm", "250км/ч", "white")
car1.start_engine()
car1.stop_engine()
car1.info()


car2 = Car("Mercedes", 'AMG GP', '2195kg', '520l', '476nm', '380', 'black')
car2.start_engine()
car2.stop_engine()
car2.info()








# class Mercedes:
#
#     def __init__(self, title, model, weight, hp, nm, max_speed, color):
#         self.title = title
#         self.model = model
#         self.weight = weight
#         self.hp = hp
#         self.nm = nm
#         self.max_speed = max_speed
#         self.color = color
#
#     def start_engine(self):
#         print(f"\n{self.title} {self.model} engine started!")
#
#     def stop_engine(self):
#         print(f"\n{self.title} {self.model} engine stoped!")
#
#     def info(self):
#         print(f"\nAll Info:\n"
#               f"title: {self.title}, model: {self.model}, weight: {self.weight},\n"
#               f"hp: {self.hp}, nm:{self.nm}, max_speed: {self.max_speed}, color: {self.color}")
#
#
# car2 = Mercedes("Mercedes", 'AMG GP', '2195kg', '520l', '476nm', '380', 'black')
# car2.start_engine()
# car2.stop_engine()
# car2.info()
