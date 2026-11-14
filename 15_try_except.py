# resultado = 5 / 0

#try except nos permite manejar los errores de manera controlada
try:
    numero = int(input("Ingreso un número: "))
    resultado = 10 / numero
    print(f"El resultado es {resultado}")
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero")
except ValueError:
    print("Error: Debes ingresar un número válido")
except Exception:
    print("Error: Ha ocurrido un error desconocido")

# Se ejecuta SOLO SI NO HUBO NINGUN ERROR en el bloque try
#else:
    print("Proceso finalizado con éxito")
    print(resultado)

# Se ejecuta SIEMPRE (haya ocurrido un error o no)
#finally:
#    print("Proceso finalizado")
    

try:
    with open("file.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
else:
    print("Archivo leído con éxito")
    print(contenido)
finally:
    print("Proceso de lectura finalizado")
        