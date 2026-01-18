import pandas as pd
import numpy as np

'''
https://pandas.pydata.org/
https://pandas.pydata.org/docs/getting_started/intro_tutorials/
https://www.w3schools.com/python/pandas/default.asp
https://www.datacamp.com/es/tutorial/pandas
'''

def ejemplo1():
    #Tipo de datos similar a un array
    # Serie desde lista
    serie = pd.Series([10, 20, 30])
    print(1,type(serie),serie)

    # Serie desde diccionario
    serie_dict = pd.Series({'a': 10, 'b': 20, 'c': 30})
    print(2,type(serie_dict),serie_dict)
    
    # Tipo de datos similar a una matriz. Puede tener etiquetas para las filas o las columnas
    # DataFrame desde diccionario
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    print(3,type(df))
    print("----")
    print(df)
    print("----")
    print(df['A'])
    print(df['B'][1])
    fila = df.iloc[0]
    print(fila)
    print(fila.iloc[1])  

def cargaryFiltrarDataset():

    # Paso 1: Cargar el archivo CSV
    df = pd.read_csv('titanic.csv') #https://www.kaggle.com/datasets/heptapod/titanic?resource=download

    # Paso 2: Seleccionar solo algunas columnas
    columnas_seleccionadas = ['Passengerid', 'Sex', 'Age', 'Survived'] 
    df_filtrado = df[columnas_seleccionadas]

    # Paso 3: Guardar el nuevo DataFrame en un archivo CSV
    df_filtrado.to_csv('titanic_filtrado.csv', index=False)  # index=False para no guardar el índice
    
def estadisticas():

    # Paso 1: Cargar el archivo CSV descargado de Kaggle
    df = pd.read_csv('titanic.csv') 
        
    print(df.describe())
    print("----------------------")
    print(df['Age'].value_counts())#Numero de individuos de cada edad
    
def filtrado():    
    df = pd.read_csv('titanic.csv') 
        
    df_filtrado = df[df['Age'] > 30]#nos quedamos con los individuos mayores de 30
    print(df_filtrado['Age'].value_counts())# mostramos para comprobar
    
def ejercicio():
    df = pd.read_csv('titanic.csv') 
    #Quedate con los pasajeros de un sexo concreto
     
def limpieza():
    df = pd.read_csv('titanic.csv') 
    df.dropna(inplace=True)         # Eliminar filas con valores nulos
    df.fillna(0, inplace=True)      # Reemplazar nulos por 0
    df.drop_duplicates(inplace=True) # Eliminar duplicados
    df.to_csv('titanic_limpio.csv', index=False)


print("Empezamos")

print(pd.__version__)
ejemplo1()
#cargaryFiltrarDataset()
print("*"*50)
estadisticas()
print("*"*50)
filtrado()
print("*"*50)
ejercicio()
print("*"*50)
limpieza()

print("Fin")



#Ejercicios
'''
### Preparación común (ejecuta esto al principio)

# python
#import pandas as pd
#import numpy as np

# Datos base que usaremos en casi todos los ejercicios
np.random.seed(42)

df = pd.DataFrame({
    'nombre': ['Ana', 'Luis', 'Carlos', 'María', 'Pedro', 'Laura', 'José', 'Sofía', 'Miguel', 'Elena',
               'Pablo', 'Lucía', 'Diego', 'Carmen', 'Raúl', 'Julia', 'Marcos', 'Clara', 'Andrés', 'Valeria'],
    'edad': np.random.randint(22, 60, 20),
    'ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao', 'Madrid', 'Barcelona', 'Málaga', 
               'Valencia', 'Madrid', 'Sevilla', 'Barcelona', 'Madrid', 'Bilbao', 'Valencia', 
               'Málaga', 'Madrid', 'Sevilla', 'Barcelona', 'Valencia'],
    'departamento': ['IT', 'RRHH', 'IT', 'Marketing', 'IT', 'RRHH', 'Marketing', 'IT', 'RRHH', 'Marketing',
                     'IT', 'Marketing', 'RRHH', 'IT', 'Marketing', 'RRHH', 'IT', 'Marketing', 'IT', 'RRHH'],
    'salario': np.random.randint(30000, 90000, 20),
    'fecha_ingreso': pd.date_range('2018-01-01', periods=20, freq='45D'),
    'bono': np.random.randint(0, 15000, 20),
    'activo': [True, True, False, True, True, True, False, True, True, True,
               True, False, True, True, False, True, True, True, True, False]
})

# Añadimos algunos nulos para practicar
df.loc[2:4, 'salario'] = np.nan
df.loc[10:12, 'bono'] = np.nan
df.loc[5, 'ciudad'] = np.nan
'''

