import tkinter as tk
import cmath

class MyWindow:
  def __init__(self, win):
    self.label1 = tk.Label(win, text="Value for a:", fg = "blue")
    self.label1.grid(row=1, column=1, padx=10, pady=10)
    self.label2 = tk.Label(win, text="Value for b:", fg = "blue")
    self.label2.grid(row=2, column=1, padx=10, pady=10)
    self.label3 = tk.Label(win, text="Value for c:", fg = "blue")
    self.label3.grid(row=3, column=1, padx=10, pady=10)
    self.answer_label = tk.Label(win, text="Answer:", fg = "blue")
    self.answer_label.grid(row=5, column=1, padx=10, pady=10)

    self.input1 = tk.Entry(win)
    self.input1.grid(row=1, column=2)
    self.input2 = tk.Entry(win)
    self.input2.grid(row=2, column=2)
    self.input3 = tk.Entry(win)
    self.input3.grid(row=3, column=2)

    self.result_label = tk.Label(win, text="", fg = "blue")
    self.result_label.grid(row=5, column=2, padx=10, pady=10)

    self.button1 = tk.Button(win, text="Calculate Quadratic", command=self.quad)
    self.button1.grid(row=4, columnspan=3, padx=10, pady=10)

  def quad(self):
    a = float(self.input1.get())
    b = float(self.input2.get())
    c = float(self.input3.get())
    
    d = (b**2) - (4*a*c)
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    sol1 = round(sol1.real, 3) + round(sol1.imag, 3) * 1j
    sol2 = round(sol2.real, 3) + round(sol2.imag, 3) * 1j

    result = (sol1, sol2)
    self.result_label.config(text=result)

window = tk.Tk()
mywin = MyWindow(window)
window.title("Quadratic Formula Calculator")
window.geometry("500x500")
window.mainloop()