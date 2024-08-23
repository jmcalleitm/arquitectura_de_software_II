from typing import List
from Producto import Producto

# Definición del Carrito de Compras
class CarritoCompras:
    def __init__(self) -> None:
        self.productos: List[Producto] = []
    
    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)
    
    def eliminar_producto(self, producto: Producto) -> None:
        if producto in self.productos:
            self.productos.remove(producto)
    
    def calcular_total(self) -> float:
        return sum(producto.precio for producto in self.productos)