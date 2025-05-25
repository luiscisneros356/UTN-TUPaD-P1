def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingresa una posición para mostrar la serie de Fibonacci hasta ese punto: "))

print("Serie de Fibonacci:")
for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")