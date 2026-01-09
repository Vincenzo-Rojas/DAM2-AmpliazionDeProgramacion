import numpy as np
import time

'''
https://numpy.org/doc/stable/
https://numpy.org/es/learn/
https://deepnote.com/app/anthonymanotoa/Tutorial-de-NumPy-en-Espanol-180f7d51-b297-4aea-b61e-34ef867ca6fb
https://www.w3schools.com/python/numpy/default.asp
https://realpython.com/numpy-tutorial/
'''

def ejemplo1():
	print("Medicion de rencimiento con respecto a listas normales")
	#Ejemplo de rendimiento
	# Ejemplo con listas
	lista = list(range(1000000))
	start = time.time()
	sum(lista)
	print("Lista:", time.time() - start)

	# Ejemplo con arrays
	arr = np.arange(1000000)
	start = time.time()
	np.sum(arr)
	print("Array:", time.time() - start)
    

def creacionArrays():

    # Array de una dimensión
    a1 = np.array([1, 2, 3])
    print(a1)
    print(a1[1])
    print("-"*25)
    
    # Array de dos dimensiones (matriz)
    a2 = np.array([[1, 2, 3], [4, 5, 6]])
    print(a2)
    print(a2[0])
    print(a2[0][2])
    print("-"*25)
    
    # Array de 3 dimensiones
    a3 = np.zeros((5, 4, 3))
    print(a3)
    print("-"*25)
    
    for i in a2:
        for j in i:
            print(j,end="")
        print()
        
def algunasPropiedades():
    a2 = np.array([[1, 2, 3], [4, 5, 6]])
    print(a2)
    print("Shape:", a2.shape)
    print("Shape:", a2.shape[0])
    print("Shape:", len(a2))
    print("Shape:", a2.shape[1])
    print("Número de dimensiones:", a2.ndim)
    print("Número de elementos:", a2.size)
    print("Número de elementos:", len(a2))
    print("Tipo de dato:", a2.dtype)
    print("Tamaño de cada elemento:", a2.itemsize)
    print("Tamaño total en bytes:", a2.nbytes)

def ejercicio1():
    a3 = np.zeros((5, 4))
    print(a3)
    print("-"*25)
    #RELLENA LOS ELEMENTOS DE LA MATRIZ CON LOS NUMEROS DEL 1 AL 20
    print(a3)
    
def operacionesBasicas():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print("Suma:", a + b)
    print("Resta:", a - b)
    print("Multiplicación:", a * b)
    print("División:", b / a)
    print("FUNCIONES MATEMATICAS")
    print("Media:", np.mean(a))    
    print("Máximo:", np.max(a))
    print("Mínimo:", np.min(a))
    print("Desviación estándar:", np.std(a))
    print("Suma:", np.sum(a))


print("Empezamos")
print("Version:",np.__version__)

ejemplo1()
print("*"*50)
creacionArrays()
print("*"*50)
algunasPropiedades()
print("*"*50)
ejercicio1()
print("*"*50)
operacionesBasicas()

print("Fin")

'''

Ejercicios numpy

### Nivel Básico (1-10)
1. Crea un array 1D de 10 elementos con valores del 0 al 9.  
2. Crea un array de ceros de forma (3, 4).  
3. Crea un array de unos de forma (5, 2) con tipo de dato `int32`.  
4. Crea un array con valores espaciados uniformemente entre 0 y 100 (inclusive) con 21 elementos.  
5. Crea un array 1D con 50 valores aleatorios entre 0 y 1 (usa `np.random.random`).  
6. Convierte el siguiente array a tipo `float64`: `arr = np.array([1, 2, 3, 4, 5])`  
7. Crea una matriz identidad 6×6.  
8. Crea un array 1D con valores del 10 al 49 (ambos incluidos).  
9. Invierte el orden de los elementos del array anterior (sin usar `[::-1]`). Usa `np.flip`.  
10. Encuentra los índices de los elementos no cero en: `arr = np.array([0, 2, 0, 5, 0, 8, 0])`

### Nivel Básico-Intermedio (11-20)
11. Cambia la forma del array `np.arange(12)` a (3, 4) sin cambiar sus datos.  
12. Crea una matriz 5×5 con valores de 1 a 25 y luego extrae la submatriz central 3×3.  
13. Crea un array 4×4 de ceros y pon 1s en el borde (como un marco).  
14. Crea un array de forma (8, 8) con un patrón de tablero de ajedrez (0s y 1s alternados).  
15. Dados `a = np.array([1,2,3])` y `b = np.array([4,5,6])`, concaténalos horizontal y verticalmente.  
16. Sin usar bucles, suma 5 a todos los elementos pares de un array y resta 3 a los impares.  
17. Reemplaza todos los valores mayores que 30 por 30 y menores que 10 por 10 en un array aleatorio de 100 elementos entre 0 y 50.  
18. Calcula la media, mediana y desviación estándar de un array de 1000 números aleatorios normales.  
19. Normaliza (resta la media y divide por la desviación estándar) un array 1D.  
20. Encuentra el valor máximo y su posición en cada fila de una matriz 6×6 de números aleatorios.

### Nivel Intermedio (21-30)
21. Usa broadcasting para sumar un vector fila a cada fila de una matriz 10×5.  
22. Crea dos matrices 3×3 aleatorias y calcula su producto matricial (usa `@` o `np.matmul`).  
23. Dada una matriz 10×10, extrae la diagonal principal y las dos diagonales por encima y debajo de ella.  
24. Genera un array 1D de 20 elementos y redondea cada elemento al entero más cercano.  
25. Crea un array de forma (6, 7, 8) y calcula la suma a lo largo del eje 1.  
26. Encuentra los valores únicos y sus conteos en el array:  
   `arr = np.array([1,2,1,3,2,4,5,2,3,1,5,5])`  
27. Usa `np.where` para crear un array que sea 1 donde los valores sean mayores que 0.5 y -1 en caso contrario (sobre un array aleatorio).  
28. Implementa la función de distancia euclidiana entre dos arrays 1D sin usar bucles ni `np.linalg.norm`.  
29. Genera 1000 puntos aleatorios en 2D (matriz 1000×2) y encuentra cuál está más cerca del origen (0,0).  
30. Crea una matriz 100×100 y reemplaza todos los elementos de las columnas pares por sus valores al cuadrado y los de las columnas impares por su raíz cuadrada.
'''
