import tkinter as tk
from tkinter import messagebox
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
    
        self.tasks = []
        self.task_entry = tk.Entry(root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10, padx=20, fill=tk.BOTH)
        
        self.add_button = tk.Button(root, text="Add Task", font=("Helvetica", 12), command=self.add_task)
        self.add_button.pack(padx=20, pady=5, fill=tk.BOTH)
        
        self.tasks_listbox = tk.Listbox(root, font=("Helvetica", 12), selectbackground="yellow")
        self.tasks_listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        self.delete_button = tk.Button(root, text="Delete Task", font=("Helvetica", 12), command=self.delete_task)
        self.delete_button.pack(padx=20, pady=5, fill=tk.BOTH)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
        
    def delete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")
        
    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)
def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()

