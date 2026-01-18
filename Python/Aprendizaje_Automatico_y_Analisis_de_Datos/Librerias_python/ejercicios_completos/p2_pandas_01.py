import pandas as pd
import numpy as np
from pprint import pprint

#Ejercicios

### Preparación común (ejecuta esto al principio)

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
print("\nEJ1: Primeras 8 filas")
print(df.head(8))
print("\nEJ1: Ultimas 5 filas")
print(df.tail(5))

#2. ¿Cuántas filas y columnas tiene el DataFrame?
print("Filas y columnas:", df.shape)

#3. Muestra solo los nombres de las columnas y sus tipos de datos.
print("\nEJ3: Tipos de datos por columna")
print(df.dtypes)

#4. ¿Cuántos valores nulos hay en cada columna?
print("\nEJ4: Valores nulos por columna")
print(df.isna().sum())

#5. Selecciona solo la columna `nombre` como Series y como DataFrame.
print("\nEJ5: Columna nombre como Series")
print(df['nombre'])
print("\nEJ5: Columna nombre como DataFrame")
print(df[['nombre']])

#6. Selecciona las columnas `nombre`, `edad` y `salario`.
print("\nEJ6: Columnas nombre, edad y salario")
print(df[['nombre', 'edad', 'salario']])

#7. Muestra las filas de la posición 5 a la 12 (inclusive) usando `iloc`.
print("\nEJ7: Filas 5 a 12 (iloc)")
print(df.iloc[5:13])

#8. Muestra las filas con índice 0, 5, 10 y 15 usando `loc`.
print("\nEJ8: Filas con indices 0, 5, 10 y 15 (loc)")
print(df.loc[[0, 5, 10, 15]])

#9. Filtra los empleados que tienen más de 45 años.
print("\nEJ9: Empleados con edad > 45")
print(df[df['edad'] > 45])

#10. Filtra los empleados de Madrid que estén activos.
print("\nEJ10: Empleados de Madrid activos")
print(df[(df['ciudad'] == 'Madrid') & (df['activo'] == True)])

#11. Filtra los empleados cuyo nombre empiece por 'A' o 'M'.
print("\nEJ11: Nombres que empiezan por A o M")
print(df[df['nombre'].str.startswith(('A', 'M'))])

#12. Crea una nueva columna `salario_anual` que sea el salario × 14 (12 meses + 2 pagas extra).
df['salario_anual'] = df['salario'] * 14
print("\nEJ12: Salario anual")
print(df[['nombre', 'salario', 'salario_anual']])

#13. Crea una columna `antiguedad_años` redondeada (hoy - fecha_ingreso).
hoy = pd.Timestamp.today()
df['antiguedad_años'] = ((hoy - df['fecha_ingreso']).dt.days / 365).round(0)
print("\nEJ13: Antiguedad en anos")
print(df[['nombre', 'fecha_ingreso', 'antiguedad_años']])

#14. Crea una columna `categoria_edad` que sea:  
#    - "Joven" (< 30), "Adulto" (30-45), "Senior" (> 45)
df['categoria_edad'] = pd.cut(
    df['edad'],
    bins=[0, 29, 45, 120],
    labels=['Joven', 'Adulto', 'Senior']
)
print("\nEJ14: Categoria de edad")
print(df[['nombre', 'edad', 'categoria_edad']])

#15. Aumenta un 10% el salario a todos los empleados del departamento IT.
df.loc[df['departamento'] == 'IT', 'salario'] *= 1.10
print("\nEJ15: Salario tras incremento en IT")
print(df[['nombre', 'departamento', 'salario']])

#16. Rellena los salarios nulos con la media del salario por departamento.
df['salario'] = df.groupby('departamento')['salario'].transform(
    lambda x: x.fillna(x.mean())
)
print("\nEJ16: Salarios sin valores nulos")
print(df[['nombre', 'departamento', 'salario']])