### Ejercicios

#1. Muestra las primeras 8 filas y las últimas 5 filas del DataFrame.

#2. ¿Cuántas filas y columnas tiene el DataFrame?

#3. Muestra solo los nombres de las columnas y sus tipos de datos.
#4. ¿Cuántos valores nulos hay en cada columna?
#5. Selecciona solo la columna `nombre` como Series y como DataFrame.
#6. Selecciona las columnas `nombre`, `edad` y `salario`.
#7. Muestra las filas de la posición 5 a la 12 (inclusive) usando `iloc`.
#8. Muestra las filas con índice 0, 5, 10 y 15 usando `loc`.
#9. Filtra los empleados que tienen más de 45 años.
#10. Filtra los empleados de Madrid que estén activos.

#11. Filtra los empleados cuyo nombre empiece por 'A' o 'M'.
#12. Crea una nueva columna `salario_anual` que sea el salario × 14 (12 meses + 2 pagas extra).

#13. Crea una columna `antiguedad_años` redondeada (hoy - fecha_ingreso).

#14. Crea una columna `categoria_edad` que sea:  
#    - "Joven" (< 30), "Adulto" (30-45), "Senior" (> 45)
#15. Aumenta un 10% el salario a todos los empleados del departamento IT.
#16. Rellena los salarios nulos con la media del salario por departamento.
#17. Elimina todas las filas donde `bono` sea nulo.
#18. Ordena el DataFrame por salario de forma descendente.
#19. Ordena primero por ciudad (asc) y luego por salario (desc).
#20. ¿Cuál es el salario medio, máximo y mínimo por departamento?
#21. ¿Cuántos empleados hay por ciudad? Muestra también el salario medio.

#22. Calcula el salario total (salario + bono) y llámalo `compensacion_total`.  Luego ordena de mayor a menor compensación.
#23. Usando `groupby`, encuentra el empleado con mayor salario de cada departamento (nombre y salario).
#24. Crea una tabla pivot que muestre el salario medio por departamento (filas) y ciudad (columnas).
#25. Une este DataFrame con el siguiente (simula una tabla de objetivos):
''' python
    objetivos = pd.DataFrame({
        'departamento': ['IT', 'RRHH', 'Marketing'],
        'objetivo_ventas': [500000, 200000, 800000]
    })
'''
#Haz un merge para añadir el objetivo a cada empleado.

#26. Con los datos unidos, crea una columna `cumple_objetivo` que sea True si el departamento tiene objetivo y el salario > 60000 (simulación simple).
#27. Guarda el DataFrame final en CSV y en Excel (dos archivos distintos).
#28. Lee de nuevo el CSV que acabas de guardar y comprueba que todo está igual.
#29. Trabaja con fechas:  
#    - Extrae el año y el mes de `fecha_ingreso` en columnas nuevas.  
#    - Filtra los empleados que entraron en 2020 o después.

#30. (Reto final) Crea una función que reciba un DataFrame y devuelva un resumen con:
#    - Número total de empleados
#    - Salario medio y mediana
#    - Departamento con mayor salario medio
#    - Porcentaje de empleados activos
#    - Ciudad con más empleados

