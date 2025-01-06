class Temperature:
  def __init__(self, celsius):
    self.celsius = celsius
  # creating a method to convert celsius to fahrenheit
  def fahrenheit(self):
    return self.celsius * 9/5 + 32

  def kelvin(self):
    return self.celsius + 273.15

roomtemp = Temperature(25)

print(roomtemp.fahrenheit())
print(roomtemp.kelvin())