import random

while True:
  name = input("Name: ").capitalize()  #Takes user input and capitalizes it
  if name.isalpha() == False:
    print("Sorry, enter letters only.")
    continue
  name = name[0:5]  #Truncates the name to 5 characters
  random_int = random.randint(1, 100)  #Generates a random number
  Username = name + str(random_int)  #Combines the name and the random number
  print(f"Your username is {Username}.")
  break