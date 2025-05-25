
# 5. Segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresa una cantidad de segundos: "))
print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos):.2f} horas")