import tkinter as tk
import random
import string

def generate_password():
    name = name_entry.get()
    length = int(length_entry.get())
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    result_label.config(text=f"Hi {name}, your generated password is:\n{password}")

# Create the main application window
root = tk.Tk()
root.title("Name-based Password Generator")
root.geometry("200x200")

# Name input
name_label = tk.Label(root, text="Your Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Length input
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the main loop
root.mainloop()
