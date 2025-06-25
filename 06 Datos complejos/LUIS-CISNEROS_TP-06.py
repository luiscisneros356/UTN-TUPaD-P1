# funciones auxiliares
# Se utiliza un formato especial para dar color a la salida
# Se importa la librería colorama para dar color a la salida

# imports
from colorama import init, Fore, Style
from collections import deque
import math

# Inicializa Colorama
init(autoreset=True)

def print_header():
    # Imprime el encabezado del programa
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)
    print(Fore.CYAN + Style.BRIGHT + r"""
    .----------------------.
    |                      |
    |  U   U TTTTTT N   N  |
    |  U   U   TT   NN  N  |
    |  U   U   TT   N N N  |
    |  U   U   TT   N  NN  |
    |   UUU    TT   N   N  |
    |                      |
    '----------------------'
    """)
    print(Fore.CYAN + Style.BRIGHT + "Universidad Tecnológica Nacional")
    print(Fore.CYAN + Style.BRIGHT + "Campoy Guillermo")
    print(Fore.CYAN + Style.BRIGHT + "Comisión 11")
    print(Fore.CYAN + Style.BRIGHT + "Abril 2025")
    print(Fore.CYAN + Style.BRIGHT + "=" * 60)
print()

def print_separator(title="Ejercicio XXX"):
    # Espacio en blanco
    print()
    # Imprime un separador con el título dado
    print(Fore.YELLOW + "-" * 60)
    print(Fore.YELLOW + f"{title.center(60)}")
    print(Fore.YELLOW + "-" * 60)


def print_footer():
    # Imprime el pie de página del programa
    print()
    print(Fore.GREEN + Style.BRIGHT + "=" * 60)
    print(Fore.GREEN + Style.BRIGHT + "¡Fin de la ejecución!".center(60))
    print(Fore.GREEN + Style.BRIGHT + "=" * 60)
    print()

# clases

class Persona:
    # Clase Persona
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar (self):
        return f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años."

class Circulo:
    # Clase Circulo
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Pila:
    # Clase Pila
    # Solo se define constructor y metodo de igualdad
    # con una máscara dada

    mascara = ["(", "{", "[", "]", "}", ")"]
    def __init__(self, *elementos):
        self.pila = list(elementos)

    def ver_pila(self):
        return self.pila
    
    def igual_a_mascara(self):
        if self.pila == self.mascara:
            return True
        else:
            return False

class Cola:
    # Clase con uso de claso deque
    # Se utiliza deque para implementar la cola

    def __init__(self):
        self.elementos = deque() 

    def agregar_cliente(self, elemento):
        self.elementos.append(elemento)

    def atender_cliente(self):
        return self.elementos.popleft() if not self.esta_vacia() else "La cola está vacía"

    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def ver_cola(self):
        return self.elementos
    
    def siguiente_cliente(self):
        return self.elementos[0] if not self.esta_vacia() else "La cola está vacía"

class Nodo:
    def __init__(self, dato):
        self.dato = dato  
        self.siguiente = None  

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:  # Traverse the list, reversing the direction of the links one node at a time
            print(actual.dato, end=' --> ')
            actual = actual.siguiente
        print("None")
    
    def invertir_lista(self):
        anterior = None
        actual = self.cabeza

        while actual:
            siguiente = actual.siguiente # Guardar el siguiente nodo   
            actual.siguiente = anterior # Invertir el enlace  
            anterior = actual  # Mover el puntero anterior hacia adelante
            actual = siguiente  # Mover el puntero actual hacia adelante

        self.cabeza = anterior  # Actualizar la cabeza de la lista


# programa principal
print_header()

# Ejercicio 1 uso de diccionarios
print_separator("Actividad 1 - Uso de diccionarios")

precios_frutas = {
    "Banana": 1200,
    "Ananá": 2500,
    "Melón": 3000,
    "Uva": 1450,
}

print(Fore.YELLOW + Style.BRIGHT + "Frutas y precios (estado inicial):")
for fruta, precio in precios_frutas.items():
    print(Fore.BLUE + Style.BRIGHT + f"{fruta}: ${precio}")

# Se propone añadir nuevas frutas con nuevos precios
precios_frutas.update({
    "Naranja": 1200,
    "Manzana": 1500,
    "Pera": 2300,
})
print()
print(Fore.YELLOW + Style.BRIGHT + "Frutas y precios (estado final):")
for fruta, precio in precios_frutas.items():
    print(Fore.GREEN + Style.BRIGHT + f"{fruta}: ${precio}")

# Ejercicio 2 continuación punto 1 con actualización de precios
print_separator("Actividad 2 - Actualización de precios")

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print()
print(Fore.YELLOW + Style.BRIGHT + "Frutas y precios (actualización ejercicio 2):")
for fruta, precio in precios_frutas.items():
    print(Fore.GREEN + Style.BRIGHT + f"{fruta}: ${precio}")

# Ejercicio 3 creación de lista solo con keys de diccionario
print_separator("Actividad 3 - Lista de claves")
# Se crea una lista con las claves del diccionario
lista_frutas = list(precios_frutas.keys())
print(Fore.YELLOW + Style.BRIGHT + "Lista de frutas:")
for fruta in lista_frutas:
    print(Fore.GREEN + Style.BRIGHT + fruta)

