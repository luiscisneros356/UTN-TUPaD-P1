
# 10. Calcular promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))
promedio = calcular_promedio(n1, n2, n3)
print(f"El promedio es: {promedio:.2f}")