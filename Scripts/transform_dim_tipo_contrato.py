# 1 - Bibliotecas

import pandas as pd
import openpyxl
import os

# 2 - Lendo arquivo dim_tipo_contrato

input_path = "../Data/2 - Bronze/dim_tipo_contrato.parquet"
output_path = "../Data/3 - Silver"

df = pd.read_parquet(input_path)

df

# 3 - Renomeando colunas

df = df.rename(columns={'Cód T. Contrato': 'cod_tipo_contrato', 
                        'Tipo Contrato': 'tipo_contrato',})

# 4 - Tipando as colunas do data frame

tipos = { 
    'cod_tipo_contrato': 'Int64',
    'tipo_contrato': 'string',
}

df = df.astype(tipos)

# 5 - Garantir que os IDs das situações sempre sejam numéricos 

df['cod_tipo_contrato'] = pd.to_numeric(df['cod_tipo_contrato'], errors='coerce')

# 6 - Padronizando os dados do tipo string para maíusculo

colunas_texto = df.select_dtypes(include=['string']).columns

for col in colunas_texto:
    df[col] = df[col].str.upper().str.strip()

df

# 7 - Enviando dim_tipo_contrato tratada para a camada silver

df.to_parquet(os.path.join(output_path, "dim_tipo_contrato.parquet"), index=False)


