from typing import List
from Producto import Producto
from CarritoCompras import CarritoCompras
from SistemaPagoExistente import SistemaPagoExistente

# Ejemplo de uso sin el patrón Adapter
def main() -> None:
    # Crear productos
    producto1 = Producto(1, "Laptop", 1200.00)
    producto2 = Producto(2, "Smartphone", 800.00)

    # Crear carrito y agregar productos
    carrito = CarritoCompras()
    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)

    # Convertir datos del carrito a XML (directamente en el código principal)
    productos_xml = "".join(
        f"<producto><id>{producto.id_producto}</id><nombre>{producto.nombre}</nombre><precio>{producto.precio}</precio></producto>"
        for producto in carrito.productos
    )
    xml_datos = f"<carrito>{productos_xml}</carrito>"

    # Crear el sistema de pago existente
    sistema_pago_existente = SistemaPagoExistente()

    # Procesar el pago directamente
    if sistema_pago_existente.procesar_pago(xml_datos):
        print("Pago procesado exitosamente.")
    else:
        print("Error al procesar el pago.")

if __name__ == "__main__":
    main()
