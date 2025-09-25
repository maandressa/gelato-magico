import numpy as np
import pandas as pd
from pathlib import Path

Path("data").mkdir(exist_ok=True)

np.random.seed(42)
n = 365
temperatura = np.random.uniform(15, 40, size=n)
vendas = (temperatura * 12) + np.random.normal(0, 20, size=n)
vendas = np.maximum(0, vendas).round().astype(int)

df = pd.DataFrame({
    "temperatura": np.round(temperatura, 2),
    "vendas": vendas
})

df.to_csv("data/icecream_sales.csv", index=False)
print("Arquivo gerado: data/icecream_sales.csv ({} linhas)".format(len(df)))
