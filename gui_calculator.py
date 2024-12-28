import tkinter as tk
from tkinter import messagebox
from Calculator_functions import add, subtract, multiply, divide, modulo, sin, cos, power, square_root, floor, ceil

def calculate():
    try:
        if not entry1.get() and not entry2.get():
            raise ValueError("Both input fields are empty.")
            
        num1 = float(entry1.get()) if entry1.get() else 0
        num2 = float(entry2.get()) if entry2.get() else 0
        operation = operation_var.get()

        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)
        elif operation == "Modulo":
            result = modulo(num1, num2)
        elif operation == "Sin":
            result = sin(num1)
        elif operation == "Cos":
            result = cos(num1)
        elif operation == "Power":
            result = power(num1, num2)
        elif operation == "Square Root":
            result = square_root(num1)
        elif operation == "Floor":
            result = floor(num1)
        elif operation == "Ceil":
            result = ceil(num1)

        result_label.config(text=f"Result: {result}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Setting up the GUI window
root = tk.Tk()
root.title("Calculator")

# Input fields and labels
entry1 = tk.Entry(root, width=20)
entry1.grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=10, pady=5)

entry2 = tk.Entry(root, width=20)
entry2.grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=10, pady=5)

# Dropdown menu for operations
operation_var = tk.StringVar(root)
operation_var.set("Addition")  # Default value
operations = ["Addition", "Subtraction", "Multiplication", "Division", "Modulo", "Sin", "Cos", "Power", "Square Root", "Floor", "Ceil"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=2, column=1, padx=10, pady=5)
tk.Label(root, text="Operation:").grid(row=2, column=0, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Start the GUI loop
root.mainloop()
