public class Client {
    public static void main(String[] args) {
        // Cada vez que se aplica un filtro, se crea una nueva instancia y se carga la imagen
        ImageProcessor imageProcessor1 = new RealImageProcessor("ruta/a/imagen.jpg");
        imageProcessor1.applyFilter("Desenfoque");
        
        ImageProcessor imageProcessor2 = new RealImageProcessor("ruta/a/imagen.jpg");
        imageProcessor2.applyFilter("Ajuste de color");
        
        ImageProcessor imageProcessor3 = new RealImageProcessor("ruta/a/imagen.jpg");
        imageProcessor3.applyFilter("Desenfoque");
    }
}
