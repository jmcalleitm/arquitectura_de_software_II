public class RealImageProcessor implements ImageProcessor {
    private String imagePath;
    
    public RealImageProcessor(String imagePath) {
        this.imagePath = imagePath;
        loadImage();
    }
    
    private void loadImage() {
        // Simulación de carga de la imagen en memoria
        System.out.println("Cargando imagen desde: " + imagePath);
    }
    
    @Override
    public void applyFilter(String filter) {
        // Simulación de la aplicación de un filtro a la imagen
        System.out.println("Aplicando filtro: " + filter + " a la imagen.");
    }
}
