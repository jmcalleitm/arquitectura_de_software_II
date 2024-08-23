from Producto import Producto
from CarritoCompras import CarritoCompras
from FactoryPago import FactoryPago

# Ejemplo de uso
def main() -> None:
    # Crear productos
    producto1 = Producto(1, "Laptop", 1200.00)
    producto2 = Producto(2, "Smartphone", 800.00)

    # Crear carrito y agregar productos
    carrito = CarritoCompras()
    carrito.agregar_producto(producto1)
    carrito.agregar_producto(producto2)

    # Seleccionar el sistema de pago
    tipo_sistema_pago = "JSON"  # Cambia a "XML" para usar el sistema de pagos existente
    sistema_pago = FactoryPago.obtener_sistema_pago(tipo_sistema_pago)

    # Procesar el pago usando el adaptador adecuado
    if sistema_pago.procesar_pago(carrito):
        print("Pago procesado exitosamente.")
    else:
        print("Error al procesar el pago.")

if __name__ == "__main__":
    main()
