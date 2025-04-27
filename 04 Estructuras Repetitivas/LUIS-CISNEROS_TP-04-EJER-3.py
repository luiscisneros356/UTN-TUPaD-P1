# Ejercicio 3: Sumar números entre dos valores
inicio = int(input("Ingresa el primer valor: "))
fin = int(input("Ingresa el segundo valor: "))


menor = min(inicio, fin)
mayor = max(inicio, fin)

# Sumamos los valores entre menor y mayor, excluyendo los extremos
suma = 0
for i in range(menor + 1, mayor):
    suma += i

print(f"La suma de los números entre {inicio} y {fin} (excluyéndolos) es: {suma}")