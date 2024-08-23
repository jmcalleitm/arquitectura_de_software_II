# Definición del Producto
class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float) -> None:
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio