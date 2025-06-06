#Lenguaje en uso: Python

def anagrama(cadena1, cadena2):
    c1 = cadena1.lower().replace(" ","")
    c2 = cadena2.lower().replace(" ","")
    if sorted(c1) == sorted(c2):
        return True
    else:
        return False

print(anagrama("amor","roma"))
print(anagrama("cena","mesa"))
print(anagrama("El perro","Re el pro"))