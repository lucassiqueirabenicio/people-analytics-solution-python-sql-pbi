# 1 - Bibliotecas

import pandas as pd
import openpyxl
import os
import glob

# 2 - Lendo Arquivo Contratos.xlsx

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

input_path_contratos = os.path.join(DIRETORIO_ATUAL, "..", "Data", "1 - Raw", "Contratos", "Contratos.xlsx")

input_path_ficha_financeira = os.path.join(DIRETORIO_ATUAL, "..", "Data", "1 - Raw", "Ficha Financeira")

output_path = os.path.join(DIRETORIO_ATUAL, "..", "Data", "2 - Bronze")


df_bruto = pd.read_excel(input_path_contratos, dtype=str)

# 3 - Data Frame contratos bruto

df_bruto

# 4 - Criando a dimensão funcionário

colunas_funcionario = ['Cód Funcionário', 'Funcionário', 'Sexo', 'Nacionalidade', 
                'Raça', 'Estado Civil', 'Escolaridade', 'Data Nascimento']

dim_funcionario = df_bruto[colunas_funcionario].drop_duplicates(subset=['Cód Funcionário']).reset_index(drop=True)

dim_funcionario

# 5 - Criando a dimensão cargo

dim_cargo = df_bruto[['Cód Cargo', 'Cargo']].drop_duplicates().reset_index(drop=True)

#dim_cargo

# 6 - Criando a dimensão Centro de Custo

dim_centro_custo = df_bruto[['Cód C.Custo', 'Centro Custo']].drop_duplicates().reset_index(drop=True)

#dim_centro_custo

# 7 - Criando a dimensão Escala

dim_escala = df_bruto[['Cód Escala', 'Escala']].drop_duplicates().reset_index(drop=True)

# 8 - Criando a dimensão Tipo Contrato

dim_tipo_contrato = df_bruto[['Cód T. Contrato', 'Tipo Contrato']].drop_duplicates().reset_index(drop=True)

# 9 - Criando a dimensão Situação 

dim_situacao = df_bruto[['Cód Situação', 'Situação']].drop_duplicates().reset_index(drop=True)

# 10 - Criando a fato contrato

colunas_fato = [
    'Cód Funcionário',      
    'Cód Cargo',           
    'Cód Escala',           
    'Cód C.Custo',          
    'Cód T. Contrato',      
    'Cód Situação',        
    'Data Admissão', 
    'Valor Salário', 
    'Data Salário', 
    'Data Afastamento'
]

fato_contrato = df_bruto[colunas_fato].copy()

# 11 - Salvando as dimensões e fato contratos em arquivo parquet na camada bronze

dim_funcionario.to_parquet(os.path.join(output_path, "dim_funcionario.parquet"), index=False)

dim_cargo.to_parquet(os.path.join(output_path, "dim_cargo.parquet"), index=False)

dim_centro_custo.to_parquet(os.path.join(output_path, "dim_centro_custo.parquet"), index=False)

dim_escala.to_parquet(os.path.join(output_path, "dim_escala.parquet"), index=False)

dim_situacao.to_parquet(os.path.join(output_path, "dim_situacao.parquet"), index=False)

dim_tipo_contrato.to_parquet(os.path.join(output_path, "dim_tipo_contrato.parquet"), index=False)

fato_contrato.to_parquet(os.path.join(output_path, "fato_contrato.parquet"), index=False)

# 12 - Lendo pasta Ficha Financeira, onde os arquivos de ficha financeira estão.

padrao_busca = os.path.join(input_path_ficha_financeira, '*.csv') #Definindo uma regra para a busca dos arquvios csv

arquivos_csv = glob.glob(padrao_busca) #Utilizando o glob para listar os arquivos que batem com o padrão de busca

lista_dfs = [] #Cria uma lista vazia para armazenar cada DataFrame individual temporariamente


print(f"Arquivos encontrados: {len(arquivos_csv)}")

#df_teste = pd.read_csv(arquivos_csv[0], sep=';', encoding='latin1')
#df_teste.head() # Exibe as 5 primeiras linhas do teste

for arquivo in arquivos_csv:

    df_ficha_financeira_temp = pd.read_csv(arquivo, sep=';', encoding='latin1')
    
    lista_dfs.append(df_ficha_financeira_temp)

fato_ficha_financeira = pd.concat(lista_dfs, ignore_index=True)

# 12 - Salvando a fato ficha financeira em arquivo parquet na camada bronze

fato_ficha_financeira.to_parquet(os.path.join(output_path, "fato_ficha_financeira.parquet"), index=False)


