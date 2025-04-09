import random
from statistics import mean, median, mode


# Ejercicio 1
edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")



# Ejercicio 2

nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# Ejercicio 3


numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# Ejercicio 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Ejercicio 5
contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6



numeros_aleatorios = [random.randint(1, 100) for i in range(50)]


media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)


print("Números aleatorios:", numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")


if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")


# Ejercicio 7


frase = input("Ingrese una frase o palabra: ")

if frase[-1].lower() in "aeiou":
    frase += "!"
    
print("Resultado:", frase)


# Ejercicio 8

nombre = input("Ingrese su nombre: ")

print("Elija una opción:")
print("1. Convertir a MAYÚSCULAS")
print("2. Convertir a minúsculas")
print("3. Capitalizar (Primera letra mayúscula)")

opcion = input("Ingrese 1, 2 o 3: ")

if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida.")


# Ejercicio 9

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")


# Ejercicio 10


hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes (1-31): "))


fecha = (mes, dia)

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

print("Estación del año:", estacion)
