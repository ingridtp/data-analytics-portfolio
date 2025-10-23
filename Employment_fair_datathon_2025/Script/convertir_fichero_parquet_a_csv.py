import pandas as pd

pd.set_option('display.max_columns', None)  # Muestra todas las columnas
pd.set_option('display.width', None)        # No corta la línea

# Ruta al archivo parquet
df = pd.read_parquet("Mostra Set de dades 1_ Consum total agregat.parquet")

print(df.head())

# Ruta al archivo convertido a csv
df.to_csv('libro1.csv', index=False) 
