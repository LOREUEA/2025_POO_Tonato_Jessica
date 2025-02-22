import os #Para manejar los archivos y verificar existencias de stock

class Producto:
    '''Clase que representa un producto en el inventario'''
    def __init__(self, id_producto, nombre, precio, fecha_ingreso, cantidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.fecha_ingreso = fecha_ingreso
        self.cantidad = cantidad

    def to_line(self):
        '''Convierte un producto en una línea de texto para el archivo.'''
        return f'{self.id_producto}, {self.nombre}, {self.precio}, {self.fecha_ingreso}, {self.cantidad}\n'

    @staticmethod
    def from_line(line):
        '''Crea un producto con un line de texto.'''
        datos = line.split(',')
        return Producto(datos[0], datos[1], float(datos[2]), datos[3], int(datos[4]))

    def __str__(self):
        return (f"🆔 ID: {self.id_producto} | 📦 Producto: {self.nombre} | "
                f"💲 Precio: ${self.precio:.2f} | 📅 Ingreso: {self.fecha_ingreso} | "
                f"📦 Cantidad: {self.cantidad}")

class Inventario:
    '''Clase que gestiona el inventario y la manipulación de archivos.'''

    ARCHIVO = 'inventario.txt'  # Nombre del archivo donde se almacena el inventario

    def cargar_inventario(self):
        '''Carga los productos desde el archivo si existe.'''
        if os.path.exists(self.ARCHIVO):  # Verifica si el archivo existe
            try:
                with open(self.ARCHIVO, "r") as file:
                    self.productos = [Producto.from_line(line) for line in file]
                print("📂 Inventario cargado correctamente.")
            except FileNotFoundError:
                print("⚠️ Archivo de inventario no encontrado, se creará uno nuevo.")
            except Exception as e:
                print(f"❌ Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        '''Guarda el inventario en un archivo de texto.'''
        try:
            with open(self.ARCHIVO, "w") as file:
                for producto in self.productos:
                    file.write(producto.to_line())
            print("💾 Inventario guardado correctamente.")
        except PermissionError:
            print("❌ Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"❌ Error inesperado al guardar el inventario: {e}")

    def menu():
        '''Menú interactivo para gestionar el inventario.'''

        inventario = Inventario()

        while True:
            print("\n📋 Menú de Gestión de Inventario")
            print("1️⃣ Añadir Producto")
            print("2️⃣ Eliminar Producto")
            print("3️⃣ Actualizar Producto")
            print("4️⃣ Buscar Producto por Nombre")
            print("5️⃣ Mostrar Todos los Productos")
            print("6️⃣ Salir")

            opcion = input("🔹 Selecciona una opción: ")

            if opcion == "1":
                try:
                    id_producto = input("🔹 ID del producto: ")
                    nombre = input("🔹 Nombre del producto: ")
                    precio = float(input("🔹 Precio: "))
                    fecha_ingreso = input("🔹 Fecha de ingreso (YYYY-MM-DD): ")
                    cantidad = int(input("🔹 Cantidad: "))
                    inventario.agregar_producto(id_producto, nombre, precio, fecha_ingreso, cantidad)
                except ValueError:
                    print("❌ Error: Ingresa números válidos para precio y cantidad.")


            elif opcion == "2":
                id_producto = input("🔹 ID del producto a eliminar: ")
                inventario.eliminar_producto(id_producto)

            elif opcion == "3":
                try:
                    id_producto = input("🔹 ID del producto a actualizar: ")
                    cantidad = input("🔹 Nueva cantidad (dejar vacío para no cambiar): ")
                    precio = input("🔹 Nuevo precio (dejar vacío para no cambiar): ")
                    cantidad = int(cantidad) if cantidad else None
                    precio = float(precio) if precio else None
                    inventario.actualizar_producto(id_producto, cantidad, precio)
                except ValueError:
                    print("❌ Error: Ingresa números válidos para precio y cantidad.")

            elif opcion == "4":
                nombre = input("🔹 Nombre del producto a buscar: ")
                inventario.buscar_producto(nombre)

            elif opcion == "5":
                inventario.mostrar_productos()

            elif opcion == "6":
                print("👋 Saliendo del sistema. ¡Hasta luego!")
                break

            else:
                print("❌ Opción inválida. Intenta nuevamente.")
