class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand
class Car(Vehicle):
    def honk(self):
        return f"{self.brand} goes beep! beep!"

my_car = Car("Toyota")
print(my_car.honk()) 