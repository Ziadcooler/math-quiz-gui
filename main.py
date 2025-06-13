import tkinter as tk
import time
import random as rd

window = tk.Tk()
window.title("math quizzy thingy")
window.geometry("300x300")

def start_menu():
  label.config(text="Select a mode.")
  button.config(text="Start", command=selection_menu)

def selection_menu():
  global button2
  button.config(text="Times Tables", command = times_tables)
  button2 = tk.Button(text="Squares and Cubes", command = squares_cubes)
  button2.pack()

def times_tables():
  global currentState
  currentState = times_tables
  button2.destroy()
  new_nums_times_tables()
  label.config(text="What is " + str(num1) + " x " + str(num2) + "?")
  button.config(text="Submit", command=check_ans)
  entry.config(state="normal")

def new_nums_times_tables():
  global ans, num1, num2
  num1 = rd.randint(1, 12)
  num2 = rd.randint(1, 12)
  ans = num1*num2

def squares_cubes():
  global currentState
  currentState = squares_cubes
  button2.destroy()
  new_nums_squares_cubes()
  button.config(text="Submit", command=check_ans)
  entry.config(state="normal")

def new_nums_squares_cubes():
  global ans, num1
  choice = rd.choice(["Square", "Cube"])
  choice2 = rd.choice(["Normal", "Root"])
  if choice == "Square":
    if choice2 == "Normal":
      num1 = rd.randint(1,12)
      ans = num1 ** 2
      label.config(text=f"What is {num1} squared?")
    else:
      num1 = rd.choice([1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144])
      if num1 == 1:
        ans = 1
      else:
        ans = num1 ** 1/2
      label.config(text=f"What is the square root of {num1}?")
  else:
    if choice2 == "Normal":
      num1 = rd.randint(1,12)
      ans = num1 ** 3
      label.config(text=f"What is {num1} cubed?")
    else:
      num1 = rd.choice([1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728])
      if num1 == 1:
        ans = 1
      else:
        ans = num1 ** 1/3
      label.config(text=f"What is the cube root of {num1}?")

def validateInput(val):
  return val.isdigit() or val == ""
vcmd = window.register(validateInput)

def check_ans():
  global num1, num2, ans
  input = entry.get()
  userans = int(input)
  if userans == ans:
    label.config(text="Correct!")
    entry.delete(0, tk.END)
    entry.config(state="disabled")
    button.config(text="Next", command=currentState)
  else:
    label.config(text="Incorrect! Try again!")
    entry.delete(0, tk.END)

label = tk.Label()
label.pack(pady=10)
entry = tk.Entry(state="disabled", validate="key", validatecommand=(vcmd, '%P'))
entry.pack(pady=20)
button = tk.Button(text="Start", state="normal", command = selection_menu)
button.pack(pady=25)

start_menu()
tk.mainloop()