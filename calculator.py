import tkinter as tk

def on_button_click(event):
    current_text = event.widget.cget("text")
    if current_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif current_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, current_text)

root = tk.Tk()
root.title("Calculator")

# Create the entry field
entry = tk.Entry(root, font=("Helvetica", 20), bd=10, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4)

button_labels = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]
# Create and place the buttons
row, col = 1, 0
for label in button_labels:
    button = tk.Button(root, text=label, padx=20, pady=20, font=("Helvetica", 15))
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

    button.bind("<Button-1>", on_button_click)

root.mainloop()
