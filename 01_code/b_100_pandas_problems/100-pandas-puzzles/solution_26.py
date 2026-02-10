import pandas as pd
import numpy as np

nan = np.nan

data = [[0.04,  nan,  nan, 0.25,  nan, 0.43, 0.71, 0.51,  nan,  nan],
        [ nan,  nan,  nan, 0.04, 0.76,  nan,  nan, 0.67, 0.76, 0.16],
        [ nan,  nan, 0.5 ,  nan, 0.31, 0.4 ,  nan,  nan, 0.24, 0.01],
        [0.49,  nan,  nan, 0.62, 0.73, 0.26, 0.85,  nan,  nan,  nan],
        [ nan,  nan, 0.41,  nan, 0.05,  nan, 0.61,  nan, 0.48, 0.68]]

columns = list('abcdefghij')

df = pd.DataFrame(data, columns=columns)

# Solución "Lógica Python" (paso a paso, estilo bucles)
def find_third_nan_python(df):
    result = []
    # Iteramos por cada índice y fila del DataFrame
    for index, row in df.iterrows():
        nan_count = 0
        # Iteramos por cada columna y valor en la fila
        for col, value in row.items():
            if pd.isna(value):
                nan_count += 1
                if nan_count == 3:
                    result.append(col)
                    break
    return pd.Series(result, index=df.index)

print("--- Solución Python ---")
result_python = find_third_nan_python(df)
print(result_python)

# Solución "Pandas Way" (Vectorizada)
print("\n--- Solución Pandas ---")
# 1. df.isnull() nos dice dónde hay NaNs (True/False)
# 2. .cumsum(axis=1) va sumando cuántos NaNs hemos visto en esa fila hasta ese punto
# 3. Buscamos dónde esa suma acumulada sea == 3
# 4. Además, debe ser un NaN (para evitar contar valores que vienen DESPUÉS del 3er NaN y mantienen el conteo en 3)
mask = (df.isnull().cumsum(axis=1) == 3) & df.isnull()

# .idxmax(axis=1) nos devuelve el índice (nombre de columna) del primer True que encuentre en cada fila
solution = mask.idxmax(axis=1)
print(solution)
