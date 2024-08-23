from SistemaPago import SistemaPago
from SistemaPagoExistente import SistemaPagoExistente
from NuevoSistemaPago import NuevoSistemaPago
from AdaptadorNuevoSistemaPago import AdaptadorNuevoSistemaPago
from AdaptadorPagoExistente import AdaptadorPagoExistente

# Factory para crear el adaptador correcto
class FactoryPago:
    @staticmethod
    def obtener_sistema_pago(tipo: str) -> SistemaPago:
        if tipo == "XML":
            return AdaptadorPagoExistente(SistemaPagoExistente()) #XML
        elif tipo == "JSON":
            return AdaptadorNuevoSistemaPago(NuevoSistemaPago()) #JSON
        else:
            raise ValueError("Tipo de pago no soportado")