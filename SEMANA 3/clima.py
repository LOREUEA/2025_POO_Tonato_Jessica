# Ingresaremos funciones para las temperaturas diarias, para cumplir
# con una programación tradicional:

def main():
    print('Cálculo del promedio semanal del clima')
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    mostrar_resultados(promedio)

def ingresar_temperaturas():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = {}  # Usamos un diccionario para asociar días con temperaturas
    for dia in dias:
        while True:
            try:
                temp = float(input(f"Por favor ingresa la temperatura para {dia}: "))
                temperaturas[dia] = temp  # Guardamos la temperatura asociada al día
                break
            except ValueError:
                print('Error: Por favor 🥺, ingresa un número válido.')
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas.values()) / len(temperaturas)

def mostrar_resultados(promedio):
    print(f'El promedio de temperatura semanal es: {promedio:.2f}')

main()