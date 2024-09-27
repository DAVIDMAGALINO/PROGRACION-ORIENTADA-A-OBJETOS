import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")

        self.tasks = []

        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.entry_task = tk.Entry(self.root, width=52)
        self.entry_task.pack(pady=10)

        self.btn_add_task = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.btn_add_task.pack(pady=5)

        self.btn_complete_task = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        self.btn_complete_task.pack(pady=5)

        self.btn_remove_task = tk.Button(self.root, text="Eliminar Tarea", command=self.remove_task)
        self.btn_remove_task.pack(pady=5)

        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<Delete>", lambda event: self.remove_task())
        self.root.bind("<Control-space>", lambda event: self.complete_task())

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            completed_task = self.tasks[selected_index] + " (completada)"
            self.tasks[selected_index] = completed_task
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
