
from create_car import Car


class Ff(Car):

    def get_car_info(self):
        super().__init__(self.title, self.model, self.color)
        print(f"\ntitle:{self.title}, model:{self.model}, color:{self.color}")

