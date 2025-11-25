/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package modificardataset;

import java.io.*;
import java.nio.file.Path;
import java.util.ArrayList;

/**
 *
 * @author DAM2B-11
 */
public class ModificarDataSet {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        //Ruta actual
        String directorioActual = System.getProperty("user.dir");
        System.out.println("Directorio actual: " + directorioActual);

        //789 lineas de cabecera
        int cabecera = 789;
        String origen = "..\\..\\DataSets\\mnist.arff";
        String optimizarImagenes = "..\\..\\DataSets\\mnist_optmizar_imagenes.arff";
        String quitarImagenes = "..\\..\\DataSets\\mnist_quitar_imagenes.arff";
        quitarBitsDeImagenes(cabecera, origen, optimizarImagenes, 1.5); //limite bits a borrar, sobre 789 bits
        //quitarInstancias(optimizarImagenes, quitarImagenes, 40.0); //limite de las instancias a borrar, sobre 59.999 instancias
    }

    // quita los bits no representativos de una imagen
    public static void quitarBitsDeImagenes(int cabecera, String ruta, String nuevaRuta, Double limiteBorrado) {

        ArrayList<Double> valorDeBitsABorrar = new ArrayList<>(); //Lista que indica si esa posicion no aporta informacion
        boolean setearLista = true;

        ArrayList<Integer> numeroDelBit = new ArrayList<>(); //Lista de posiciones de bits a borrar, la obtienes de 'bitsABorrar'
        int cantidadInstancias = 0;
        int cantidadBits = 0;

        //limiteBorrado = 0.5
        //es el numero hasta 0 - 254 que tiene de limite cada bit con decimales, para mas precision, no se ingresan decimales en el dataset
        BufferedReader br;
        BufferedWriter bw;

        try {
            Path pathTxtBuf = Path.of(ruta);
            Path pathResolve = Path.of(nuevaRuta);

            // --- LECTURA CON BUFFER --- Consigue la lista de los bits que hay que saltar
            br = new BufferedReader(new FileReader(pathTxtBuf.toFile())); // BufferedReader permite leer líneas completas
            String linea; // Variable para almacenar cada línea
            
            for (int i = 0; (linea = br.readLine()) != null; i++) { // Leemos hasta el final del archivo
                if (cabecera < i) { // '>' guarda la cabecera, '<' guarda los datos
                    String[] instanciasPos = linea.split(",");
                    for (int j = 0; j < instanciasPos.length; j++) {
                        Double valorXY = Double.parseDouble(instanciasPos[j]);
                        if (setearLista == true) {
                            valorDeBitsABorrar.add(valorXY);
                        } else {
                            // --- Suma ---
                            // 1. Obtener el valor actual
                            double valorActual = valorDeBitsABorrar.get(j);

                            // 2. Calcular el nuevo valor
                            double nuevoValor = valorActual + valorXY;

                            // 3. Actualizar la posición con el nuevo valor usando set()
                            valorDeBitsABorrar.set(j, nuevoValor);
                        }
                    }
                    setearLista = false; // al terminar la instancia, se puede proceder a operar en ella
                }
                cantidadInstancias += 1;
            }
            br.close(); // Cerramos el BufferedReader

            // Para encontrar que bits hay que borrar, y cuantos son. Ademas normaliza las cantidades de la arraylist a 0 - 254
            for (int i = 0; i < valorDeBitsABorrar.size(); i++) {
                double borrarBit = valorDeBitsABorrar.get(i) / cantidadInstancias;
                if (borrarBit <= limiteBorrado) { // es el numero hasta 0 - 254 que tiene de limite cada bit
                    // i es el numero del bit a borrar
                    //System.out.println("Bit "+i); // son bits que siempre estan a 0. bit es la posicion de cada numero en la instancia
                    numeroDelBit.add(i);
                    cantidadBits += 1;
                }
            }

            System.out.println("Cantidad de bits a borrar: " + cantidadBits);
            //System.out.println(bits);

            System.out.println("Generando nuevo dataset...");

            // --- LECTURA y ESCRITURA CON BUFFER --- Lee el dataset saltando los bits que consideramos inutiles
            br = new BufferedReader(new FileReader(pathTxtBuf.toFile())); // BufferedReader permite leer líneas completas
            bw = new BufferedWriter(new FileWriter(pathResolve.toFile())); // BufferedWriter permite escribir líneas

            for (int i = 0; (linea = br.readLine()) != null; i++) { // Leemos hasta el final del archivo
                if (cabecera < i) { // '>' guarda la cabecera, '<' guarda los datos
                    String[] instanciasPos = linea.split(",");
                    ArrayList<String> nuevaInstancia = new ArrayList<>();

                    // Crear la instancia completa ignorando los bits NO necesarios
                    for (int j = 0; j < instanciasPos.length; j++) {
                        if (!numeroDelBit.contains(j)) {
                            nuevaInstancia.add(instanciasPos[j]);
                        }
                    }
                    // Convertimos el ArrayList en una sola línea de texto separada por comas
                    String lineaFormateada = String.join(",", nuevaInstancia);

                    bw.write(lineaFormateada); // Escribimos la línea de texto formateada 
                    bw.newLine();        // Salto de línea
                    //System.out.println(nuevaInstancia); // no hay problema con los espacion en el .arff
                }
            }
            br.close(); // Cerramos el BufferedReader
            bw.flush(); // Guardamos los cambios
            bw.close(); // Cerramos el BufferedWriter

            System.out.println("Nuevo archivo DataSet creado");

        } catch (IOException e) { // Captura errores de E/S
            e.printStackTrace(); // Muestra información detallada del error
        }

    }

    //quita imagenes no representativas
    public static void quitarInstancias(String nuevaTemporal, String rutaFinal, Double limiteBorrado) {

        ArrayList<Double> valorInstanciasABorrar = new ArrayList<>(); //Lista que indica si esa posicion NO aporta informacion
        ArrayList<Integer> numeroDeLaInstancias = new ArrayList<>(); //Lista de instancias a borrar, la obtienes de 'bitsABorrar'

        int cantidadInstancias = 0;
        String[] instanciasPos = null; //cantidad de bits por instancia, instanciasPos.length

        BufferedReader br;
        BufferedWriter bw;

        try {
            Path pathTxtBuf = Path.of(nuevaTemporal);
            Path pathResolve = Path.of(rutaFinal);

            // --- LECTURA CON BUFFER --- Consigue la lista de los bits que hay que saltar
            br = new BufferedReader(new FileReader(pathTxtBuf.toFile())); // BufferedReader permite leer líneas completas
            String linea; // Variable para almacenar cada línea
            
            //Recorrer instancias
            for (int i = 0; (linea = br.readLine()) != null; i++) { // Leemos hasta el final del archivo
                instanciasPos = linea.split(","); //instancia en arreglo
                Double valorXY = 0.0; // valor de la suma de los numeros de cada instancia
                
                //Recorrer los numeros instancia
                for (int j = 0; j < instanciasPos.length; j++) {
                    valorXY += Double.parseDouble(instanciasPos[j]); // valor sumado de la instancia
                }
                valorInstanciasABorrar.add(valorXY); // añade a la lista, la suma total de la instancia. El numero de posicion = numero de instancias
            }
            br.close(); // Cerramos el BufferedReader

            // Para encontrar de instancias a que borrar, y cuantos son. Ademas normaliza las cantidades de la arraylist a 0 - 254
            for (int i = 0; i < valorInstanciasABorrar.size(); i++) {
                
                double borrarBit = valorInstanciasABorrar.get(i) / instanciasPos.length;
                
                //System.out.println("borrarBit: "+borrarBit+" instanciasABorrar.get(i): "+instanciasABorrar.get(i)+" instanciasPos.length: "+instanciasPos.length);
                
                if (borrarBit <= limiteBorrado) { // es el numero hasta 0 - 254 que tiene de limite cada bit
                    // i es el numero del bit a borrar
                    //System.out.println("Instancia "+i); // son instancias que estan por debajo del limite
                    numeroDeLaInstancias.add(i);
                    cantidadInstancias += 1;
                }
            }

            System.out.println("Cantidad de instancias a borrar: " + cantidadInstancias);
            //System.out.println(bits);

            System.out.println("Generando nuevo dataset...");

            // --- LECTURA y ESCRITURA CON BUFFER --- Lee el dataset saltando los bits que consideramos inutiles
            br = new BufferedReader(new FileReader(pathTxtBuf.toFile())); // BufferedReader permite leer líneas completas
            bw = new BufferedWriter(new FileWriter(pathResolve.toFile())); // BufferedWriter permite escribir líneas

            for (int i = 0; (linea = br.readLine()) != null; i++) { // Leemos hasta el final del archivo
                if (!numeroDeLaInstancias.contains(i)) {
                    bw.write(linea); // Escribimos la línea de texto formateada 
                    bw.newLine();        // Salto de línea
                }
                //System.out.println(linea); // no hay problema con los espacion en el .arff
            }
            br.close(); // Cerramos el BufferedReader
            bw.flush(); // Guardamos los cambios
            bw.close(); // Cerramos el BufferedWriter

            System.out.println("Nuevo archivo DataSet creado");

        } catch (IOException e) { // Captura errores de E/S
            e.printStackTrace(); // Muestra información detallada del error
        }

    }

}
