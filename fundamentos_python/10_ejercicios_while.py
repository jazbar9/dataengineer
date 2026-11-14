""" 1. Validar que una contraseña tenga almenos 8 caracteres """
# Input: "1234567"
# Output: "Introduce mínimo 8 caracteres"

# Input: "12345678"
# Output: "Contraseña válida"

while True:
    password = input("Introduce una contraseña: ")
    if len(password) < 8:
        print("Introduce mínimo 8 caracteres")
    else:    
        print("Contraseña válida")
        break

""" 2. Ingresar un número y crear una tabla de multiplicar hasta el 10 """
# Input: 1
# Output: 1 x 1 = 1, 1 x 2 = 2... 1 x 10 = 10
while True:
    number = int(input("Introduce un número: "))

    i = 1
    while i <= 10:
        print(f"{number} x {i} = {number * i}")
        i = i + 1