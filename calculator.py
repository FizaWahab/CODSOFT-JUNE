import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == '+':
        result.set(num1 + num2)
    elif operation == '-':
        result.set(num1 - num2)
    elif operation == '*':
        result.set(num1 * num2)
    elif operation == '/':
        if num2 != 0:
            result.set(num1 / num2)
        else:
            result.set("Error: Division by zero")
    else:
        result.set("Invalid operation")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields and labels
entry_num1 = tk.Entry(root, width=20)
entry_num2 = tk.Entry(root, width=20)
result = tk.StringVar()

label_num1 = tk.Label(root, text="Enter the first number:")
label_num2 = tk.Label(root, text="Enter the second number:")
label_result = tk.Label(root, text="Result:")

# Create a dropdown menu for operations
operation_var = tk.StringVar(root)
operation_var.set('+')  # Default operation is addition
operation_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)

# Place widgets on the grid
label_num1.grid(row=0, column=0)
label_num2.grid(row=1, column=0)
label_result.grid(row=2, column=0)

entry_num1.grid(row=0, column=1)
entry_num2.grid(row=1, column=1)
operation_menu.grid(row=0, column=2)
calculate_button.grid(row=1, column=2)
tk.Label(root, textvariable=result).grid(row=2, column=1)

# Start the GUI main loop
root.mainloop()
