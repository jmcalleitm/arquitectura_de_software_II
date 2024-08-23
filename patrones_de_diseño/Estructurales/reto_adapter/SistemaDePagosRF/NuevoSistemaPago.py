from typing import Dict

# Nuevo sistema de pago que utiliza JSON
class NuevoSistemaPago:
    def procesar_pago(self, json_datos: Dict) -> bool:
        # Aquí iría la lógica de procesamiento con el nuevo sistema de pago en formato JSON
        print(f"Procesando pago con datos JSON: {json_datos}")
        return True  # Se asume que el pago fue exitoso
