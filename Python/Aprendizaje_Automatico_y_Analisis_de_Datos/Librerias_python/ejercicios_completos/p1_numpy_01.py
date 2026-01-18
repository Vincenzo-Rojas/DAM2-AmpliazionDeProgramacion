import numpy as np
import time

# Ejercicios numpy

### Nivel Basico (1-10)
print("Ejercicios Nivel Basico (1-10)")

# 1. Crea un array 1D de 10 elementos con valores del 0 al 9
array = np.arange(10)
print("Ej1:\n", array)

# 2. Crea un array de ceros de forma (3, 4)
array = np.zeros((3, 4))
print("Ej2:\n", array)

# 3. Crea un array de unos de forma (5, 2) con tipo de dato int32
array = np.ones((5, 2), dtype=np.int32)
print("Ej3:\n", array)

# 4. Crea un array con valores espaciados uniformemente entre 0 y 100 (inclusive) con 21 elementos
array = np.linspace(0, 100, 21)
print("Ej4:\n", array)

#5. Crea un array 1D con 50 valores aleatorios entre 0 y 1 (usa `np.random.random`).
array = np.random.random(50)
print("Ej5:\n", array)

#6. Convierte el siguiente array a tipo `float64`: `arr = np.array([1, 2, 3, 4, 5])`
array = np.array([1, 2, 3, 4, 5]).astype(np.float64)
print("Ej6:\n", array)

# 7. Crea una matriz identidad 6x6
matriz = np.eye(6)
print("Ej7:\n", matriz)

# 8. Crea un array 1D con valores del 10 al 49 (ambos incluidos)
array = np.arange(10, 50)
print("Ej8:\n", array)

#9. Invierte el orden de los elementos del array anterior (sin usar `[::-1]`). Usa `np.flip`.
array = np.flip(array)
print("Ej9:\n", array)

#10. Encuentra los índices de los elementos no cero en: `arr = np.array([0, 2, 0, 5, 0, 8, 0])`
array = np.array([0, 2, 0, 5, 0, 8, 0])
resultado = np.nonzero(array)[0]
print("Ej10:\n", resultado)

### Nivel Básico-Intermedio (11-20)
print("Ejercicios Nivel Basico-Intermedio (11-20)")

#11. Cambia la forma del array `np.arange(12)` a (3, 4) sin cambiar sus datos.
matriz = np.arange(12).reshape(3, 4)
print("Ej11:\n", matriz)

#12. Crea una matriz 5×5 con valores de 1 a 25 y luego extrae la submatriz central 3×3.
matriz = np.arange(1, 26).reshape(5, 5)
submatriz = matriz[1:4, 1:4]
print("Ej12 Matriz:\n", matriz)
print("Ej12 Submatriz:\n", submatriz)

#13. Crea un array 4×4 de ceros y pon 1s en el borde (como un marco).
matriz = np.zeros((4, 4), dtype=int)
matriz[0, :] = 1
matriz[-1, :] = 1
matriz[:, 0] = 1
matriz[:, -1] = 1
print("Ej13:\n", matriz)

#14. Crea un array de forma (8, 8) con un patrón de tablero de ajedrez (0s y 1s alternados).
matriz = np.zeros((8, 8), dtype=int)
matriz[1::2, ::2] = 1
matriz[::2, 1::2] = 1
print("Ej14:\n", matriz)

#15. Dados `a = np.array([1,2,3])` y `b = np.array([4,5,6])`, concaténalos horizontal y verticalmente.
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])
print("Ej15 Horizontal:\n", np.hstack((vector_a, vector_b)))
print("Ej15 Vertical:\n", np.vstack((vector_a, vector_b)))

#16. Sin usar bucles, suma 5 a todos los elementos pares de un array y resta 3 a los impares.
array = np.arange(10)
resultado = array + np.where(array % 2 == 0, 5, -3)
print("Ej16:\n", resultado)

#17. Reemplaza todos los valores mayores que 30 por 30 y menores que 10 por 10 en un array aleatorio de 100 elementos entre 0 y 50.
array = np.random.randint(0, 51, 100)
resultado = np.clip(array, 10, 30)
print("Ej17 Original:\n", array)
print("Ej17 Modificado:\n", resultado)

