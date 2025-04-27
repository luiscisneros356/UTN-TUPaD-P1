# Ejercicio 2: Contar los dígitos de un número
numero = int(input("Ingresa un número entero: "))
cantidad_digitos = len(str(abs(numero)))  
print(f"El número tiene {cantidad_digitos} dígitos.")