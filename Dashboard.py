import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
            print("\n--- Fin del archivo ---\n")
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Se muestra un menú interactivo para navegar y mostrar el contenido
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Semana 2/Ejemplo_Tecnicas_de_Programacion.py',
        '2': 'Semana 3/POO.py',
        '3': 'Semana 3/Programacion_tradicional.py',
        '4': 'Semana 4_EjemplosMundoReal_POO/factura.py',
        '5': 'Semana 4_EjemplosMundoReal_POO/inventario.py',
        '6': 'Semana 6/Factura_semana6.py',
        '7': 'Semana 7/Contructores_destructores.py',
    }

    while True:
        print("\n********📁 MENÚ PRINCIPAL - DASHBOARD 📂*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script 🔢 para ver su código o '0' para salir: ")
        if eleccion == '0':
            print("¡😊Gracias por usar el dashboard! ✌️")
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
            #Agregamos un submenú después de mostrar el contenido del archivo seleccionado
            while True:
                print("\n¿Qué deseas hacer ahora 🤔?")
                print("1- Volver al menú principal")
                print("2- Salir")
                accion = input("Elige una opción: ")

                if accion == '1':
                    break #Nos regresará al menú principal
                elif accion == '2':
                    print("¡Gracias por usar el dashboard! 👋")
                    return #Sale completamente del programa
                else:
                    print("Opción no válida 🤯. Intenta nuevamente 😉")
        else:
            print(f"La opción {eleccion} no es válida 😒. Intenta con un número entre 0 y {len(opciones)} 🤫.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
    print("\n--- Fin del archivo ---\n")


