# 1 - Bibliotecas

import pandas as pd
import openpyxl
import os

# 2 - Lendo arquivo dim_situacao

input_path = "../Data/2 - Bronze/dim_situacao.parquet"
output_path = "../Data/3 - Silver"

df = pd.read_parquet(input_path)

df

# 3 - Renomeando colunas

df = df.rename(columns={'Cód Situação': 'cod_situacao', 
                        'Situação': 'situacao',})

# 4 - Tipando as colunas do data frame e tratando datas fora do padrão

tipos = { 
    'cod_situacao': 'Int64',
    'situacao': 'string',
}

df = df.astype(tipos)

# 5 - Garantir que os IDs das situações sempre sejam numéricos 

df['cod_situacao'] = pd.to_numeric(df['cod_situacao'], errors='coerce')

# 6 - Padronizando os dados do tipo string para maíusculo

colunas_texto = df.select_dtypes(include=['string']).columns

for col in colunas_texto:
    df[col] = df[col].str.upper().str.strip()

df

# %% [markdown]
# 7 - Enviando dim_situacao tratada para a camada silver

# %%
df.to_parquet(os.path.join(output_path, "dim_situacao.parquet"), index=False)


