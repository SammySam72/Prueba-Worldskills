#Lenguaje en uso: Python

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def obtener_valor(self):
        return self.precio * self.stock

class Inventario:
    def __init__(self):
        self.productos = []


    def agregar_producto(self, producto):
        self.productos.append(producto)


    def mostrar_inventario(self):
        print("----Inventario de Productos----")
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Stock: {producto.stock}, Valor Total: {producto.obtener_valor()}")
        print("-" * 32)


    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                print(f"Producto encontrado: {producto.nombre}, Precio: {producto.precio}, Stock: {producto.stock}, Valor Total: {producto.obtener_valor()}")
                return
        print("Producto no encontrado.")

    def calcular_valor_total_inventrio(self):
        total = sum(producto.obtener_valor() for producto in self.productos)
        print(f"Valor total del inventario: {total}") 



Producto1 = Producto("Laptop", 1000, 5)
Producto2 = Producto("Teléfono", 500, 10)
Producto3 = Producto("Tablet", 300, 8)

inventario = Inventario()
inventario.agregar_producto(Producto1)
inventario.agregar_producto(Producto2)
inventario.agregar_producto(Producto3)
inventario.mostrar_inventario()
inventario.buscar_producto("laptop")
inventario.calcular_valor_total_inventrio()