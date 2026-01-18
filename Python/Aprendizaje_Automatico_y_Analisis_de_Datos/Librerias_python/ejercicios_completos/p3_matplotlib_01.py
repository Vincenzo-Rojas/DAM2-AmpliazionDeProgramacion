import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# Puedes usar datos simples (listas o arrays de NumPy) para resolverlos. 
# ¡Intenta implementarlos tú mismo antes de buscar soluciones!

# 1. Crea un gráfico de línea simple con los puntos x = [1, 2, 3, 4, 5] e y = [1, 4, 2, 3, 5]. Agrega etiquetas a los ejes y un título.
x1, y1 = [1,2,3,4,5], [1,4,2,3,5]
plt.figure()
plt.plot(x1, y1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ejercicio 1")
plt.show()

# 2. Dibuja dos líneas en el mismo gráfico: una con y = x² y otra con y = x³, para x de 0 a 10. Usa diferentes colores y agrega una leyenda.
x2 = np.arange(0,11)
plt.figure()
plt.plot(x2, x2**2, label="y = x²", color="blue")
plt.plot(x2, x2**3, label="y = x³", color="red")
plt.legend()
plt.title("Ejercicio 2")
plt.show()

# 3. Grafica la función seno (sin(x)) y coseno (cos(x)) en el rango de 0 a 2π. Usa una cuadrícula (grid).
x3 = np.linspace(0, 2*np.pi, 100)
plt.figure()
plt.plot(x3, np.sin(x3), label="sin(x)")
plt.plot(x3, np.cos(x3), label="cos(x)")
plt.grid(True)
plt.legend()
plt.title("Ejercicio 3")
plt.show()

# 4. Crea un gráfico de dispersión (scatter) con 100 puntos aleatorios generados con NumPy.
x4, y4 = np.random.rand(100), np.random.rand(100)
plt.figure()
plt.scatter(x4, y4, color="purple")
plt.title("Ejercicio 4")
plt.show()

# 5. Dibuja un gráfico de barras con categorías ["A", "B", "C", "D", "E"] y valores [10, 24, 15, 30, 12]. Agrega colores diferentes a cada barra.
cat5, val5 = ["A","B","C","D","E"], [10,24,15,30,12]
plt.figure()
plt.bar(cat5, val5, color=["red","blue","green","orange","purple"])
plt.title("Ejercicio 5")
plt.show()

# 6. Crea un histograma con 1000 valores aleatorios de una distribución normal (media 0, desviación 1).
data6 = np.random.randn(1000)
plt.figure()
plt.hist(data6, bins=30, color="skyblue", edgecolor="black")
plt.title("Ejercicio 6")
plt.show()

# 7. Dibuja un gráfico circular (pie chart) que muestre la proporción de [20, 30, 25, 25] con etiquetas ["Grupo A", "Grupo B", "Grupo C", "Grupo D"] y explota una porción.
sizes7, labels7 = [20,30,25,25], ["Grupo A","Grupo B","Grupo C","Grupo D"]
plt.figure()
plt.pie(sizes7, labels=labels7, explode=[0,0.1,0,0], autopct="%1.1f%%")
plt.title("Ejercicio 7")
plt.show()

# 8. Usa subplots para mostrar 4 gráficos en una figura: línea, barras, dispersión e histograma (en una cuadrícula 2x2).
x8 = np.arange(0,10)
y8a, y8b = x8**2, x8**3
data8 = np.random.randn(100)
fig, axs = plt.subplots(2,2, figsize=(10,8))
axs[0,0].plot(x8, y8a)
axs[0,0].set_title("Linea")
axs[0,1].bar(cat5, val5, color="orange")
axs[0,1].set_title("Barras")
axs[1,0].scatter(x4, y4, color="green")
axs[1,0].set_title("Scatter")
axs[1,1].hist(data8, bins=20, color="red")
axs[1,1].set_title("Histograma")
plt.suptitle("Ejercicio 8")
plt.tight_layout()
plt.show()

# 9. Grafica una línea con marcadores personalizados (por ejemplo, círculos rojos) y línea punteada.
x9 = np.linspace(0,10,20)
y9 = x9**2
plt.figure()
plt.plot(x9, y9, 'o--', color="red")
plt.title("Ejercicio 9")
plt.show()

# 10. Crea un gráfico de barras apiladas (stacked bar) con dos series de datos.
bar10 = np.array([[3,5,7,9,11],[2,4,6,8,10]])
plt.figure()
plt.bar(np.arange(5), bar10[0], label="Serie1")
plt.bar(np.arange(5), bar10[1], bottom=bar10[0], label="Serie2")
plt.legend()
plt.title("Ejercicio 10")
plt.show()

# 11. Dibuja un gráfico de áreas (area plot) con varias series apiladas.
x11 = np.arange(1,6)
y11 = np.array([x11, x11*2, x11*0.5])
plt.figure()
plt.stackplot(x11, y11, labels=["Serie1","Serie2","Serie3"], colors=["red","green","blue"])
plt.legend()
plt.title("Ejercicio 11")
plt.show()

# 12. Grafica un boxplot con varios conjuntos de datos aleatorios.
data12 = [np.random.randn(50) for _ in range(4)]
plt.figure()
plt.boxplot(data12, tick_labels=["A","B","C","D"])
plt.title("Ejercicio 12")
plt.show()

# 13. Crea un gráfico de contorno (contour plot) de la función z = sin(x) + cos(y) en una malla.
x13 = np.linspace(-3,3,50)
y13 = np.linspace(-3,3,50)
X13,Y13 = np.meshgrid(x13,y13)
Z13 = np.sin(X13)+np.cos(Y13)
plt.figure()
plt.contourf(X13,Y13,Z13, cmap="viridis")
plt.colorbar()
plt.title("Ejercicio 13")
plt.show()

# 14. Dibuja un gráfico de violín (violin plot) comparando varias distribuciones aleatorias.
data14 = [np.random.randn(100) for _ in range(4)]
plt.figure()
plt.violinplot(data14)
plt.title("Ejercicio 14")
plt.show()

# 15. Agrega anotaciones (annotations) a un gráfico de línea, marcando el punto máximo con texto y una flecha.
x15 = np.linspace(0,10,100)
y15 = np.sin(x15)
plt.figure()
plt.plot(x15, y15)
max_idx = np.argmax(y15)
plt.annotate("Maximo", xy=(x15[max_idx], y15[max_idx]),
             xytext=(x15[max_idx]+1, y15[max_idx]+0.5),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.title("Ejercicio 15")
plt.show()

# 16. Crea un gráfico polar con una espiral o una rosa polar.
theta16 = np.linspace(0, 4*np.pi, 100)
r16 = theta16
plt.figure()
ax16 = plt.subplot(111, polar=True)
ax16.plot(theta16, r16)
plt.title("Ejercicio 16")
plt.show()

# 17. Usa estilos predefinidos de Matplotlib (como 'ggplot' o 'seaborn') y compara dos gráficos con diferentes estilos.
plt.style.use('ggplot')
plt.figure()
plt.plot(x1, y1)
plt.title("Ejercicio 17 - ggplot")
plt.show()

plt.style.use('bmh')
plt.figure()
plt.plot(x1, y1)
plt.title("Ejercicio 17 - bmh")
plt.show()


# 18. Grafica datos de un DataFrame de Pandas (crea uno simple) usando el método .plot().
df18 = pd.DataFrame({"A": [1,2,3,4], "B":[4,3,2,1]})
df18.plot()
plt.title("Ejercicio 18")
plt.show()

# 19. Crea un gráfico 3D de líneas o superficie usando axes3d.
fig19 = plt.figure()
ax19 = fig19.add_subplot(111, projection='3d')
z19 = np.linspace(0,10,100)
x19 = np.sin(z19)
y19 = np.cos(z19)
ax19.plot(x19, y19, z19)
ax19.set_title("Ejercicio 19")
plt.show()

# 20. Guarda un gráfico en diferentes formatos (PNG, PDF, SVG) y ajusta parámetros como dpi y tamaño de figura.
plt.figure()
plt.plot(x1, y1)
plt.title("Ejercicio 20")
plt.savefig("ejercicio20.png", dpi=150)
plt.savefig("ejercicio20.pdf")
plt.savefig("ejercicio20.svg")
plt.show()