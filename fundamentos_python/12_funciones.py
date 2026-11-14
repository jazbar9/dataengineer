
""" Definición de funciones """
def saludar():
    print("Hola")
    
""" Llamada a la función """
saludar()

""" Definición de funciones con parámetros """
def sumar (a, b):
    return a + b

""" Llamada a la función con parámetros """ 
resultado = sumar(5, 3)
print("El resultado de la suma es:", resultado)

""" Definición de funciones con parámetros y valores por defecto """
def saludar_persona(nombre="Invitado"):
    print(f"Hola, {nombre}!")

saludar_persona()

"""Funciones con numero variable de argumentos"""
"""*args: permite pasar un número variable de argumentos posicionales"""
def  mostrar_numeros(*args):
    for numero in args:
        print(numero)

mostrar_numeros(1, 2, 3)

"""**kwargs: permite pasar un número variable de argumentos con nombre"""
def mostrar_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_informacion(nombre="Juan", edad=30, ciudad="Madrid")