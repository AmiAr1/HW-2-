
class Car:
    def __init__(self, title, engine, model, color, tachometr):
        self.title = title
        self.engine = engine
        self.model = model
        self.color = color
        self.tachometr = tachometr


    def start (self):
        print(f"{self.title} {self.model}uygx")


    def stop (self):
        print(f"{self.title} {self.model} stop")


    def cek_car(self):
        if self.tachometr < 1:
            print("on")
        else:
            print("off")





class Gg (Car):
    def init(self, title, engine, color, model, tachometer, max_speed):
        super().__init__(title, engine, color, model, tachometer)
        self.max_speed = max_speed


class Tesla(Gg):
    pass




tesla = Tesla(
    'Tesla',
    'electra car',
    'black',
    'plaid',
    1,
    250
)
print(tesla.max_speed)
tesla.start_engine()
tesla.stop_engine()
tesla.car_check()