#17. Elimina todas las filas donde `bono` sea nulo.
df = df.dropna(subset=['bono'])
print("\nEJ17: Numero de filas tras eliminar bonos nulos")
print(df.shape[0])

#18. Ordena el DataFrame por salario de forma descendente.
print("\nEJ18: DataFrame ordenado por salario (desc)")
print(df.sort_values(by='salario', ascending=False)[['nombre', 'salario']])

#19. Ordena primero por ciudad (asc) y luego por salario (desc).

print("\nEJ19: Ordenado por ciudad y salario")
print(df.sort_values(by=['ciudad', 'salario'], ascending=[True, False])[['nombre', 'ciudad', 'salario']])

#20. ¿Cuál es el salario medio, máximo y mínimo por departamento?
print("\nEJ20: Estadisticas por departamento")
print(df.groupby('departamento')['salario'].agg(['mean', 'max', 'min']))

#21. ¿Cuántos empleados hay por ciudad? Muestra también el salario medio.
print("\nEJ21: Empleados y salario medio por ciudad")
print(df.groupby('ciudad').agg(
        empleados=('nombre', 'count'),
        salario_medio=('salario', 'mean')
        )
    )

#22. Calcula el salario total (salario + bono) y llámalo `compensacion_total`.  Luego ordena de mayor a menor compensación.
df['compensacion_total'] = df['salario'] + df['bono']
print("\nEJ22: Compensacion total ordenada")
print(df.sort_values(by='compensacion_total', ascending=False)[['nombre', 'compensacion_total']])

#23. Usando `groupby`, encuentra el empleado con mayor salario de cada departamento (nombre y salario).
idx = df.groupby('departamento')['salario'].idxmax()
print("\nEJ23: Empleado con mayor salario por departamento")
print(df.loc[idx, ['departamento', 'nombre', 'salario']])

#24. Crea una tabla pivot que muestre el salario medio por departamento (filas) y ciudad (columnas).
print("\nEJ24: Tabla pivot salario medio por departamento y ciudad")
print(pd.pivot_table(
    df,
    values='salario',
    index='departamento',
    columns='ciudad',
    aggfunc='mean'
    )
)

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
print("\nEJ25: Objetivos por empleado")
print(df[['nombre', 'departamento', 'objetivo_ventas']])

#26. Con los datos unidos, crea una columna `cumple_objetivo` que sea True si el departamento tiene objetivo y el salario > 60000 (simulación simple).
df['cumple_objetivo'] = (df['objetivo_ventas'].notna()) & (df['salario'] > 60000)
print("\nEJ26: Cumple objetivo")
print(df[['nombre', 'departamento', 'salario', 'cumple_objetivo']])

#27. Guarda el DataFrame final en CSV y en Excel (dos archivos distintos). 
# instalar openpyxl en el entorno virtual
df.to_csv('empleados_final.csv', index=False)
df.to_excel('empleados_final.xlsx', index=False)
print("\nEJ27: Archivos guardados (CSV y Excel)")

#28. Lee de nuevo el CSV que acabas de guardar y comprueba que todo está igual.
df_leido = pd.read_csv('empleados_final.csv')
print("\nEJ28: Lectura CSV (primeras filas)")
print(df_leido.head())
print("Columnas iguales:", list(df.columns) == list(df_leido.columns))

#29. Trabaja con fechas:  
#    - Extrae el año y el mes de `fecha_ingreso` en columnas nuevas.  
#    - Filtra los empleados que entraron en 2020 o después.
df['anio_ingreso'] = pd.to_datetime(df['fecha_ingreso']).dt.year
df['mes_ingreso'] = pd.to_datetime(df['fecha_ingreso']).dt.month
print("\nEJ29: Empleados con ingreso desde 2020")
print(df[df['anio_ingreso'] >= 2020][['nombre', 'fecha_ingreso', 'anio_ingreso']])

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

print("\nEJ30: Resumen final")
pprint(resumen_dataframe(df))
