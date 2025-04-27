# Ejercicio 5: Juego de adivinar el número
import random

numero_secreto = random.randint(0, 9)
intentos = 0

print("¡Adivina el número secreto entre 0 y 9!")

while True:
    adivinanza = int(input("Ingresa tu número: "))
    intentos += 1
    if adivinanza == numero_secreto:
        print(f"¡Felicidades! Adivinaste en {intentos} intentos.")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")
