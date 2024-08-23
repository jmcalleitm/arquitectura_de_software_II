import java.util.HashMap;
import java.util.Map;

public class ImageProcessorProxy implements ImageProcessor {
    private String imagePath;
    private RealImageProcessor realImageProcessor;
    private Map<String, String> cachedFilters;

    public ImageProcessorProxy(String imagePath) {
        this.imagePath = imagePath;
        this.cachedFilters = new HashMap<>();
    }

    @Override
    public void applyFilter(String filter) {
        if (cachedFilters.containsKey(filter)) {
            System.out.println("Usando resultado en caché para el filtro: " + filter);
        } else {
            if (realImageProcessor == null) {
                realImageProcessor = new RealImageProcessor(imagePath);
            }
            realImageProcessor.applyFilter(filter);
            cachedFilters.put(filter, "Resultado de " + filter);
        }
    }
}
