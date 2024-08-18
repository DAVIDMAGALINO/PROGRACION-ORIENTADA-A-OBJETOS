import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Datos")

        # Etiqueta
        self.label = tk.Label(root, text="Ingrese un dato:")
        self.label.pack(pady=10)

        # Campo de texto
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        # Botón "Agregar"
        self.add_button = tk.Button(root, text="Agregar", command=self.add_item)
        self.add_button.pack(pady=5)

        # Lista para mostrar datos
        self.listbox = Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # Barra de desplazamiento
        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Botón "Limpiar"
        self.clear_button = tk.Button(root, text="Limpiar", command=self.clear_item)
        self.clear_button.pack(pady=5)

    def add_item(self):
        """Agrega el contenido del campo de texto a la lista."""
        item = self.entry.get()
        if item:
            self.listbox.insert(END, item)
            self.entry.delete(0, END)  # Limpia el campo de texto
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese un dato.")

    def clear_item(self):
        """Limpia el campo de texto y la selección de la lista."""
        self.entry.delete(0, END)  # Limpia el campo de texto
        self.listbox.selection_clear(0, END)  # Limpia la selección de la lista

# Configuración de la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()
