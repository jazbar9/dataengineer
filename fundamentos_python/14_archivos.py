"""with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)"""
"""with open. The available modes are:
- "r": read (default)
- "r", encoding="utf-8": evitar errores con tildes, eñes y otros caracteres especiales
- "w": write (creates a new file or overwrites an existing one)
- "a": append (adds to the end of the file)
""r+": read and write (does not truncate the file)
"w+": write and read (truncates the file)
"with": Gestiona recursos de forma segura y automatica, cerrando el archivo al finalizar el bloque de código

"""

archivo = open("archivo.txt", "r")
contenido = archivo.read()
#cerrar instancia del documento
archivo.close()
print(archivo)

with open("archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    #print(contenido)
    
    
    
""" Leer línea por línea """
#Se puede iterar sobre el objeto archivo para leer línea por línea
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    #contador de lineas
    rows = 0
    for linea in archivo:
        #imprime con salto de linea
        #print(linea)
        #imprime sin salto de linea
        #print(linea.strip())  # Elimina los saltos de línea al final de cada línea
        rows += 1
        if rows == 1:
            continue
        linea_sin_espacios = linea.strip() 
        lenguaje = linea_sin_espacios.split(",")[-1]  # Elimina los espacios en blanco al inicio y al final de la línea y divide la línea por comas
        print(lenguaje)  # Imprime el último elemento de la lista resultante de la división por comas
        
        
"""     Guardar las lineas en una lista     """
#Usamos esto para acceder a una linea en especifico por su posicion
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    #readlines devuelve una lista
print(lineas[0].strip())


"""     Formatos estructurados comunes(CSV y JSON)   """
#JSON
#Traer el modulo 
import json
import csv

with open("datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    print(datos)
    
with open("datos_1.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    print(datos)


#CSV    

with open("datos.csv", "r", encoding="utf-8", newline = "") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

    