#Lenguaje en uso: Python

lista_enteros = [3,7,9,12,25,30]
def multiplo(lista,n):
    return [num for num in lista if num % n == 0]
print(f"Lista inicial: {lista_enteros}")
print(f"Lista nueva: {multiplo(lista_enteros,3)}")
