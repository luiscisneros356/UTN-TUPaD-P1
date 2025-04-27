# Ejercicio 9: Calcular la media de 100 números
cantidad = 100  
suma = 0

for _ in range(cantidad):
    numero = int(input("Ingresa un número entero: "))
    suma += numero

media = suma / cantidad
print(f"La media de los números ingresados es: {media}")
