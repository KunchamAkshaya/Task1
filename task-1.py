import tkinter as tk
from tkinter import messagebox

# Function to perform arithmetic operations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        elif operator == "√":
            result = num1 ** 0.5
        elif operator == "^":
            result = num1 ** num2
        
        entry_result.delete(0, tk.END)
        entry_result.insert(0, result)
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")

# Function to add current result to memory
def memory_add():
    try:
        memory_var.set(float(memory_var.get()) + float(entry_result.get()))
    except ValueError:
        messagebox.showerror("Error", "No valid result to add to memory")

# Function to clear memory
def memory_clear():
    memory_var.set(0)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create entry widgets
entry_num1 = tk.Entry(root, width=10)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

operator_var = tk.StringVar()
operator_choices = ["+", "-", "*", "/", "√", "^"]
operator_var.set("+")
operator_menu = tk.OptionMenu(root, operator_var, *operator_choices)
operator_menu.grid(row=0, column=1, padx=5, pady=5)

entry_num2 = tk.Entry(root, width=10)
entry_num2.grid(row=0, column=2, padx=5, pady=5)

entry_result = tk.Entry(root, width=20)
entry_result.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Create buttons for memory functions
memory_var = tk.StringVar()
memory_var.set(0)
memory_label = tk.Label(root, textvariable=memory_var)
memory_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

memory_add_btn = tk.Button(root, text="M+", command=memory_add)
memory_add_btn.grid(row=3, column=0, padx=5, pady=5)

memory_clear_btn = tk.Button(root, text="MC", command=memory_clear)
memory_clear_btn.grid(row=3, column=1, padx=5, pady=5)

# Create calculate button
calculate_btn = tk.Button(root, text="Calculate", command=calculate)
calculate_btn.grid(row=3, column=2, padx=5, pady=5, sticky="ew")


root.mainloop()