# Ejericio 4 uso de clase persona
print_separator("Actividad 4 - Clase Persona")

persona = Persona("Guillermo", "Argentina", 41)
print(Fore.GREEN + Style.BRIGHT + persona.saludar())

# Ejercicio 5 uso de clase circulo
print_separator("Actividad 5 - Clase Circulo")

# Se define un número arbitrario para el radio
radio = 5
circulo = Circulo(radio)
area = circulo.calcular_area()
perimetro = circulo.calcular_perimetro()

print(Fore.YELLOW + Style.BRIGHT + f"Radio del círculo: {radio}")
print(Fore.GREEN + Style.BRIGHT + f"Área del círculo: {area:.2f}")
print(Fore.GREEN + Style.BRIGHT + f"Perímetro del círculo: {perimetro:.2f}")

# Ejericio 6 determinar orden de caracteres en una pila
print_separator("Actividad 6 - Orden de caracteres en una pila")

# Se debe validar que el orden de los caracteres en la pila sea igual a la mascara
# Se define la clase pila, con una mascara dada y metodo de igualdad
pila_ordenada = Pila("(", "{", "[", "]", "}", ")")
pila_desordenada = Pila("(", "{", "]", "}", ")", "[")
otra_pila_desordenada = Pila("(", "{", "[", "}", "}", "}")

print(Fore.YELLOW + Style.BRIGHT + "Resultados Pilas dadas:")
print()
print(Fore.BLUE + Style.BRIGHT + "Primer Pila:")
print(Fore.YELLOW + Style.BRIGHT + str(pila_ordenada.ver_pila()))
if pila_ordenada.igual_a_mascara():
    print(Fore.GREEN + Style.BRIGHT + "La pila está ordenada correctamente.")
else:
    print(Fore.RED + Style.BRIGHT + "La pila no está ordenada correctamente.")

print()
print(Fore.BLUE + Style.BRIGHT + "Segunda Pila:")
print(Fore.YELLOW + Style.BRIGHT + str(pila_desordenada.ver_pila()))
if pila_desordenada.igual_a_mascara():
    print(Fore.GREEN + Style.BRIGHT + "La pila está ordenada correctamente.")
else:
    print(Fore.RED + Style.BRIGHT + "La pila no está ordenada correctamente.")

print()
print(Fore.BLUE + Style.BRIGHT + "Tercera Pila:")
print(Fore.YELLOW + Style.BRIGHT + str(otra_pila_desordenada.ver_pila()))
if otra_pila_desordenada.igual_a_mascara():
    print(Fore.GREEN + Style.BRIGHT + "La pila está ordenada correctamente.")
else:
    print(Fore.RED + Style.BRIGHT + "La pila no está ordenada correctamente.")

# Ejercicio 7 uso de Cola para simular atención en un lugar
print_separator("Actividad 7 - Uso de Cola")

#inicializamos una nueva cola vacía
cola_clientes = Cola()

# Agregamos clientes a la cola
cola_clientes.agregar_cliente("Cliente 1")
cola_clientes.agregar_cliente("Cliente 2")
cola_clientes.agregar_cliente("Cliente 3")
cola_clientes.agregar_cliente("Cliente 4")
cola_clientes.agregar_cliente("Cliente 5")

#Listado estado actual de cola
print(Fore.YELLOW + Style.BRIGHT + "Estado actual de la cola:")
print(Fore.BLUE + Style.BRIGHT + f"{cola_clientes.ver_cola()}")

print()
#Atender cliente
cola_clientes.atender_cliente()
print(Fore.YELLOW + Style.BRIGHT + "Atención de cliente en curso...")

#siguiente en la fila
print(Fore.BLUE + Style.BRIGHT + "Siguiente cliente en la cola:")
print(Fore.GREEN + Style.BRIGHT + f"{cola_clientes.siguiente_cliente()}")

# Ejericio 8 uso de lista enlazada
print_separator("Actividad 8 - Uso de lista enlazada")

lista_enlazada = ListaEnlazada()
lista_enlazada.insertar("Elemento 5")
lista_enlazada.insertar("Elemento 4")
lista_enlazada.insertar("Elemento 3")
lista_enlazada.insertar("Elemento 2")
lista_enlazada.insertar("Elemento 1")
lista_enlazada.insertar("Elemento 0")

#presentamos la lista enlazada
print(Fore.GREEN + Style.BRIGHT + "Lista enlazada:")
lista_enlazada.mostrar()

# Ejercicio 9 implementar funcion para invertir lista enlazada
print_separator("Actividad 9 - Invertir lista enlazada")

# Tomamos la lista ya cargada del ejercicio 8 y la invertimos
lista_invertida = ListaEnlazada()

# Realizamos una copia de la lista anterior
lista_invertida = lista_enlazada
lista_invertida.invertir_lista()
print(Fore.GREEN + Style.BRIGHT + "Lista enlazada invertida:")
lista_invertida.mostrar()

print_footer()