from SistemaPagoExistente import SistemaPagoExistente
from CarritoCompras import CarritoCompras


# Adaptador para el sistema de pago existente (XML)
class AdaptadorPagoExistente():
    def __init__(self, sistema_pago: SistemaPagoExistente) -> None:
        self.sistema_pago = sistema_pago
    
    def procesar_pago(self, carrito: CarritoCompras) -> bool: #obligatorio
        xml_datos = self._convertir_a_xml(carrito)
        return self.sistema_pago.procesar_pago(xml_datos)
    
    def _convertir_a_xml(self, carrito: CarritoCompras) -> str:
        productos_xml = "".join(
            f"<producto><id>{producto.id_producto}</id><nombre>{producto.nombre}</nombre><precio>{producto.precio}</precio></producto>"
            for producto in carrito.productos
        )
        return f"<carrito>{productos_xml}</carrito>"