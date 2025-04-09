

import math

print("Hola Mundo!")

##########################


nombre = input("Por favor, ingrese su nombre: ")

print(f"Hola {nombre}!")

print("Hola " + nombre + "!")

##########################


nombre2 = input("Por favor, ingrese su nombre: ")


apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
lugar_de_residencia = input("Por favor, ingrese su lugar de residencia: ")

print(f"Soy {nombre2} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}.")

##########################



radio_circulo = float(input("Por favor, ingrese el radio del círculo: "))


area_circulo = math.pi * (radio_circulo)**2

perimetro_circulo = 2 * math.pi * radio_circulo

print(f"El área del círculo es de {area_circulo} y el perímetro es de {perimetro_circulo}.")


##########################

radio_circulo2 = float(input("Por favor, ingrese el radio del círculo: "))


area_circulo2 = round(math.pi * (radio_circulo2)**2, 2)


perimetro_circulo2 = round(2 * math.pi * radio_circulo2, 2)

print(f"El área del círculo es de {area_circulo2} y el perímetro es de {perimetro_circulo2}.")

##########################

cantidad_segundos = float(input("Por favor, ingrese la cantidad de segundos a convertir: "))

cantidad_horas = round(cantidad_segundos / 3600, 2)

print(f"El equivalente a {cantidad_segundos} segundos son {cantidad_horas} horas.")



##########################
numero_a_multiplicar = int(input("Por favor, ingrese un número entero: "))

numero_por_0 = numero_a_multiplicar * 0
numero_por_1 = numero_a_multiplicar * 1
numero_por_2 = numero_a_multiplicar * 2
numero_por_3 = numero_a_multiplicar * 3
numero_por_4 = numero_a_multiplicar * 4
numero_por_5 = numero_a_multiplicar * 5
numero_por_6 = numero_a_multiplicar * 6
numero_por_7 = numero_a_multiplicar * 7
numero_por_8 = numero_a_multiplicar * 8
numero_por_9 = numero_a_multiplicar * 9


print(f"""
  {numero_a_multiplicar} x 0 = {numero_por_0}
  {numero_a_multiplicar} x 1 = {numero_por_1}
  {numero_a_multiplicar} x 2 = {numero_por_2}
  {numero_a_multiplicar} x 3 = {numero_por_3}
  {numero_a_multiplicar} x 4 = {numero_por_4}
  {numero_a_multiplicar} x 5 = {numero_por_5}
  {numero_a_multiplicar} x 6 = {numero_por_6}
  {numero_a_multiplicar} x 7 = {numero_por_7}
  {numero_a_multiplicar} x 8 = {numero_por_8}
  {numero_a_multiplicar} x 9 = {numero_por_9}
      """)


##########################

numero_a_multiplicar2 = int(input("Por favor, ingrese un número entero: "))

print(f"""
  {numero_a_multiplicar2} x 0 = {numero_a_multiplicar2 * 0}
  {numero_a_multiplicar2} x 1 = {numero_a_multiplicar2 * 1}
  {numero_a_multiplicar2} x 2 = {numero_a_multiplicar2 * 2}
  {numero_a_multiplicar2} x 3 = {numero_a_multiplicar2 * 3}
  {numero_a_multiplicar2} x 4 = {numero_a_multiplicar2 * 4}
  {numero_a_multiplicar2} x 5 = {numero_a_multiplicar2 * 5}
  {numero_a_multiplicar2} x 6 = {numero_a_multiplicar2 * 6}
  {numero_a_multiplicar2} x 7 = {numero_a_multiplicar2 * 7}
  {numero_a_multiplicar2} x 8 = {numero_a_multiplicar2 * 8}
  {numero_a_multiplicar2} x 9 = {numero_a_multiplicar2 * 9}
      """)


##########################

numero_a = float(input("Por favor, ingrese un número distinto de 0: "))
numero_b = float(input("Por favor, ingrese otro número distinto de 0: "))

suma_a_b = numero_a + numero_b

division_a_b = round(numero_a / numero_b, 2)

multiplicacion_a_b = numero_a * numero_b

resta_a_b = numero_a - numero_b

print(f"""
  Resultado de la suma: {suma_a_b}
  Resultado de la división: {division_a_b}
  Resultado de la multiplicación: {multiplicacion_a_b}
  Resultado de la resta: {resta_a_b}
      """)


##########################

peso = float(input("Por favor, ingrese su peso en kilogramos: "))
altura = float(input("Por favor, ingrese su altura en metros: "))

imc = round(peso / altura**2, 2)

print(f"Su IMC es de: {imc}.")


##########################

temperatura_celsius = float(input("Por favor, una temperatura en °C: "))

temperatura_fahrenheit = round((9/5)*temperatura_celsius+32, 2)

print(f"{temperatura_celsius} °C equivalen a {temperatura_fahrenheit} °F.")


##########################

numero_a = float(input("Por favor, ingrese el primer número: "))
numero_b = float(input("Por favor, ingrese el segundo número: "))
numero_c = float(input("Por favor, ingrese el tercer número: "))

suma_a_b_c = numero_a + numero_b + numero_c

promedio_a_b_c = round(suma_a_b_c/3, 2)

print(f"El promedio de los números ingresados es {promedio_a_b_c}.")


