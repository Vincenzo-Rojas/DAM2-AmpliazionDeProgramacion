/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package parte3;

import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.highgui.HighGui;
import org.opencv.imgproc.Imgproc;
import org.opencv.videoio.VideoCapture;

/**
 *
 * @author JAVI
 */
public class Webcam_02 {
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
        System.out.println("Empezamos a capturar");
        //capturar1();
        capturar2();
        System.out.println("Fin a capturar");
    }
    
    public static void capturar2() {
        VideoCapture camera = new VideoCapture(0);
        Mat frame = new Mat();
        
        while (true) {
            if (camera.read(frame)) {
                Mat imagen2 = new Mat();
                Imgproc.Sobel(frame, imagen2, CvType.CV_8U, 1, 1);   
                HighGui.imshow("sobel", imagen2);
                //Imgproc.medianBlur(frame, imagen2, 5);
                //HighGui.imshow("Mediana", imagen2);
                // Aplicar detección de color aquí
                HighGui.imshow("Cámara", imagen2);
            }
            if (HighGui.waitKey(1) == 27) break; // Salir con ESC
        }
        
        // Liberar la cámara y destruir las ventanas de HighGui
        System.out.println("Liberando la cámara...");
        camera.release();
        frame.release(); // Liberar el Mat del frame también

        System.out.println("Destruyendo ventanas de HighGui...");
        HighGui.destroyAllWindows(); // Cierra todas las ventanas abiertas por HighGui

        System.out.println("Programa finalizado.");
        System.exit(0); // Asegura que la aplicación termine completamente si hay hilos de HighGui
    }
    
    public static void capturar1() {
        VideoCapture camera = new VideoCapture(0);
        Mat frame = new Mat();
        
        while (true) {
            if (camera.read(frame)) {
                Mat imagen2 = new Mat();        
                Imgproc.medianBlur(frame, imagen2, 5);
                HighGui.imshow("Mediana", imagen2);
                // Aplicar detección de color aquí
                HighGui.imshow("Cámara", imagen2);
            }
            if (HighGui.waitKey(1) == 27) break; // Salir con ESC
        }
        
        // Liberar la cámara y destruir las ventanas de HighGui
        System.out.println("Liberando la cámara...");
        camera.release();
        frame.release(); // Liberar el Mat del frame también

        System.out.println("Destruyendo ventanas de HighGui...");
        HighGui.destroyAllWindows(); // Cierra todas las ventanas abiertas por HighGui

        System.out.println("Programa finalizado.");
        System.exit(0); // Asegura que la aplicación termine completamente si hay hilos de HighGui
    }
}
