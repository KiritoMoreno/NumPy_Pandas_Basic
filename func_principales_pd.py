#Funciones principales de Pandas
import pandas as pd

df_books = pd.read_csv('bestsellers-with-categories.csv',sep=',', header=0)

#Mostrar las primeras dos líneas de registro
df_books.head(2) 

#Mostrar los diferentes datos que contiene el DataFrame
# Inicialmente para el analisis al dataframe
df_books.info()

#Obtener diferentes datos estadísticos de las columnas numéricas.
df_books.describe()

#Mostrar los últimos 5 registros del DataFrame
df_books.tail()

#Obtener el uso de la memoria de cada columna (al nivel tecnico)
df_books.memory_usage(deep=True)

#Obtener cuantos datos tenemos de algo en específico
df_books['Author'].value_counts()

#Eliminar registros duplicados
df_books.drop_duplicates()

#Ordenar los registros según valores de la columna (orden ascendente)
df_books.sort_values('Year')

#Ordenar los registros según valores de la columna (orden descendente)
df_books.sort_values('Year', ascending=False)
