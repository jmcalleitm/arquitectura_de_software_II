from bs4 import BeautifulSoup

# Clase que representa el sistema de pago existente
class SistemaPagoExistente:
    def procesar_pago(self, xml_datos: str) -> bool:
        # Aquí iría la lógica de procesamiento con el sistema de pago en formato XML
        bs = BeautifulSoup(xml_datos, "xml")
        print(f"Procesando pago con datos XML: {bs.prettify()}")
        return True  # Se asume que el pago fue exitoso
    