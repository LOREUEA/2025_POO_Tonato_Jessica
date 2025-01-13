# Crearemos un inventario usando el método PEPS

# Creamos la clase Producto
class Producto:
    def __init__(self, nombre, precio, fecha_ingreso, cantidad):
        self.nombre = nombre  # Asignaremos un nombre del producto
        self.precio = precio  # Asignaremos un precio por unidad
        self.fecha_ingreso = fecha_ingreso  # Registraremos la fecha de ingreso al inventario
        self.cantidad = cantidad  # Cantidad disponible

    def __str__(self):
        # Representación en texto del producto
        return (f'Producto: {self.nombre}, Precio: $ {self.precio:.2f}, '
                f'Fecha Ingreso: {self.fecha_ingreso}, Cantidad: {self.cantidad}')


# Creamos la clase Inventario
class Inventario:
    def __init__(self):
        # Generamos una lista para almacenar los lotes de productos
        self.productos = []

    def agregar_producto(self, producto):
        # Agregaremos un nuevo lote de producto al inventario
        if isinstance(producto, Producto):
            self.productos.append(producto)
        else:
            raise ValueError('Producto no válido')

    def mostrar_inventario(self):
        # Muestra todos los productos en el inventario
        if not self.productos:
            print('No hay productos')
        else:
            print('Inventario actual:')
            for producto in self.productos:
                print(producto)

    def actualizar_stock(self, nombre_producto, cantidad_vendida):
        # Actualiza el stock de un producto según el método PEPS
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.cantidad >= cantidad_vendida:
                    producto.cantidad -= cantidad_vendida
                    print(f"Se han vendido {cantidad_vendida} unidades de {nombre_producto}.")
                    return
                else:
                    cantidad_vendida -= producto.cantidad
                    print(f"Se han vendido {producto.cantidad} unidades del lote de {nombre_producto}.")
                    producto.cantidad = 0  # Este lote se agota
        print("No hay suficientes productos en el inventario.")


# Crear un registro del inventario
inventario = Inventario()

# Agregar productos al inventario
producto1 = Producto("Leche Deslactosada", 1.06, "2024-12-30", 100)
producto2 = Producto("Sal Crisal", 0.56, "2024-12-15", 150)
producto3 = Producto("Cereal Chocapic", 7.16, "2025-01-03", 72)

inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)

# Mostrar el inventario
inventario.mostrar_inventario()

# Actualizar el stock usando el método PEPS
inventario.actualizar_stock("Leche Deslactosada", 80)
inventario.actualizar_stock("Sal Crisal", 99)
inventario.actualizar_stock("Cereal Chocapic", 60)

# Mostrar el inventario nuevamente
inventario.mostrar_inventario()

