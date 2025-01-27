# Sistema de usuarios para servicios de internet
# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario, email, servicio_contratado):
        #Constructor: Inicializa los atributos del usuario.
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.email = email
        self.servicio_contratado = servicio_contratado
        print(f'Usuario creado: {self.nombre} (ID: {self.id_usuario})')

    def __del__(self):
        #Destructor: Indica que el usuario está siendo eliminado.
        print(f'Usuario eliminado: {self.nombre} (ID: {self.id_usuario})')

# Clase GestorUsuarios
class GestorUsuarios:
    def __init__(self):
        #Inicializa una lista vacía para gestionar usuarios.
        self.usuarios = []

    def agregar_usuario(self, usuario):
        #Agregamos a un nuevo usuario al sistema.
        if isinstance(usuario, Usuario):
            self.usuarios.append(usuario)
            print(f'Usuario {usuario.nombre} agregado al sistema.')
        else:
            raise ValueError('Solo se pueden agregar objetos de la clase Usuario')

    def eliminar_usuario(self, id_usuario):
        'Eliminamos a un usuario por su ID.'
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                self.usuarios.remove(usuario)
                del usuario
                print(f'Usuario con ID {id_usuario} eliminado.')
                return
        print(f'No se encontró un usuario con ID {id_usuario}.')

    def mostrar_usuarios(self):
        #Muestrará todos los usuarios registrados.
        if not self.usuarios:
            print('No hay usuarios registrados.')
        else:
            print('Usuarios registrados:')
            for usuario in self.usuarios:
                print(f'- {usuario.nombre} (ID: {usuario.id_usuario}, Servicio: {usuario.servicio_contratado})')

if __name__ == "__main__":
    # Crear un gestor de usuarios
    gestor = GestorUsuarios()

    # Crear usuarios
    usuario1 = Usuario("Mela", "U022", "mel145@gmail.com", "Premium")
    usuario2 = Usuario("Keren", "U023", "keren_m@gmail.com", "Básico")

    # Agregar usuarios al sistema
    gestor.agregar_usuario(usuario1)
    gestor.agregar_usuario(usuario2)

    # Mostrar los usuarios registrados
    gestor.mostrar_usuarios()

    # Eliminar un usuario
    gestor.eliminar_usuario("U022")

    # Mostrar usuarios después de la eliminación
    gestor.mostrar_usuarios()
