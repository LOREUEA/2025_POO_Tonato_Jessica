class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Agregaremos una Tupla
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Libro: {self.titulo_autor[0]} por {self.titulo_autor[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Creamos una Lista de objetos (Libro)

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {len(self.libros_prestados)}"

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Creamos un Diccionario: ISBN, para  Libro
        self.usuarios_registrados = {}  # Creamos un Diccionario: ID Usuario, para Usuario

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro añadido: {libro.titulo_autor[0]}")
        else:
            print("El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario.nombre}")
        else:
            print("El usuario ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.usuarios_registrados[id_usuario]
            libro = self.libros_disponibles.pop(isbn)  # Cambia el listado de libro de disponibles
            usuario.libros_prestados.append(libro)  # Permite añadir a los libros prestados
            print(f"Libro '{libro.titulo_autor[0]}' prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros_disponibles[isbn] = libro  # Devuelve el libro al inventario
                    print(f"Libro '{libro.titulo_autor[0]}' devuelto por {usuario.nombre}.")
                    return
            print("El usuario no tiene ese libro prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if (criterio == "titulo" and valor.lower() in libro.titulo_autor[0].lower()) or \
               (criterio == "autor" and valor.lower() in libro.titulo_autor[1].lower()) or \
               (criterio == "categoria" and valor.lower() == libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            return usuario.libros_prestados
        else:
            return []

# Pruebas del sistema
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("Bajo la misma estrella", "John Green", "Romance", "584756324")
libro2 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Novela", "942741124")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Angelica Perales", "001")
biblioteca.registrar_usuario(usuario1)

# Prestar libros
biblioteca.prestar_libro("001", "942741124")

# Buscar libros
print("\n🔍 Búsqueda por título 'El amor en los tiempos del cólera':")
for libro in biblioteca.buscar_libro("titulo", "El amor en los tiempos del cólera"):
    print(libro)

# Listar libros prestados
print("\n📚 Libros prestados a Angelica Perales:")
for libro in biblioteca.listar_libros_prestados("001"):
    print(libro)

# Devolver libros
biblioteca.devolver_libro("001", "942741124")

# Mostrar libros disponibles después de la devolución
print("\n📖 Libros disponibles en la biblioteca:")
for libro in biblioteca.libros_disponibles.values():
    print(libro)