import tkinter as tk
from tkinter import messagebox

class BMI_Calculator:
  def __init__(self):
    self.window = tk.Tk()
    self.window.title("BMI Calculator")

    self.weight_label = tk.Label(self.window, text="Weight (lbs):")
    self.weight_label.grid(row=0, column=0, padx=10, pady=10)
    self.weight_entry = tk.Entry(self.window)
    self.weight_entry.grid(row=0, column=1, padx=10, pady=10)

    self.height_label = tk.Label(self.window, text="Height (inches):")
    self.height_label.grid(row=1, column=0, padx=10, pady=10)
    self.height_entry = tk.Entry(self.window)
    self.height_entry.grid(row=1, column=1, padx=10, pady=10)

    self.calculate_button = tk.Button(self.window, text="Calculate BMI", command=self.run)
    self.calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    self.result_label = tk.Label(self.window, text="")
    self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    self.weight = 0
    self.height = 0
    self.bmi = 0

    self.window.mainloop()

  def user_weight(self):
    try:
      self.weight = float(self.weight_entry.get())
      if self.weight < 0:  # Check if the weight is negative
        messagebox.showerror("Error", "Please enter a postive number.")
    except ValueError:
      messagebox.showerror("Error", "Please enter a valid number.")

  def user_height(self):
    try:
      self.height = float(self.height_entry.get())
      if self.height < 0:
        messagebox.showerror("Error", "Please enter a postive number.")
    except ValueError:
      messagebox.showerror("Error", "Please enter a valid number.")

  def calculate(self):
    self.bmi = self.weight * 703 / self.height ** 2  # Calculate BMI

  def interpret(self):
    if self.bmi <= 18.4:
      self.result_label.config(text=f"BMI Index: {self.bmi}. You're underweight.")
    elif self.bmi <= 24.9:
      self.result_label.config(text=f"BMI Index: {self.bmi}. You're healthy.")
    elif self.bmi <= 39.9:
      self.result_label.config(text=f"BMI Index: {self.bmi}. You're overweight.")
    elif self.bmi >= 40:
      self.result_label.config(text=f"BMI Index: {self.bmi}. You're obese.")

  def run(self):
    self.user_weight()
    self.user_height()
    self.calculate()
    self.interpret()

bmi = BMI_Calculator()  # Create an instance of the BMI_Calculator class