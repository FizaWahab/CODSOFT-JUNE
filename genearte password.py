import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
label = tk.Label(root, text="Enter password length:")
label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

# Start the GUI main loop
root.mainloop()
