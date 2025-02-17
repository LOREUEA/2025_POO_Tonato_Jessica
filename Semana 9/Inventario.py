# Crearemos un sistema de inventarios simple para una tienda

class Producto:
    def __init__(self, id_producto, nombre, precio, fecha_ingreso, cantidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.fecha_ingreso = fecha_ingreso
        self.cantidad = cantidad

    # Getters
    def get_id_producto(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    def get_fecha_ingreso(self):
        return self.fecha_ingreso

    def get_cantidad(self):
        return self.cantidad

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_precio(self, precio):
        self.precio = precio

    def set_fecha_ingreso(self, fecha_ingreso):
        self.fecha_ingreso = fecha_ingreso

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def __str__(self):
        return (f"🆔 ID: {self.id_producto} | 📦 Producto: {self.nombre} | "
                f"💲 Precio: ${self.precio:.2f} | 📅 Ingreso: {self.fecha_ingreso} | "
                f"📦 Cantidad: {self.cantidad}")

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, id_producto, nombre, precio, fecha_ingreso, cantidad):
        # Verificar si el ID ya existe en el inventario
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                print("❌ Error: Ya existe un producto con este ID.")
                return

        nuevo_producto = Producto(id_producto, nombre, precio, fecha_ingreso, cantidad)
        self.productos.append(nuevo_producto)
        print(f"✅ Producto '{nombre}' añadido con ID: {id_producto}")


    def eliminar_producto(self, id_producto):
        #Elimina un producto del inventario por su ID

        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                self.productos.remove(producto)
                print(f"🗑️ Producto con ID {id_producto} eliminado.")
                return
        print("❌ Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):

        #Actualiza la cantidad o el precio de un producto por su ID

        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print("🔄 Producto actualizado correctamente.")
                return
        print("❌ Error: Producto no encontrado.")

    def buscar_producto(self, nombre):

        #Busca productos por nombre (puede haber nombres similares).

        encontrados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        if encontrados:
            print("🔍 Productos encontrados:")
            for producto in encontrados:
                print(producto)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_productos(self):

        #Muestra todos los productos en el inventario.

        if not self.productos:
            print("📭 Inventario vacío.")
        else:
            print("\n📦 Lista de Productos:")
            for producto in self.productos:
                print(producto)

def menu():
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
                print("❌ Error: Entrada inválida. Asegúrate de ingresar números para precio y cantidad.")

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
                print("❌ Error: Entrada inválida. Asegúrate de ingresar números para precio y cantidad.")

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