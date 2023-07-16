# Valores Nulos
import pandas as pd
import numpy as np

#Creamos un DataFrame con algunos valores nulos
dict1 = {'Col1' :[1,2,3,np.nan],
         'Col2' :[4,np.nan,6,7],
          'Col3' :['a','b','c',None] }

df = pd.DataFrame(dict1)
print(df)
#Identificar valores nulos en un DataFrame
df.isnull()

#Identificar valores nulos con un valor numérico
df.isnull()* 1

#Sustituir los valores nulos por una cadena
df.fillna('Missing')

#Sustituir valores nulos por una medida estadística realizada con los valores de las columnas
df.fillna(df.mean())

#Sustituir valores nulos por valores de interpolación
#Siempre y cuando sepamos que los datos están de manera estructurada con una serie y una frecuencia exacta
df.interpolate()

#Eliminar valores nulos
df.dropna()
