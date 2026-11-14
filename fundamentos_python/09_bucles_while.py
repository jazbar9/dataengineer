from time import sleep

contador = 0
while contador < 10:
    contador = contador + 1
    sleep(1)
    print(contador)
else:
    print("¡El bucle ha terminado correctamente! 🐍")

""" Salir de un bucle while con break """
while True:
    print(contador)
    contador += 1
    if contador == 15:
        break # Rompe el bucle while cuando contador es 15

""" Saltar una iteración con continue """
while True:
    contador += 1
    if contador == 5:
        continue # Salta la iteración cuando contador es 5
    print(contador)

    if contador == 10:
        break
    