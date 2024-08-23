from typing import Protocol

# Interfaz para procesar el pago
class SistemaPago(Protocol):
    def procesar_pago(self, datos: str) -> bool:
        ...
