/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package pruebas;

import org.opencv.core.Core;
import org.opencv.videoio.VideoCapture;
import org.opencv.core.Mat;
import org.opencv.highgui.HighGui;

/**
 *
 * @author JAVI
 */
public class Video_01 {

    // Cargar la librería nativa de OpenCV al inicio
    static {
        try {
            System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        } catch (UnsatisfiedLinkError e) {
            System.err.println("Error al cargar la librería nativa de OpenCV: " + e.getMessage());
            System.err.println("Asegúrate de que OpenCV esté correctamente configurado y las librerías nativas en el java.library.path.");
            System.exit(1);
        }
    }

    public static void main(String[] args) {
        String directorioActual = System.getProperty("user.dir");
        System.out.println("Directorio actual: " + directorioActual);

        System.out.println("Empezamos a capturar");
        capturar();

        System.out.println("Fin a capturar");
    }

    public static void capturar() {

        VideoCapture capture = new VideoCapture(System.getProperty("user.dir") + "/video_prueba/trafico.mp4");
        Mat frame = new Mat();

        if (!capture.isOpened()) {
            System.out.println("No se pudo abrir el vídeo.");
            return;
        }

        while (true) {
            if (!capture.read(frame) || frame.empty()) {
                System.out.println("Fin del vídeo o frame vacío.");
                break;
            }

            HighGui.imshow("Video", frame);

            if (HighGui.waitKey(20) == 27) { 
                break;
            }
        }

        capture.release();
        frame.release();
        HighGui.destroyAllWindows();
    }

}
