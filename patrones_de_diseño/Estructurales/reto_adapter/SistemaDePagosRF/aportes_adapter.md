Este es un caso ideal para aplicar el patrón **Adapter**, lo que permitirá encapsular la lógica de conversión entre los diferentes formatos de datos (XML y JSON) sin modificar la lógica de negocio principal. También introduciremos un patrón **Factory** para que el sistema pueda seleccionar el adaptador adecuado en función del proveedor de pagos que se va a utilizar.


### Explicación del Código:

1. **Clases `Producto` y `CarritoCompras`:** Se mantienen igual que en las versiones anteriores.

2. **Interfaz `SistemaPago`:** Define un protocolo para los sistemas de pago, asegurando que todos los sistemas de pago (XML y JSON) sigan una interfaz común.

3. **Clase `SistemaPagoExistente`:** Representa el sistema de pagos existente que acepta datos en formato XML.

4. **Clase `NuevoSistemaPago`:** Representa el nuevo sistema de pagos que acepta datos en formato JSON.

5. **Clase `AdaptadorPagoExistente`:** Es el adaptador que convierte los datos del carrito de compras en formato XML para el sistema de pagos existente.

6. **Clase `AdaptadorNuevoSistemaPago`:** Es el adaptador que convierte los datos del carrito de compras en formato JSON para el nuevo sistema de pagos.

7. **Clase `FactoryPago`:** Implementa el patrón **Factory** para seleccionar el adaptador adecuado (XML o JSON) según el tipo de sistema de pago especificado.

8. **Función `main`:** 
   - Crea algunos productos y los añade al carrito.
   - Selecciona el sistema de pago (XML o JSON) usando la fábrica.
   - Procesa el pago usando el adaptador correspondiente.

### Ventajas de Esta Solución:

- **Desacoplamiento:** El código principal de la aplicación no está atado a ningún formato de datos específico (XML o JSON). Esto permite cambiar fácilmente entre proveedores de pago sin modificar la lógica de negocio.
  
- **Extensibilidad:** Si en el futuro se añade un nuevo proveedor de pagos con un formato de datos diferente, solo es necesario implementar un nuevo adaptador y añadirlo a la fábrica.

- **Flexibilidad:** El patrón Factory permite seleccionar el sistema de pago dinámicamente en tiempo de ejecución, facilitando la gestión de múltiples proveedores de pago.

Esta arquitectura es más flexible, escalable y fácil de mantener en comparación con la versión original sin el patrón Adapter.