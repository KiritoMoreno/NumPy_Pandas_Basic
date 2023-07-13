# Filtrado con loc y iloc en los archivos CSV y JSON
import pandas as pd

#.loc
#Filtra según un label
df_books = pd.read_csv('bestsellers-with-categories.csv',sep = ',', header = 0)

print(df_books.loc[0:4]) # Muestra los datos de la fila 0 a la fila 4

# Filtrando por filas y columnas

print(df_books.loc[0:4,['Name', 'Author']])

# Podemos modificar los valores de una columna específica del dataFrame

print(df_books.loc[:,['Reviews']]* -1) # Multiplica por -1 todos los valores de la columna Reviews

# Filtrar datos que cumplan una condición determinada
print(df_books.loc[:,['Author']] == 'JJ Smith') #muestra la columna Author con True en los valores que cumplen la condicion y False para los que no la cumplen

#.iloc
#Filtra mediante índices.
print(df_books.iloc[:]) # Muestra todo

# Filtrar datos según los índices de las filas y las columnas
print(df_books.iloc[:4, 0:2]) # Muestra datos de las filas que van de 0 a 3 y las columnas con indice 0 y 1

# Buscar un dato específico.
print(df_books.iloc[1,3]) # Muestra el dato alojado en la fila 1 columna 3

