import tkinter as tk
from tkinter import messagebox, simpledialog


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        self.tasks = []  # Lista para almacenar las tareas

        # Configuración de la interfaz
        self.label = tk.Label(root, text="Eventos / Tareas Programadas")
        self.label.pack(pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Agregar Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = simpledialog.askstring("Agregar Tarea", "Introduce la tarea:")
        if task:
            self.tasks.append(task)
            self.update_task_listbox()

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Limpia el Listbox
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)  # Añade tareas actuales al Listbox


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

    def agregar_evento(self):
        evento = simpledialog.askstring("Agregar Evento", "Ingrese el evento:")
        if evento:
            self.eventos.append(evento)
            self.actualizar_lista()

    def eliminar_evento(self):
        try:
            seleccion = self.lista_eventos.curselection()[0]
            del self.eventos[seleccion]
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")

    def actualizar_lista(self):
        self.lista_eventos.delete(0, tk.END)
        for evento in self.eventos:
            self.lista_eventos.insert(tk.END, evento)


if name == "main":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()