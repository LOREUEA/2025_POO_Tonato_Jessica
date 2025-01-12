#Crearemos una factura de consumo de alimentos
class Factura:
    def __init__(self, descripcion, subtotal, descuento):
        self.descripcion = descripcion
        self.subtotal = subtotal
        self.descuento = descuento
        self.iva = None  # Asignamos un porcentaje de IVA, dependiendo del producto
        self.total = subtotal - descuento #Calculamos automaticamente el total

    def asignar_iva(self, iva):
        if isinstance(iva, Iva):
            self.iva = iva

    def __str__(self):
        iva_valor = f'{self.iva.valor * 100:.0f}%' if self.iva else 'No asignado' #He usado .0f para mostrar valores
        # enteros, para representar los valores porcentuales
        return (
            f'Factura: {self.descripcion}\n'
            f'Subtotal: ${self.subtotal:.2f}\n' #He usado .2f para mostrar valores monetarios con 2 decimales
            f'Descuento: ${self.descuento:.2f}\n'
            f'IVA: {iva_valor}\n'
            f'Total: ${self.total:.2f}'
        )

class Iva:
    def __init__(self, producto, valor):
        self.producto = producto
        self.valor = valor #Representa el porcentaje

    def __str__(self):
        return f'IVA para {self.producto}: {self.valor * 100:.0f}%'

#Creamos los objetos de Factura
factura1 = Factura('Leche Deslactosada Funda 900Ml', 1.06, 0.00)
factura2 = Factura('Sal Crisal 1Kg', 0.53, 0.00)
factura3 = Factura('Cereal Chocapic 720G', 7.16, 1.07)

#Creamos objetos del IVA
iva1 = Iva('Alimentos', 0.0) #IVA 0%
iva2 = Iva('Alimentos', 0.15) #IVA 15%

#Asignar un IVA a la Factura
factura1.asignar_iva(iva1)
factura2.asignar_iva(iva1)
factura3.asignar_iva(iva2)

#Imprimimos nuestra informacion de la factura
print(factura1, end="\n\n")
print(factura2, end="\n\n")
print(factura3, end="\n\n")

#Forma 2: Carrito de compras
# Clase Producto que representa un artículo individual
class Producto:
    def __init__(self, nombre, precio, descuento=0):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento

    def __str__(self):
        return (
            f"{self.nombre}: ${self.precio:.2f} "
            f"(Descuento: ${self.descuento:.2f})"
        )

# Clase Factura que representa un conjunto de productos
class Factura:
    def __init__(self):
        self.productos = []  # Lista para almacenar productos

    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            self.productos.append(producto)
        else:
            raise ValueError("Solo se pueden agregar objetos de la clase Producto")

    def calcular_total(self):
        subtotal = sum(p.precio for p in self.productos)
        total_descuentos = sum(p.descuento for p in self.productos)
        total = subtotal - total_descuentos
        return subtotal, total_descuentos, total

    def __str__(self):
        productos_str = "\n".join(str(p) for p in self.productos)
        subtotal, total_descuentos, total = self.calcular_total()
        return (
            f"Productos en la factura:\n{productos_str}\n\n"
            f"Subtotal: ${subtotal:.2f}\n"
            f"Total Descuentos: ${total_descuentos:.2f}\n"
            f"Total General: ${total:.2f}"
        )

# Ejemplo de uso
# Crear productos
producto1 = Producto("Leche Deslactosada", 1.06, 0.10)
producto2 = Producto("Sal Crisal", 0.53, 0.00)
producto3 = Producto("Cereal Chocapic", 7.16, 1.07)

# Crear factura y agregar productos
factura = Factura()
factura.agregar_producto(producto1)
factura.agregar_producto(producto2)
factura.agregar_producto(producto3)

# Imprimir factura con el total general
print(factura)
