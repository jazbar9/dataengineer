lista = ["Python", "Rust", "Java", "C++", "TypeScript"]

"""Recorrer una lista"""
for lenguaje in lista: 
    print(lenguaje)
    
""""Recorrer cadenas de texto"""
texto = "I love Python"
for letra in texto:
    print(letra)
    
""" Recorrer una lista con un índice """
for index, lenguaje in enumerate(lista):
    print(index, lenguaje)