def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


numero = int(input("Ingresa un número entero positivo: "))
digito = int(input("¿Qué dígito quieres contar (0-9)?: "))
print("Cantidad de veces que aparece:", contar_digito(numero, digito))
