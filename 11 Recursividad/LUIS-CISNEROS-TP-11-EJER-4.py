def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingresa un número entero positivo para convertir a binario: "))
if numero == 0:
    print("0")
else:
    print(f"Binario: {decimal_a_binario(numero)}")
