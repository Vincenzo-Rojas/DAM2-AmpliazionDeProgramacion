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

''' # Operaciones de ejemplo
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

#Ejercicios numpy

### Nivel Básico (1-10)
print("Ejercicios Nivel Basico (1-10)")
# 1. Crea un array 1D de 10 elementos con valores del 0 al 9
ej1 = np.arange(10)
print("Ej1:", ej1)

# 2. Crea un array de ceros de forma (3, 4)
ej2 = np.zeros((3, 4))
print("Ej2:\n", ej2)

# 3. Crea un array de unos de forma (5, 2) con tipo de dato int32
ej3 = np.ones((5, 2), dtype=np.int32)
print("Ej3:\n", ej3)

# 4. Crea un array con valores espaciados uniformemente entre 0 y 100 (inclusive) con 21 elementos
ej4 = np.linspace(0, 100, 21)
print("Ej4:", ej4)

#5. Crea un array 1D con 50 valores aleatorios entre 0 y 1 (usa `np.random.random`).
ej5 = np.random.random(50)
print("Ej5:", ej5) 
#6. Convierte el siguiente array a tipo `float64`: `arr = np.array([1, 2, 3, 4, 5])`
arr6 = np.array([1, 2, 3, 4, 5])
ej6 = arr6.astype(np.float64)
print("Ej6:", ej6)

#7. Crea una matriz identidad 6×6.
ej7 = np.eye(6)
print("Ej7:\n", ej7)

#8. Crea un array 1D con valores del 10 al 49 (ambos incluidos).
ej8 = np.arange(10, 50)
print("Ej8:", ej8)

#9. Invierte el orden de los elementos del array anterior (sin usar `[::-1]`). Usa `np.flip`.
ej9 = np.flip(ej8)
print("Ej9:", ej9)

#10. Encuentra los índices de los elementos no cero en: `arr = np.array([0, 2, 0, 5, 0, 8, 0])`
arr10 = np.array([0, 2, 0, 5, 0, 8, 0])
ej10 = np.nonzero(arr10)[0]
print("Ej10:", ej10)


### Nivel Básico-Intermedio (11-20)
print("Ejercicios Nivel Basico-Intermedio (11-20)")

#11. Cambia la forma del array `np.arange(12)` a (3, 4) sin cambiar sus datos.
ej11 = np.arange(12).reshape(3, 4)
print("Ej11:\n", ej11)

#12. Crea una matriz 5×5 con valores de 1 a 25 y luego extrae la submatriz central 3×3.
mat12 = np.arange(1, 26).reshape(5, 5)
ej12 = mat12[1:4, 1:4]
print("Ej12 (matriz 5x5):\n", mat12)
print("Ej12 (submatriz 3x3):\n", ej12)

#13. Crea un array 4×4 de ceros y pon 1s en el borde (como un marco).
ej13 = np.zeros((4, 4), dtype=int)
ej13[0, :] = 1
ej13[-1, :] = 1
ej13[:, 0] = 1
ej13[:, -1] = 1
print("Ej13:\n", ej13)

#14. Crea un array de forma (8, 8) con un patrón de tablero de ajedrez (0s y 1s alternados).
ej14 = np.zeros((8, 8), dtype=int)
ej14[1::2, ::2] = 1
ej14[::2, 1::2] = 1
print("Ej14:\n", ej14)

#15. Dados `a = np.array([1,2,3])` y `b = np.array([4,5,6])`, concaténalos horizontal y verticalmente.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
ej15_h = np.hstack((a, b))
ej15_v = np.vstack((a, b))
print("Ej15 Horizontal:", ej15_h)
print("Ej15 Vertical:\n", ej15_v)

#16. Sin usar bucles, suma 5 a todos los elementos pares de un array y resta 3 a los impares.
arr16 = np.arange(10)
ej16 = arr16 + np.where(arr16 % 2 == 0, 5, -3)
print("Ej16:", ej16)

#17. Reemplaza todos los valores mayores que 30 por 30 y menores que 10 por 10 en un array aleatorio de 100 elementos entre 0 y 50.
arr17 = np.random.randint(0, 51, 100)
ej17 = np.clip(arr17, 10, 30)
print("Ej17 Original:", arr17)
print("Ej17 Modificado:", ej17)

#18. Calcula la media, mediana y desviación estándar de un array de 1000 números aleatorios normales.
arr18 = np.random.randn(1000)
mean18 = np.mean(arr18)
median18 = np.median(arr18)
std18 = np.std(arr18)
print("Ej18 Media:", mean18, "Mediana:", median18, "Desviacion:", std18)

#19. Normaliza (resta la media y divide por la desviación estándar) un array 1D.
arr19 = np.random.randint(0, 100, 10)
ej19 = (arr19 - np.mean(arr19)) / np.std(arr19)
print("Ej19 Original:", arr19)
print("Ej19 Normalizado:", ej19)

#20. Encuentra el valor máximo y su posición en cada fila de una matriz 6×6 de números aleatorios.
arr20 = np.random.randint(0, 100, (6, 6))
max_vals = np.max(arr20, axis=1)
max_pos = np.argmax(arr20, axis=1)
print("Ej20 Matriz:\n", arr20)
print("Ej20 Maximos por fila:", max_vals)
print("Ej20 Posicion de maximos por fila:", max_pos)

'''
### Nivel Intermedio (21-30)
21. Usa broadcasting para sumar un vector fila a cada fila de una matriz 10×5.
22. Crea dos matrices 3×3 aleatorias y calcula su producto matricial (usa `@` o `np.matmul`).
23. Dada una matriz 10×10, extrae la diagonal principal y las dos diagonales por encima y debajo de ella.
24. Genera un array 1D de 20 elementos y redondea cada elemento al entero más cercano.
25. Crea un array de forma (6, 7, 8) y calcula la suma a lo largo del eje 1.
26. Encuentra los valores únicos y sus conteos en el array:  'arr = np.array([1,2,1,3,2,4,5,2,3,1,5,5])`
27. Usa `np.where` para crear un array que sea 1 donde los valores sean mayores que 0.5 y -1 en caso contrario (sobre un array aleatorio).
28. Implementa la función de distancia euclidiana entre dos arrays 1D sin usar bucles ni `np.linalg.norm`.
29. Genera 1000 puntos aleatorios en 2D (matriz 1000×2) y encuentra cuál está más cerca del origen (0,0).
30. Crea una matriz 100×100 y reemplaza todos los elementos de las columnas pares por sus valores al cuadrado y los de las columnas impares por su raíz cuadrada.
'''
