class Vehicle:
  def __init__(self, name):
    self.name = name

  def move(self):
    print(f"{self.name} is moving.")

class Car(Vehicle):
  def __init__(self, name):
    super().__init__(name)

class Truck(Vehicle):
  def __init__(self, name):
    super().__init__(name)

my_car = Car("Honda")
my_truck = Truck("Ford")

my_car.move()
my_truck.move()