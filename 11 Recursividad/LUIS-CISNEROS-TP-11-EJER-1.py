def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


numero = int(input("Ingresa un número entero positivo para calcular los factoriales desde 1 hasta ese número: "))

print("Factoriales:")
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")
