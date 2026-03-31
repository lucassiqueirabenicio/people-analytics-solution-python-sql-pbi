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
* **Orquestração:** Script Python Customizado (`main.py`)

## 📂 Estrutura do Repositório

```text
📦 hr-analytics-pipeline
 ┣ 📂 Dashboard            # Arquivo do Power BI e os assets usados no dashboard
 ┃  ┗ 📜 people_analytics.pbix
 ┣ 📂 Data
 ┃ ┣ 📂 1 - Raw             # Arquivos originais
 ┃ ┣ 📂 2 - Bronze          # Arquivos Parquet brutos
 ┃ ┗ 📂 3 - Silver          # Star Schema (Fato e Dimensões tratadas em Parquet)
 ┣ 📂 Scripts
 ┃ ┣ 📜 ingestao_full.py          # Extração da camada RAW para camada Bronze
 ┃ ┣ 📜 transform_dim_*.py        # Transformações das Dimensões
 ┃ ┣ 📜 transform_fato_*.py       # Transformações das Fatos
 ┃ ┗ 📜 main.py                   # Gatilho principal do pipeline (Orquestrador)
 ┣ 📂 Perguntas_de_negocio
 ┣ ┣ 📜 media_por_escolaridade.py      # Queries SQL respondendo perguntas de negócio 
 ┃ ┗ 📜 total_folha_pagamento.py      
 ┣ 📜 requirements.txt            # Dependências do projeto

```
## 🚀 Como Executar o Projeto

1. **Clone o Repositório**

```text
git clone [https://github.com/SEU_USUARIOpeople-analytics-solution-python-sql-pbi.git](https://github.com/SEU_USUARIO/people-analytics-solution-python-sql-pbi.git)
```
2. **Instale as Dependências do Projeto**

```text
pip install -r requirements.txt
```
3. **Execute o Orquestrador**

```text
cd Scripts
python main.py
```

4. **Execute as Análises de Negócio (SQL)**

```text
cd ../Perguntas_de_negocio
python media_por_escolaridade.py
```

## 📈 Dashboard no Power BI


<img width="1605" height="862" alt="image" src="https://github.com/user-attachments/assets/a53403de-4461-4f82-82a2-105070a41eee" />

[Link para o dashboard](https://app.powerbi.com/view?r=eyJrIjoiZGM2NGE5ZDAtMTkxNS00NzQ0LTk3YmEtM2YxNWZmMzJhNGEwIiwidCI6IjkxMTMxOGI2LTMwYjAtNDY5ZS1iMGE0LTk1OTU0ZjM5MjczMyJ9)

## 💡 Principais Aprendizados

* Vantagens de performance e tipagem do formato **Parquet** em relação ao CSV.
* Aprofundar minhas habilidades de manipulação de dados com Pandas.
* Poder analítico do **DuckDB** para consultar arquivos físicos localmente utilizando SQL puro sem a necessidade de instanciar um servidor de banco de dados.
* Fortalecimento do meu conhecimento em Storytelling e Visualização de Dados.



