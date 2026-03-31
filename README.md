# 📊 Data Engineering & Analytics Pipeline: HR Analytics

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=black)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Parquet](https://img.shields.io/badge/Parquet-000000?style=for-the-badge&logo=apache&logoColor=white)

## 📌 Visão Geral do Projeto
Este projeto é um pipeline de Engenharia de Dados de ponta a ponta focado em dados de Recursos Humanos (HR Analytics). O objetivo foi extrair dados brutos de planilhas .XLSX e .CSV, processá-los aplicando a **Arquitetura Medalhão (Medallion Architecture)** e a **Modelagem Dimensional (Star Schema)**, e finalmente disponibilizá-los para análises de negócios via SQL e dashboard no Power BI.

## 🏛️ Arquitetura de Dados

Desenhei o fluxo de dados para ser modular, escalável e performático, dividido nas seguintes camadas:

1. **Camada Raw:** Arquivos originais recebidos em formatos variados (`.xlsx` e `.csv`).
2. **Camada Bronze:** Ingestão bruta dos dados, convertendo-os para o formato colunar **Parquet** (sem aplicação de regras de negócio, apenas preservando o histórico).
3. **Camada Silver:** Limpeza, tipagem de dados, tratamento de nulos e modelagem em um **Star Schema** (separação em Tabelas Fato e Dimensão).
4. **Business Analytics (DuckDB):** Consultas SQL analíticas (OLAP) executadas diretamente nos arquivos Parquet da camada Silver para responder a perguntas de negócio.
5. **Data Visualization (Power BI):** Consumo do Star Schema para criação de dashboards interativos.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Manipulação e ETL:** Pandas, OpenPyXL
* **Armazenamento:** Apache Parquet (PyArrow)
* **Análise SQL (OLAP):** DuckDB
* **Visualização:** Microsoft Power BI
* **Orquestração:** Script Python Customizado (`orquestrador.py`)

## 📂 Estrutura do Repositório

```text
📦 hr-analytics-pipeline
 ┣ 📂 Data
 ┃ ┣ 📂 1 - Raw             # Arquivos originais (Ignorados no Git)
 ┃ ┣ 📂 2 - Bronze          # Arquivos Parquet brutos
 ┃ ┗ 📂 3 - Silver          # Star Schema (Fato e Dimensões em Parquet)
 ┣ 📂 Scripts
 ┃ ┣ 📜 ingestao_full.py       # Extração para camada Bronze
 ┃ ┣ 📜 silver_dim_*.py        # Transformações das Dimensões
 ┃ ┣ 📜 silver_fato_*.py       # Transformações das Fatos
 ┃ ┗ 📜 orquestrador.py        # Gatilho principal do pipeline
 ┣ 📂 Perguntas_de_negocio
 ┃ ┗ 📜 analise_duckdb.py      # Queries SQL respondendo perguntas de negócio
 ┣ 📜 dashboard_hr.pbix        # Arquivo do Power BI
 ┣ 📜 requirements.txt         # Dependências do projeto
 ┗ 📜 README.md
```
## 🚀 Como Executar o Projeto

1. **Clone o Repositório**

```text
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
cd NOME_DO_REPOSITORIO
```

