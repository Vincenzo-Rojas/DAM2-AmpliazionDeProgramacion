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

'''
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
'''


#Ejercicios

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


### Ejercicios

#1. Muestra las primeras 8 filas y las últimas 5 filas del DataFrame.
print(df.head(8))
print(df.tail(5))

#2. ¿Cuántas filas y columnas tiene el DataFrame?
print("Filas y columnas:", df.shape)

#3. Muestra solo los nombres de las columnas y sus tipos de datos.
print(df.dtypes)

#4. ¿Cuántos valores nulos hay en cada columna?
print(df.isna().sum())

#5. Selecciona solo la columna `nombre` como Series y como DataFrame.
serie_nombre = df['nombre']
df_nombre = df[['nombre']]
print(serie_nombre)
print(df_nombre)

#6. Selecciona las columnas `nombre`, `edad` y `salario`.
print(df[['nombre', 'edad', 'salario']])

#7. Muestra las filas de la posición 5 a la 12 (inclusive) usando `iloc`.
print(df.iloc[5:13])

#8. Muestra las filas con índice 0, 5, 10 y 15 usando `loc`.
print(df.loc[[0, 5, 10, 15]])

#9. Filtra los empleados que tienen más de 45 años.
print(df[df['edad'] > 45])

#10. Filtra los empleados de Madrid que estén activos.
print(df[(df['ciudad'] == 'Madrid') & (df['activo'] == True)])

#11. Filtra los empleados cuyo nombre empiece por 'A' o 'M'.
print(df[df['nombre'].str.startswith(('A', 'M'))])

#12. Crea una nueva columna `salario_anual` que sea el salario × 14 (12 meses + 2 pagas extra).
df['salario_anual'] = df['salario'] * 14
print(df[['nombre', 'salario', 'salario_anual']])

#13. Crea una columna `antiguedad_años` redondeada (hoy - fecha_ingreso).
hoy = pd.Timestamp.today()
df['antiguedad_anos'] = ((hoy - df['fecha_ingreso']).dt.days / 365).round(0)
print(df[['nombre', 'fecha_ingreso', 'antiguedad_anos']])

#14. Crea una columna `categoria_edad` que sea:  
#    - "Joven" (< 30), "Adulto" (30-45), "Senior" (> 45)
df['categoria_edad'] = pd.cut(
    df['edad'],
    bins=[0, 29, 45, 120],
    labels=['Joven', 'Adulto', 'Senior']
)
print(df[['nombre', 'edad', 'categoria_edad']])

#15. Aumenta un 10% el salario a todos los empleados del departamento IT.
df.loc[df['departamento'] == 'IT', 'salario'] *= 1.10
print(df[['nombre', 'departamento', 'salario']])

#16. Rellena los salarios nulos con la media del salario por departamento.
df['salario'] = df.groupby('departamento')['salario'].transform(
    lambda x: x.fillna(x.mean())
)
print(df[['nombre', 'departamento', 'salario']])

#17. Elimina todas las filas donde `bono` sea nulo.
df = df.dropna(subset=['bono'])
print("Filas tras eliminar bonos nulos:", df.shape[0])

#18. Ordena el DataFrame por salario de forma descendente.
df_ordenado_salario = df.sort_values(by='salario', ascending=False)
print(df_ordenado_salario[['nombre', 'salario']])

#19. Ordena primero por ciudad (asc) y luego por salario (desc).
df_ordenado_ciudad_salario = df.sort_values(
    by=['ciudad', 'salario'],
    ascending=[True, False]
)
print(df_ordenado_ciudad_salario[['nombre', 'ciudad', 'salario']])

#20. ¿Cuál es el salario medio, máximo y mínimo por departamento?
estadisticas_dep = df.groupby('departamento')['salario'].agg(['mean', 'max', 'min'])
print(estadisticas_dep)

