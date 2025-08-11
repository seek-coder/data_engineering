# Basic concepts

import pandas as pd

# Crear dataframes
df = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], columns= ["A", "B", "C"]
) # generalmente no se arma manualmente, sino que se sigue el proceso ETL (Extraction, Transformation and Load)

print(df, "\n")

# Mostrar primera fila
print(df.head(1), "\n")

# Mostrar última fila
print(df.tail(1), "\n")

# Mostrar índices
print(df.index)

# Mostrar info
print(df.info(), "\n") # impacto en memoria
print(df.describe(), "\n")
print(df["A"].unique(), "\n")


