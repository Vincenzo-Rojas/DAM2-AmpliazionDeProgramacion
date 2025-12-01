/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package parte3;

/**
 *
 * @author JAVI
 */

import org.opencv.core.*;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.highgui.HighGui;
import org.opencv.core.*;
import org.opencv.features2d.*;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.highgui.HighGui;

import java.util.ArrayList;
import java.util.List;
import org.opencv.calib3d.Calib3d;

public class Patrones {
    
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
        ejemplo01();
        //FeatureMatchingExample();
    }
    
    public static void ejemplo01() {


        // Cargar la imagen grande y el patrón (template)
        Mat imagenGrande = Imgcodecs.imread("busquedaPatrones/imagen_grande.png");
        Mat patron = Imgcodecs.imread("busquedaPatrones/banana.png");
        Mat mascara = Imgcodecs.imread("busquedaPatrones/mascara.png");

        if (imagenGrande.empty() || patron.empty()) {
            System.out.println("No se pudo cargar una de las imágenes.");
            return;
        }

        // Crear el resultado de la coincidencia
        int resultCols = imagenGrande.cols() - patron.cols() + 1;
        int resultRows = imagenGrande.rows() - patron.rows() + 1;
        Mat resultado = new Mat(resultRows, resultCols, CvType.CV_32FC1);

        // Buscar el patrón en la imagen grande
        Imgproc.matchTemplate(imagenGrande, patron, resultado, Imgproc.TM_CCOEFF_NORMED,mascara);
        //Imgproc.matchTemplate(imagenGrande, patron, resultado, Imgproc.TM_CCOEFF_NORMED);

        // Encontrar la mejor coincidencia
        Core.MinMaxLocResult mmr = Core.minMaxLoc(resultado);
        Point matchLoc = mmr.maxLoc;

        // Dibujar un rectángulo donde se encontró el patrón
        Imgproc.rectangle(
            imagenGrande,
            matchLoc,
            new Point(matchLoc.x + patron.cols(), matchLoc.y + patron.rows()),
            new Scalar(0, 255, 0),
            2
        );

        // Mostrar la imagen con el patrón marcado
        HighGui.imshow("Patrón encontrado", imagenGrande);
        HighGui.waitKey(0);
        System.exit(0);
    }
    
    public static void FeatureMatchingExample () {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);

        // Cargar las dos imágenes a comparar
        Mat img1 = Imgcodecs.imread("busquedaPatrones/imagen_grande.png", Imgcodecs.IMREAD_GRAYSCALE);
        Mat img2 = Imgcodecs.imread("busquedaPatrones/banana.png", Imgcodecs.IMREAD_GRAYSCALE);

        if (img1.empty() || img2.empty()) {
            System.out.println("No se pudieron cargar las imágenes.");
            return;
        }

        // 1. Detectar keypoints y calcular descriptores con ORB
        ORB orb = ORB.create();
        MatOfKeyPoint keypoints1 = new MatOfKeyPoint();
        MatOfKeyPoint keypoints2 = new MatOfKeyPoint();
        Mat descriptors1 = new Mat();
        Mat descriptors2 = new Mat();

        orb.detectAndCompute(img1, new Mat(), keypoints1, descriptors1);
        orb.detectAndCompute(img2, new Mat(), keypoints2, descriptors2);

        // 2. Matcher Brute-Force con distancia Hamming
        DescriptorMatcher matcher = DescriptorMatcher.create(DescriptorMatcher.BRUTEFORCE_HAMMING);
        List<MatOfDMatch> knnMatches = new ArrayList<>();
        matcher.knnMatch(descriptors1, descriptors2, knnMatches, 2);

        // 3. Filtrar matches usando la razón de Lowe
        float ratioThresh = 0.75f;
        List<DMatch> goodMatches = new ArrayList<>();
        for (MatOfDMatch matOfDMatch : knnMatches) {
            DMatch[] matches = matOfDMatch.toArray();
            if (matches.length >= 2) {
                if (matches[0].distance < ratioThresh * matches[1].distance) {
                    goodMatches.add(matches[0]);
                }
            }
        }

        // 4. Dibujar los matches
        Mat imgMatches = new Mat();
        Features2d.drawMatches(
                img1, keypoints1,
                img2, keypoints2,
                new MatOfDMatch(goodMatches.toArray(new DMatch[0])),
                imgMatches
        );

        // 5. Mostrar el resultado
        HighGui.imshow("Feature Matching con ORB", imgMatches);
        HighGui.waitKey();
        HighGui.destroyAllWindows();
    }
    
    
}
