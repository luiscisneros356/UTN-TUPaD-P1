# Ejercicio 8: Contar pares, impares, positivos y negativos
cantidad = 100  
pares = impares = positivos = negativos = 0

for _ in range(cantidad):
    numero = int(input("Ingresa un número entero: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
