# 1 - Bibliotecas

import pandas as pd
import openpyxl
import os

# 2 - Lendo arquivo fato_ficha_financeira

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(DIRETORIO_ATUAL, "..", "Data", "2 - Bronze", "fato_ficha_financeira.parquet")

output_path = os.path.join(DIRETORIO_ATUAL, "..","Data", "3 - Silver")

df = pd.read_parquet(input_path)

df

# 3 - Renomeando colunas

df = df.rename(columns={'Matricula': 'cod_funcionario', 
                        'Cargo': 'cargo',
                        'Mês Pag.': 'mes_pagamento',
                        'Evento': 'evento',
                        'Descrição': 'descricao',
                        'Tipo': 'tipo',
                        'Valor': 'valor',
                        })

# 4 - Excluindo linhas de resumo (em branco) do data frame

df.dropna(how='any', inplace=True)
 
df

# 5 - Tipando colunas do data frame

tipos = { 
    'cod_funcionario': 'Int64',
    'cargo': 'string',
    'mes_pagamento': 'string',
    'evento': 'int64',
    'descricao': 'string',
    'tipo': 'string',
    'valor': 'float',
}

df

# 6 - Garantir que os IDs dos funcionarios sempre sejam numéricos 

df['cod_funcionario'] = pd.to_numeric(df['cod_funcionario'], errors='coerce')

# 7 - Padronizando os dados do tipo string para maísculo

colunas_texto = df.select_dtypes(include=['string']).columns

for col in colunas_texto:
    df[col] = df[col].str.upper().str.strip()

df

# 8 - Enviando fato_ficha_financeira tratada para a camada silver

df.to_parquet(os.path.join(output_path, "fato_ficha_financeira.parquet"), index=False)



