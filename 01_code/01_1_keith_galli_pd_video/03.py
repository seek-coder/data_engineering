# Accesing Data with Pandas

import pandas as pd

coffee = pd.read_csv("01_code/01_1_keith_galli_pd_video/resources/warmup-data/coffee.csv") # en crudo (raw) desde el repo

print(coffee.sample(10), "\n") # random data

# Información específica mediante rows y columns (loc)
print(coffee.loc[[0, 2, 3, 7]], "\n") # valores específicos
print(coffee.loc[0:5], "\n") # slice
print(coffee.loc[7:10], "\n")
print(coffee.loc[7:10, ["Day", "Units Sold"]], "\n") # sólo ciertas columnas (case sensitive)

# coffee.index = coffee["Day"]

print(coffee.loc["Monday":"Wednesday"])

# Información específica mediante rows y columns pero sólo usando índex values (iloc)
print(coffee.iloc[7:10], "\n")

# Para setear data podemos usar...

coffee.loc[1, "Units Sold"] = 12
print(coffee.head())

# iat y at son formas mejoradas, pero no tan usadas, de iloc y loc

print(coffee.at[0, "Units Sold"]) # ¡y no me deja usar intervalos!

# 21:16