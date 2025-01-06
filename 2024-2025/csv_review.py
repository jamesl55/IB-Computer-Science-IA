import csv
import pandas as pd

def user_input(num_of_users):
  User_Data = []
  for x in range(num_of_users):  # loop for number of users
    user_horoscope = input("Horoscope: ")
    user_salary = float(input("Salary: "))
    User_Data.append([user_horoscope, user_salary])  # appends to list
  with open("user_data.csv", "a", newline="") as csvfile:  # opens csv file
    writer = csv.writer(csvfile)  # creates writer object
    if csvfile.tell() == 0:  # checks if file is empty
      writer.writerow(["Horocscope", "Salary"])
    writer.writerows(User_Data)

def display(csvfile):
  df = pd.read_csv(csvfile)  # converts csv file to dataframe
  df.index += 1  # starts dataframe index at 1
  print(f"\n{df}")

num_of_users = int(input("Number of users to be inputted: "))
user_input(num_of_users)
display("user_data.csv")