import tkinter as tk

class ToDoListApp:
    def _init_(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []
        self.task_entry = tk.Entry(root)
        self.task_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=5)

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack(padx=10, pady=5)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.pack(padx=10, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task_info in self.tasks:
            status = "✔️" if task_info["completed"] else "❌"
            self.task_listbox.insert(tk.END, f"[{status}] {task_info['task']}")

    def mark_completed(self):
        selected_indices = self.task_listbox.curselection()
        for idx in selected_indices:
            self.tasks[idx]["completed"] = True
        self.update_task_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = ToDoListApp(root)
    root.mainloop()
