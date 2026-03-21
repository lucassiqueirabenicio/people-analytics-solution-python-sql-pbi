# 1 - Bibliotecas

import pandas as pd
import openpyxl
import os

# 2 - Lendo arquivo dim_cargo.parquet

input_path = "../Data/2 - Bronze/dim_cargo.parquet"
output_path = "../Data/3 - Silver"

df = pd.read_parquet(input_path)

df

# 3 - Renomeando colunas

df = df.rename(columns={'Cód Cargo': 'cod_cargo', 
                        'Cargo': 'cargo',
                      })

# 4 - Tipando as colunas do data frame

tipos = { 
    'cod_cargo': 'Int64',
    'cargo': 'string',

}

df = df.astype(tipos)

# 5 - Garantir que os IDs dos cargos sempre sejam numéricos 

df['cod_cargo'] = pd.to_numeric(df['cod_cargo'], errors='coerce')

# 6 - Padronizando os dados do tipo string para maiúsculo

colunas_texto = df.select_dtypes(include=['string']).columns

for col in colunas_texto:
    df[col] = df[col].str.upper().str.strip()

df

# 7 - Enviando dim_cargo para a camada silver

df.to_parquet(os.path.join(output_path, "dim_cargo.parquet"), index=False)


