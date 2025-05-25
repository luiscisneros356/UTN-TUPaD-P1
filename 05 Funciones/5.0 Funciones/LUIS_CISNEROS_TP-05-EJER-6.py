
# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)
