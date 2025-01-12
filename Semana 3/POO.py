# Creación de una clase para la información diaria del clima
class Dia:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def __str__(self):
        return f'Temperatura: {self.temperatura}°C'

# Función para calcular el promedio semanal de temperaturas
def calcular_promedio_semanal(dias):
    temperaturas = [dia.temperatura for dia in dias]
    return sum(temperaturas) / len(temperaturas)

# Creación de objetos Dia
dias_semana = []
for _ in range(7):
    while True:
        try:
            temperatura = float(input("Ingrese la temperatura: "))
            break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("Por favor, ingrese un número válido.")
    dia = Dia(temperatura)  # Uso correcto de la clase
    dias_semana.append(dia)

# Cálculo del promedio
promedio = calcular_promedio_semanal(dias_semana)
print("El promedio de temperatura semanal es:", promedio)
