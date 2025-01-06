import math

class Shape:
   def __init__(self):
       pass  # Placeholder for future attributes

   def volume(self):
       raise NotImplementedError("Subclasses must implement volume method")

class Cube:
    def __init__(self, side_length):
        self.side_length = side_length

    def volume(self):
        return self.side_length ** 3

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

cube = Cube(5)
print(f"The volume of a cube with side length 5 is {cube.volume()}")

cylinder = Cylinder(2, 5)
print(f"The volume of a cylinder with radius 2 and height 5 is {cylinder.volume()}")