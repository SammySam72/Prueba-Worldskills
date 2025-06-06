#Lenguaje en uso: Python

class Vehiculo:
    def __init__(self, marca, modelo, año, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def mostrar_info(self):
        print("----Información del vehiculo----")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Kilometraje: {self.kilometraje}")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, kilometraje, n_puertas):
        super().__init__(marca, modelo, año, kilometraje)
        self.n_puertas = n_puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de puertas: {self.n_puertas}")
        print("-" * 32)





class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, kilometraje, cc):
        super().__init__(marca, modelo, año, kilometraje)
        self.cc = cc

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Clindraje: {self.cc}cc")
        print("-" * 32)


# Creación de instancia de Vehiculo
mi_vehiculo = Vehiculo("Toyota", "4x4", 2012, 10000)
mi_vehiculo.mostrar_info() #Llamdada al método

#Creación de instancia de Coche
mi_coche = Coche("Ford", "Focus", 2018, 20000, 4)
mi_coche.mostrar_info() #Llamdada al método


#Creacion de instancia de motocicleta
mi_moto = Moto("Yamaha", "R15", 2020, 15000, 150)
mi_moto.mostrar_info() #Llamdada al método