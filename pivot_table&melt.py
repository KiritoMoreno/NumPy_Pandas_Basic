import pandas as pd
import numpy as np

df_books = pd.read_csv('bestsellers-with-categories.csv',sep=',',header=0)

#pivot_table

#Explóralo viendo sus primeras 5 filas:
print(df_books.head(5))

#Aplica pivot_table:
#Como resultado, los valores de Author pasan a formar el índice por fila y los valores de Genre pasan a formar parte de los índices por columna, y el User Rating se mantiene como valor.
df_books.pivot_table(index='Author',columns='Genre',values='User Rating')

#Ejecuta la siguiente variación:
#En este caso tenemos por cada género, la suma a lo largo de los años. Esto es mucho más interesante, ¿verdad? La mejor noticia es que no solo podemos obtener la suma, también podemos obtener la media, la desviación estándar, el conteo, la varianza, etc. Únicamente con cambiar el parámetro aggfunc que traduce función de agrupamiento.
df_books.pivot_table(index='Genre',columns='Year', values='User Rating',aggfunc='sum')


#melt

#Para ello ejecuta la siguiente línea en tu Jupyter Notebook:
#simplemente al imprimir las cinco primeras filas del DataFrame con las columnas de Name y Genre se tiene este resultado.
df_books[['Name','Genre']].head(5)

#Aplica melt de la siguiente manera:
#Ahora cada resultado de las dos columnas pasa a una fila de este modo a tipo llave:valor.
df_books[['Name','Genre']].head(5).melt() 

#En el siguiente ejemplo ejecutemos melt de esta manera:
#Simplemente, podemos seleccionar las columnas que no quiero hacer melt usando el parámetro id_vars. Para este caso Year y también la única columna que quiero aplicar el melt, para este caso Genre con la propiedad value_vars.
df_books.melt(id_vars='Year',value_vars='Genre')