public class Client {
    public static void main(String[] args) {
        ImageProcessor imageProcessor = new ImageProcessorProxy("ruta/a/imagen.jpg");

        // Aplicando varios filtros a la misma imagen
        imageProcessor.applyFilter("Desenfoque");
        imageProcessor.applyFilter("Ajuste de color");
        
        // Reaplicando un filtro, debería utilizar el caché
        imageProcessor.applyFilter("Desenfoque");
    }
}
