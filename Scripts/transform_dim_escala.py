# 1 - Bibliotecas

import pandas as pd
import openpyxl
import os

# 2 - Lendo arquivo dim_funcionário.parquet

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(DIRETORIO_ATUAL, "..", "Data", "2 - Bronze", "dim_escala.parquet")

output_path = os.path.join(DIRETORIO_ATUAL, "..","Data", "3 - Silver")

df = pd.read_parquet(input_path)

df

# 3 - Renomando Colunas

df = df.rename(columns={'Cód Escala': 'cod_escala', 
                        'Escala': 'escala',})

# 4 - Tipando as colunas do data frame

tipos = { 
    'cod_escala': 'Int64',
    'escala': 'string',
}

df = df.astype(tipos)

# 5 - Garantindo que os IDs das escalas sempre sejam numéricos

df['cod_escala'] = pd.to_numeric(df['cod_escala'], errors='coerce')

# 6 - Padronizando os dados do tipo string para maiúsculo

colunas_texto = df.select_dtypes(include=['string']).columns

for col in colunas_texto:
    df[col] = df[col].str.upper().str.strip()

df

# 7 - Enviando dim_escala tratada para a camada silver

df.to_parquet(os.path.join(output_path, "dim_escala.parquet"), index=False)


