from typing import Dict
from NuevoSistemaPago import NuevoSistemaPago
from CarritoCompras import CarritoCompras

# Adaptador para el nuevo sistema de pago (JSON)
class AdaptadorNuevoSistemaPago:
    def __init__(self, sistema_pago: NuevoSistemaPago) -> None:
        self.sistema_pago = sistema_pago
    
    def procesar_pago(self, carrito: CarritoCompras) -> bool:
        json_datos = self._convertir_a_json(carrito)
        return self.sistema_pago.procesar_pago(json_datos)
    
    def _convertir_a_json(self, carrito: CarritoCompras) -> Dict:
        productos_json = [
            {"id": producto.id_producto, "nombre": producto.nombre, "precio": producto.precio}
            for producto in carrito.productos
        ]
        return {"carrito": productos_json}