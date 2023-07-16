# Agregar o eliminar datos con Pandas
import pandas as pd
import numpy as np

df_books = pd.read_csv('bestsellers-with-categories.csv', sep=',', header=0)
'''
print(df_books.head(2))

# Drop columns
# Con está función lo borra de la salida por consola (quiere decir que no se borra del archivo)
print(df_books.drop('Genre',axis= 1).head(2))

# Si lo queremos borrar total mente, hasta en el archivo-->
#print(df_books.drop('Genre',axis= 1, inplace = True))

# Está es una función de Python que tambien podria borrar
del df_books['Price']
print(df_books.head(2))
'''
# Drop rows

df_books.drop(0,axis=0).head(2)

# Eliminar un conjunto de filas mediante una lista
df_books.drop([0,1,2],axis=0).head(2)

# Elimina un conjunto de filas mediante un rango
df_books.drop(range(0,10),axis=0).head(2)

# Agregar una nueva columna con valores Nan
df_books['Nueva_Columna'] = np.nan
#print(df_books.head(2))

# Mostrar el número de filas que tiene un DataFrame
df_books.shape[0]

# Agregar valores a una nueva columna
data = np.arange(0, df_books.shape[0])
 
# Crear una nueva columna y agregar los valores almacenados en el array
df_books['Rango'] = data

# Para añadir filas se utiliza la función append de Python añadiendo como parámetro una lista, diccionario o añadiendo los valores manualmente.
#df_books.append(df_books)
print(df_books=pd.concat([df_books,df_books.iloc[0].to_frame().T]))
