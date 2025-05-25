def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


niveles = int(input("Ingresa la cantidad de bloques en el nivel más bajo: "))
print("Total de bloques necesarios:", contar_bloques(niveles))
