#APPLY

import pandas as pd
import numpy as np

df_books = pd.read_csv('bestsellers-with-categories.csv',sep=',',header=0)

print(df_books.head(2))

#Creamos nuestra función
def two_times(value):
    return value * 2

#Lo aplicamos a la columna de User Rating
df_books['User Rating'].apply(two_times) # Mucho más eficiente que usar un for

#Podemos guardarlo en una columna nueva
df_books['User Rating2'] =df_books['User Rating'].apply(two_times)

#Se pueden crear lambda functions
df_books['User Rating2'] =df_books['User Rating'].apply(lambda x: x* 3)

#Apply en varias columnas con condiciones, hay que especificar a que los vamos a aplicar (filas o columnas)
df_books.apply(lambda x: x['User Rating'] * 2 if x['Genre'] == 'Fiction' else x['User Rating'], axis = 1)
