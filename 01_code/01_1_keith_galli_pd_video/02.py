# Loading in Dataframes from Files

import pandas as pd

# coffee = pd.read_csv("01_code/01_1_keith_galli_pd_video/resources/warmup-data/coffee.csv") # con path relativo

coffee = pd.read_csv("https://raw.githubusercontent.com/seek-coder/data_engineering/refs/heads/main/01_code/01_1_keith_galli_pd_video/resources/warmup-data/coffee.csv?token=GHSAT0AAAAAADECF7GLI54YAMRXHKRZGQCK2EL7LDA") # en crudo (raw) desde el repo

print(coffee.head())

results = pd.read_parquet("01_code/01_1_keith_galli_pd_video/resources/data/results.parquet")

print(results.head())

