#Leer archivos CSV y JSON con Pandas

import pandas as pd

df_book = pd.read_csv('bestsellers-with-categories.csv', sep = ',', header = 0) # tambien le podemos añadir (names= '' ->aqui seria el nombre de las columnas o le podemos cambiar los nombres)

df_book = df_book[df_book['Year'] == 2016] # Podemo hacerle un filtramos 

#JSON
#Para ***agregar un archivo ‘JSON’***, se hace de igual manera, pero en esta ocasión usamos

df_json_book =pd.read_json('hpcharactersdataraw.json')
# df_json_book =pd.read_json('hpcharactersdataraw.json',typ = 'Series') -->Aqui llevamos una estructura JSON a una estructura pandas (typ='')
# Simplemente me va a indexar una lista con los valores que tengo, pero en formato RAW. Esto es un panda series

print(df_book.columns)
print()
print(df_json_book.columns)
print()

# leer el archivo csv world population
df_world = pd.read_csv('world_population.csv', sep = ',', header = 0)
df_world = df_world[df_world['Continent'] == 'South America']

print(df_world)