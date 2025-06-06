#Lenguaje en uso: Python

while True:
    try:
        num = int(input("Ingrese un numero entero positivo: "))
        if num > 0:
            print(f"Número válido ingresado: {num}")
            break
        else:
            print("Algo ha salido mal. El numero debe ser mayor a 0")
    except ValueError:
        print("Error: El dato solicitado debe ser un número")



