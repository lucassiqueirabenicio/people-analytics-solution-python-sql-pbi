# 1 - Bibliotecas

import pandas as pd
import openpyxl
import os

# 2 - Lendo arquivo fato_contrato
def executar_transform_fato_contrato():

    DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

    input_path = os.path.join(DIRETORIO_ATUAL, "..", "Data", "2 - Bronze", "fato_contrato.parquet")

    output_path = os.path.join(DIRETORIO_ATUAL, "..","Data", "3 - Silver")

    df = pd.read_parquet(input_path)

    df

    # 3 - Renomeando colunas

    df = df.rename(columns={'Cód Funcionário': 'cod_funcionario', 
                            'Cód Cargo': 'cod_cargo',
                            'Cód Escala': 'cod_escala',
                            'Cód C.Custo': 'cod_centro_custo',
                            'Cód T. Contrato': 'cod_tipo_contrato',
                            'Cód Situação': 'cod_situacao',
                            'Data Admissão': 'data_admissao',
                            'Data Salário': 'data_salario',
                            'Data Afastamento': 'data_afastamento',
                            'Valor Salário': 'valor_salario',})

    # 4 - Tipando colunas do data frame

    tipos = { 
        'cod_funcionario': 'Int64',
        'cod_cargo': 'Int64',
        'cod_escala': 'Int64',
        'cod_centro_custo': 'string',
        'cod_tipo_contrato': 'Int64',
        'cod_situacao': 'Int64',
        'cod_situacao': 'Int64',
        'valor_salario': 'float'
    }

    df = df.astype(tipos)

    df['data_admissao'] = pd.to_datetime(df['data_admissao'], format='%d/%m/%Y', errors='coerce')
    df['data_salario'] = pd.to_datetime(df['data_salario'], format='%d/%m/%Y', errors='coerce')
    df['data_afastamento'] = pd.to_datetime(df['data_afastamento'], format='%d/%m/%Y', errors='coerce')

    df

    # 5 - Garantir que os IDs dos funcionarios sempre sejam numéricos 

    df['cod_funcionario'] = pd.to_numeric(df['cod_funcionario'], errors='coerce')

    # 6 - Padronizando os dados do tipo string para maísculo

    colunas_texto = df.select_dtypes(include=['string']).columns

    for col in colunas_texto:
        df[col] = df[col].str.upper().str.strip()

    df

    # 7 - Enviando fato_contrato tratada para a camada silver

    df.to_parquet(os.path.join(output_path, "fato_contrato.parquet"), index=False)


if __name__ == "__main__":
    executar_transform_fato_contrato()
