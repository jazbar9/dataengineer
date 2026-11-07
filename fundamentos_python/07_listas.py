""" Son colecciones ordenadas y mutables de elementos que permiten almacenar multiples elementos
en una sola variable. Se pueden crear listas utilizando corchetes [] y separando los elementos
con comas. Las listas pueden contener elementos de diferentes tipos de datos, incluyendo números,
cadenas de texto, booleanos, e incluso otras listas.
"""
lista1 = [1, 2, 3, 4, 5]
lista2 = ["Python", "Rust", "Typescript"]
lista3 = [1,2,3.14, True, "Hola"]

# Acceder a los elementos de una lista
print(lista1[0])
# Output: 1

print(lista2[1])
# Output: Rust

print(lista3[-1])
# Output: Hola


""" Slicing (Rebanando) de listas: permite acceder a un subconjunto
de elementos de una lista utilizando índices y rangos."""

print(lista1[1:4])
# Output: [2, 3, 4]

print(lista1[:3])
# Output: [1, 2, 3]

print(lista1[3:])
# Output: [4, 5]

print(lista1[::2]) #Paso 2
# Output: [1, 3, 5]


"""Modificar elementos de una lista: se puede cambiar el valor de un elemento en una lista"""
lista1[4] = 10
print(lista1)
# Output: [10, 2, 3, 4, 5]

"""Agregar elementos a una lista: se pueden agregar elementos al final de una lista 
utilizando el método append()"""

lista1 = lista1 + [6,7]
print(lista1)
# Output: [10, 2, 3, 4, 5, 6]

""" Obtener la longitud de una lista: se puede obtener el número de elementos en una 
lista utilizando la función len()"""
print(len(lista1))
# Output: 6

""" Metodos de listas"""
lista = ["Python"]
lista.append("Go")
print(lista)
# Output: ['Python', 'Go']

lista.insert(0, "C++")
print(lista)
# Output: ['C++', 'Python', 'Go']

lista.remove("Go")
print(lista)
# Output: ['C++', 'Python']

lista.pop(0) # Por defecto elimina el último elemento de la lista
print(lista)
# Output: ['Python']

print(lista.index("Python"))
# Output: 0

print(lista.count("Python"))
# Output: 1

lista2 = [5, 10, 2]
lista2.sort()
print(lista2)

lista2.reverse()
print(lista2)

lista2.clear()
print(lista2)  
# Output: []