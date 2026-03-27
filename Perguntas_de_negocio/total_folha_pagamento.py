import duckdb
import os

# 1. Mapear o diretório atual
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

# 2. Mapeando as fatos e dimensões da camada silver
path_fato_ficha_financeira = os.path.join(DIRETORIO_ATUAL, "..", "Data", "3 - Silver", "fato_ficha_financeira.parquet").replace('\\', '/')


# Pergunta: Qual o valor total de proventos da folha de pagamento por mês?

query_teste = f""" 
    SELECT mes_pagamento AS 'Mês Pagamento', SUM(valor) AS 'Movimentação'
    FROM '{path_fato_ficha_financeira}' WHERE tipo = 'PROVENTO'
    GROUP BY mes_pagamento
"""


resultado_dept = duckdb.query(query_teste).df()
print(resultado_dept)