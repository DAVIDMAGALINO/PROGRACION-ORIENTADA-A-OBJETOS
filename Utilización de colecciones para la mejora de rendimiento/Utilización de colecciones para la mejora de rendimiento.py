class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor  # Almacena autor como una tupla (nombre, apellido)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor[0]} {self.autor[1]} - ISBN: {self.isbn}, Categoría: {self.categoria}"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def __str__(self):
        return f"{self.nombre} (ID: {self.user_id})"

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros con ISBN como clave
        self.usuarios = {}  # Diccionario para almacenar usuarios con user_id como clave
        self.ids_usuarios = set()  # Conjunto para mantener IDs únicos

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro_quitado = self.libros.pop(isbn)
            print(f"Libro quitado: {libro_quitado}")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, nombre, user_id):
        if user_id not in self.ids_usuarios:
            usuario = Usuario(nombre, user_id)
            self.usuarios[user_id] = usuario
            self.ids_usuarios.add(user_id)
            print(f"Usuario registrado: {usuario}")
        else:
            print("El ID de usuario ya está registrado.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            usuario_quitado = self.usuarios.pop(user_id)
            self.ids_usuarios.remove(user_id)
            print(f"Usuario quitado: {usuario_quitado}")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            print(f"Libro prestado: {libro} a {usuario}")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros[isbn]
            if libro in usuario.libros_prestados:
                usuario.devolver_libro(libro)
                print(f"Libro devuelto: {libro} de {usuario}")
            else:
                print("El libro no estaba prestado a este usuario.")
        else:
            print("Usuario o libro no encontrado.")

    def buscar_libro(self, criterio):
        found_books = [libro for libro in self.libros.values() if criterio.lower() in libro.titulo.lower() or
                       criterio.lower() in libro.categoria.lower() or
                       criterio.lower() in ' '.join(libro.autor).lower()]
        return found_books

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            return usuario.libros_prestados
        else:
            print("Usuario no encontrado.")
            return []


# Ejemplo de uso
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Agregar libros
    biblioteca.agregar_libro(Libro("Cien años de soledad", ("Gabriel", "García Márquez"), "Novela", "1234567890"))
    biblioteca.agregar_libro(Libro("Don Quijote de la Mancha", ("Miguel", "de Cervantes"), "Literatura", "0987654321"))

    # Registrar usuarios
    biblioteca.registrar_usuario("Juan Pérez", "user_001")
    biblioteca.registrar_usuario("Ana Martínez", "user_002")

    # Prestar libros
    biblioteca.prestar_libro("user_001", "1234567890")

    # Listar libros prestados
    libros_prestados = biblioteca.listar_libros_prestados("user_001")
    print("Libros prestados a Juan Pérez:", libros_prestados)

    # Devolver libro
    biblioteca.devolver_libro("user_001", "1234567890")

    # Buscar libro
    libros_encontrados = biblioteca.buscar_libro("Quijote")
    print("Libros encontrados:", libros_encontrados)

    # Quitar libro
    biblioteca.quitar_libro("0987654321")

    # Dar baja a un usuario
    biblioteca.dar_baja_usuario("user_002")