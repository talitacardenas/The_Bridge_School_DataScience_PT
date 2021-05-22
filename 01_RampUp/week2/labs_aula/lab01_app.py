# Creamos las variables del contador
from typing import final


try:
    print("¿Qué día es hoy?")
    date = input()
    print("Calorias desayuno")
    breakfast = int(input())
    print("Calorias comida")
    lunch = int(input())
    print("Calorias cena")
    dinner = int(input())
    print("Calorias merienda")
    snack = int(input())

    # Aqui calculamos el total de las calorias
    totalCal = breakfast + lunch + dinner + snack

    # Imprimimos el resultado
    print("El total de las calorías del día " + date + " son: " + str(totalCal) + " calorias.")
except Exception(e):
    print(e)
finally:
    print("Código ejecutado correctamente")
    pass