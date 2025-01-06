import math

def Square(l):
  l = float(input("Length: "))
  return l^2  #Calculates the area of a square and returns it

def Rectangle(l, w):
  l = float(input("Length: "))
  w = float(input("Width: "))
  return l * w

def Triangle(b, h):
  b = float(input("Base: "))
  h = float(input("Height: "))
  return 0.5 * l * w

def Circle(r):
  r = float(input("Radius: "))
  return math.pi * r * r  #Calculates the area of a circle using the given values and returns it

def Trapezoid(b1, b2, h):
  b1 = float(input("Base 1: "))
  b2 = float(input("Base 2: "))
  h = float(input("Height: "))
  return (b1 + b2) / 2 * h

def Rhombus(d1, d2):
  d1 = float(input("Diagonal 1: "))
  d2 = float(input("Diagonal 2: "))
  return (d1 * d2) / 2
  
option = input("Enter the shape you want to calculate the area of: ")  #Asks the user to input the shape they want to calculate the area of

if option.lower() == "square":
  area = Square(0)
  print(f"The area of the square is {area}")  #Calls the Square function and assigns the returned value to the area variable
elif option.lower() == "rectangle":
  area = Rectangle(0, 0)
  print(f"The area of the rectangle is {area}")
elif option.lower() == "triangle":
  area = Triangle(0, 0)
  print(f"The area of the triangle is {area}")
elif option.lower() == "circle":
  area = Circle(0)
  print(f"The area of the circle is {area}")
elif option.lower() == "trapezoid":
  area = Trapezoid(0, 0, 0)
  print(f"The area of the trapezoid is {area}")
elif option.lower() == "rhombus":
  area = Rhombus(0, 0)
  print(f"The area of the rhombus is {area}")
else:
  print("Invalid shape choice.")  #If the user enters an invalid shape choice, it prints an error message