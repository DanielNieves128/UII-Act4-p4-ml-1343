import pandas as pd
import numpy as np
# Daniel Nieves NC=1343
n_filas=5
n_columnas=5
tag_columnas=tuple('ABCDE') # etiquetas para las columnas de una tupla
print(tag_columnas)
matriz=np.random.randint(1, 6, size=(n_filas, n_columnas))
print("genera matriz de 5 filas por 5 columnas")
print("con numeros aleatorios comprendidos entre 1 y 10")
print(matriz)
# la variable df es DataFrame
df=pd.DataFrame(matriz, columns= tag_columnas)
print("--- La tabla o dataframe ---NC=1343")
print(df)
print("Daniel Nieves NC=1343")