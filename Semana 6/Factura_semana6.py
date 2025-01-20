# Clase base: Producto
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Atributo protegido
        self._precio = precio  # Atributo protegido

    def calcular_precio(self):
        """Método para calcular el precio, se sobrescribirá en las clases derivadas."""
        return self._precio

    def mostrar_informacion(self):
        """Mostrar información básica del producto."""
        return f"Producto: {self._nombre}, Precio: ${self._precio:.2f}"


# Clase derivada: ProductoFisico
class ProductoFisico(Producto):
    def __init__(self, nombre, precio, costo_envio):
        super().__init__(nombre, precio)
        self._costo_envio = costo_envio  # Atributo protegido

    def calcular_precio(self):
        """Incluye el costo de envío en el precio final."""
        return self._precio + self._costo_envio

    def mostrar_informacion(self):
        """Mostrar información específica del producto físico."""
        info_base = super().mostrar_informacion()
        return f"{info_base}, Costo de envío: ${self._costo_envio:.2f}"


# Clase derivada: ProductoDigital
class ProductoDigital(Producto):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        self._descuento = descuento  # Atributo protegido

    def calcular_precio(self):
        """Aplica un descuento al precio final."""
        return self._precio - self._descuento

    def mostrar_informacion(self):
        """Mostrar información específica del producto digital."""
        info_base = super().mostrar_informacion()
        return f"{info_base}, Descuento: ${self._descuento:.2f}"


# Ejecución del programa
if __name__ == "__main__":
    # Crear instancias de las clases
    producto1 = ProductoFisico("Laptop", 1200, 7.50)
    producto2 = ProductoDigital("E-book", 20, 5)
    producto3 = ProductoFisico("Teclado Gammer", 95, 5)
    producto4 = ProductoFisico("Audifonos", 80, 5)

    # Mostrar información y calcular precios
    print(producto1.mostrar_informacion())
    print(f"Precio final: ${producto1.calcular_precio():.2f}\n")

    print(producto2.mostrar_informacion())
    print(f"Precio final: ${producto2.calcular_precio():.2f}\n")

    print(producto3.mostrar_informacion())
    print(f"Precio final: ${producto3.calcular_precio():.2f}\n")

    print(producto4.mostrar_informacion())
    print(f"Precio final: ${producto4.calcular_precio():.2f}")