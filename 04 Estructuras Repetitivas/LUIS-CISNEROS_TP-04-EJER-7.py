# Ejercicio 7: Suma de 0 hasta un número dado
numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("Debe ser un número positivo.")
else:
    suma = sum(range(numero + 1))
    print(f"La suma de los números de 0 a {numero} es: {suma}")
