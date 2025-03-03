class Inventario:
    '''Clase que gestiona el inventario y la manipulación de archivos.'''

    ARCHIVO = 'inventario.txt'  # Nombre del archivo donde se almacena el inventario

    def __init__(self):
        '''Inicializa el inventario como una lista vacía y carga los productos.'''
        self.productos = []  # Lista vacía para almacenar los productos
        self.cargar_inventario()
class Inventario:

    def menu(self):
        '''Menú interactivo para gestionar el inventario.'''
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
                    self.agregar_producto(id_producto, nombre, precio, fecha_ingreso, cantidad)
                except ValueError:
                    print("❌ Error: Ingresa números válidos para precio y cantidad.")

            elif opcion == "2":
                id_producto = input("🔹 ID del producto a eliminar: ")
                self.eliminar_producto(id_producto)

            elif opcion == "3":
                try:
                    id_producto = input("🔹 ID del producto a actualizar: ")
                    cantidad = input("🔹 Nueva cantidad (dejar vacío para no cambiar): ")
                    precio = input("🔹 Nuevo precio (dejar vacío para no cambiar): ")
                    cantidad = int(cantidad) if cantidad else None
                    precio = float(precio) if precio else None
                    self.actualizar_producto(id_producto, cantidad, precio)
                except ValueError:
                    print("❌ Error: Ingresa números válidos para precio y cantidad.")

            elif opcion == "4":
                nombre = input("🔹 Nombre del producto a buscar: ")
                self.buscar_producto(nombre)

            elif opcion == "5":
                self.mostrar_productos()

            elif opcion == "6":
                print("👋 Saliendo del sistema. ¡Hasta luego!")
                break

            else:
                print("❌ Opción inválida. Intenta nuevamente.")
    def agregar_producto(self, id_producto, nombre, precio, fecha_ingreso, cantidad):
        '''Añade un producto al inventario y lo guarda en el archivo.'''
        for producto in self.productos:
            if producto.id_producto == id_producto:
                print("❌ Error: Ya existe un producto con este ID.")
                return

        nuevo_producto = Producto(id_producto, nombre, precio, fecha_ingreso, cantidad)
        self.productos.append(nuevo_producto)
        self.guardar_inventario()
        print(f"✅ Producto '{nombre}' añadido con ID: {id_producto}")

    def eliminar_producto(self, id_producto):
        '''Elimina un producto por ID.'''
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                self.guardar_inventario()
                print(f"🗑️ Producto con ID {id_producto} eliminado.")
                return
        print("❌ Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        '''Actualiza un producto en el inventario.'''
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if nueva_cantidad is not None:
                    producto.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    producto.precio = nuevo_precio
                self.guardar_inventario()
                print("🔄 Producto actualizado correctamente.")
                return
        print("❌ Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        '''Busca productos por nombre.'''
        encontrados = [producto for producto in self.productos if nombre.lower() in producto.nombre.lower()]
        if encontrados:
            print("🔍 Productos encontrados:")
            for producto in encontrados:
                print(producto)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        '''Muestra todos los productos en el inventario.'''
        if not self.productos:
            print("📭 Inventario vacío.")
        else:
            print("\n📦 Lista de Productos:")
            for producto in self.productos:
                print(producto)
if __name__ == "__main__":
    inventario = Inventario()
    inventario.menu()