#18. Calcula la media, mediana y desviación estándar de un array de 1000 números aleatorios normales.
array = np.random.randn(1000)
print("Ej18 Media:\n", np.mean(array), "Mediana:\n", np.median(array), "Desviacion:\n", np.std(array))

#19. Normaliza (resta la media y divide por la desviación estándar) un array 1D.
array = np.random.randint(0, 100, 10)
resultado = (array - np.mean(array)) / np.std(array)
print("Ej19 Original:\n", array)
print("Ej19 Normalizado:\n", resultado)

#20. Encuentra el valor máximo y su posición en cada fila de una matriz 6×6 de números aleatorios.
matriz = np.random.randint(0, 100, (6, 6))
print("Ej20 Matriz:\n", matriz)
print("Ej20 Maximos:\n", np.max(matriz, axis=1))
print("Ej20 Posiciones:\n", np.argmax(matriz, axis=1))


### Nivel Intermedio (21-30)
print("Ejercicios Nivel Intermedio (21-30)")

# 21. Usa broadcasting para sumar un vector a cada fila de una matriz 10x5
matriz = np.random.randint(0, 10, (10, 5))
vector = np.arange(5)
print("Ej21 Matriz:\n", matriz)
print("Ej21 Vector:\n", vector)
print("Ej21 Resultado:\n", matriz + vector)

#22. Crea dos matrices 3×3 aleatorias y calcula su producto matricial (usa `@` o `np.matmul`).
matriz_a = np.random.randint(0, 10, (3, 3))
matriz_b = np.random.randint(0, 10, (3, 3))
print("Ej22:\n", matriz_a @ matriz_b)

#23. Dada una matriz 10×10, extrae la diagonal principal y las dos diagonales por encima y debajo de ella.
matriz = np.arange(100).reshape(10, 10)
print("Ej23 Diagonal:\n", np.diag(matriz))
print("Ej23 Superior:\n", np.diag(matriz, 1))
print("Ej23 Inferior:\n", np.diag(matriz, -1))

#24. Genera un array 1D de 20 elementos y redondea cada elemento al entero más cercano.
array = np.random.uniform(0, 10, 20)
print("Ej24:\n", np.rint(array))

#25. Crea un array de forma (6, 7, 8) y calcula la suma a lo largo del eje 1.
array = np.random.randint(0, 10, (6, 7, 8))
resultado = np.sum(array, axis=1)
print("Ej25 Shape:\n", resultado.shape)
print("Ej25:\n", resultado)

#26. Encuentra los valores únicos y sus conteos en el array:  'arr = np.array([1,2,1,3,2,4,5,2,3,1,5,5])`
array = np.array([1, 2, 1, 3, 2, 4, 5, 2, 3, 1, 5, 5])
valores, conteos = np.unique(array, return_counts=True)
print("Ej26 Valores:\n", valores)
print("Ej26 Conteos:\n", conteos)

#27. Usa `np.where` para crear un array que sea 1 donde los valores sean mayores que 0.5 y -1 en caso contrario (sobre un array aleatorio).
array = np.random.random(10)
resultado = np.where(array > 0.5, 1, -1)
print("Ej27 Original:\n", array)
print("Ej27 Resultado:\n", resultado)

#28. Implementa la función de distancia euclidiana entre dos arrays 1D sin usar bucles ni `np.linalg.norm`.
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])
distancia = np.sqrt(np.sum((vector_a - vector_b) ** 2))
print("Ej28:\n", distancia)

#29. Genera 1000 puntos aleatorios en 2D (matriz 1000×2) y encuentra cuál está más cerca del origen (0,0).
puntos = np.random.random((1000, 2))
distancias = np.sqrt(np.sum(puntos ** 2, axis=1))
indice = np.argmin(distancias)
print("Ej29 Punto:\n", puntos[indice])
print("Ej29 Distancia:\n", distancias[indice])

#30. Crea una matriz 100×100 y reemplaza todos los elementos de las columnas pares por sus valores al cuadrado y los de las columnas impares por su raíz cuadrada.
matriz = np.random.randint(1, 100, (100, 100))
matriz[:, ::2] = matriz[:, ::2] ** 2
matriz[:, 1::2] = np.sqrt(matriz[:, 1::2])
print("Ej30:\n", matriz)