#21. ¿Cuántos empleados hay por ciudad? Muestra también el salario medio.
empleados_ciudad = df.groupby('ciudad').agg(
    empleados=('nombre', 'count'),
    salario_medio=('salario', 'mean')
)
print(empleados_ciudad)

#22. Calcula el salario total (salario + bono) y llámalo `compensacion_total`.  Luego ordena de mayor a menor compensación.
df['compensacion_total'] = df['salario'] + df['bono']
df_comp = df.sort_values(by='compensacion_total', ascending=False)
print(df_comp[['nombre', 'compensacion_total']])

#23. Usando `groupby`, encuentra el empleado con mayor salario de cada departamento (nombre y salario).
idx = df.groupby('departamento')['salario'].idxmax()
mayor_salario_dep = df.loc[idx, ['departamento', 'nombre', 'salario']]
print(mayor_salario_dep)

#24. Crea una tabla pivot que muestre el salario medio por departamento (filas) y ciudad (columnas).
tabla_pivot = pd.pivot_table(
    df,
    values='salario',
    index='departamento',
    columns='ciudad',
    aggfunc='mean'
)
print(tabla_pivot)

#25. Une este DataFrame con el siguiente (simula una tabla de objetivos):

''' python
    objetivos = pd.DataFrame({
        'departamento': ['IT', 'RRHH', 'Marketing'],
        'objetivo_ventas': [500000, 200000, 800000]
    })
'''
#Haz un merge para añadir el objetivo a cada empleado.

objetivos = pd.DataFrame({
    'departamento': ['IT', 'RRHH', 'Marketing'],
    'objetivo_ventas': [500000, 200000, 800000]
})

df = df.merge(objetivos, on='departamento', how='left')
print(df[['nombre', 'departamento', 'objetivo_ventas']])

#26. Con los datos unidos, crea una columna `cumple_objetivo` que sea True si el departamento tiene objetivo y el salario > 60000 (simulación simple).
df['cumple_objetivo'] = (df['objetivo_ventas'].notna()) & (df['salario'] > 60000)
print(df[['nombre', 'departamento', 'salario', 'cumple_objetivo']])

#27. Guarda el DataFrame final en CSV y en Excel (dos archivos distintos).
df.to_csv('empleados_final.csv', index=False)
df.to_excel('empleados_final.xlsx', index=False)

#28. Lee de nuevo el CSV que acabas de guardar y comprueba que todo está igual.
df_leido = pd.read_csv('empleados_final.csv')
print(df_leido.head())
print("Columnas iguales:", list(df.columns) == list(df_leido.columns))

#29. Trabaja con fechas:  
#    - Extrae el año y el mes de `fecha_ingreso` en columnas nuevas.  
#    - Filtra los empleados que entraron en 2020 o después.
df['anio_ingreso'] = pd.to_datetime(df['fecha_ingreso']).dt.year
df['mes_ingreso'] = pd.to_datetime(df['fecha_ingreso']).dt.month

df_2020 = df[df['anio_ingreso'] >= 2020]
print(df_2020[['nombre', 'fecha_ingreso', 'anio_ingreso']])

#30. (Reto final) Crea una función que reciba un DataFrame y devuelva un resumen con:
#    - Número total de empleados
#    - Salario medio y mediana
#    - Departamento con mayor salario medio
#    - Porcentaje de empleados activos
#    - Ciudad con más empleados

def resumen_dataframe(dataframe):
    return {
        'total_empleados': len(dataframe),
        'salario_medio': dataframe['salario'].mean(),
        'salario_mediana': dataframe['salario'].median(),
        'departamento_mayor_salario_medio':
            dataframe.groupby('departamento')['salario'].mean().idxmax(),
        'porcentaje_activos':
            dataframe['activo'].mean() * 100,
        'ciudad_con_mas_empleados':
            dataframe['ciudad'].value_counts().idxmax()
    }

resumen = resumen_dataframe(df)
print(resumen)
