# 1 - Bibliotecas

import pandas as pd
import openpyxl
import os

# 2 - Lendo arquivo dim_funcionario.parquet

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(DIRETORIO_ATUAL, "..", "Data", "2 - Bronze", "dim_funcionario.parquet")

output_path = os.path.join(DIRETORIO_ATUAL, "..","Data", "3 - Silver")

df = pd.read_parquet(input_path)

df

# 3 - Renomeando colunas

df = df.rename(columns={'Cód Funcionário': 'cod_funcionario', 
                        'Funcionário': 'funcionario',
                       'Sexo': 'sexo',
                       'Nacionalidade': 'nacionalidade',
                       'Raça': 'raca',
                       'Estado Civil': 'estado_civil',
                       'Escolaridade': 'escolaridade',
                       'Data Nascimento': 'data_nascimento'})

# 4 - Tipando as colunas do data frame e tratando datas fora do padrão

tipos = { 
    'cod_funcionario': 'Int64',
    'funcionario': 'string',
    'sexo': 'string',
    'nacionalidade': 'string',
    'raca': 'string',
    'estado_civil': 'string',
    'escolaridade': 'string',
}

df = df.astype(tipos)

df['data_nascimento'] = pd.to_datetime(df['data_nascimento'], format='%d/%m/%Y', errors='coerce')

# 5 - Garantir que os IDs dos funcionarios sempre sejam numéricos 

df['cod_funcionario'] = pd.to_numeric(df['cod_funcionario'], errors='coerce')

# 6 - Padronizando os dados do tipo string para maíusculo

colunas_texto = df.select_dtypes(include=['string']).columns

for col in colunas_texto:
    df[col] = df[col].str.upper().str.strip()

df

# 7 - Enviando dim_funcionario tratada para a camada silver

df.to_parquet(os.path.join(output_path, "dim_funcionario.parquet"), index=False)


