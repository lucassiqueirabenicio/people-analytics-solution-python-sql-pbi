import duckdb
import os

# 1. Mapear o diretório atual
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

# 2. Mapeando as fatos e dimensões da camada silver
path_fato_contrato = os.path.join(DIRETORIO_ATUAL, "..", "Data", "3 - Silver", "fato_contrato.parquet").replace('\\', '/')
path_dim_funcionario = os.path.join(DIRETORIO_ATUAL, "..", "Data", "3 - Silver", "dim_funcionario.parquet").replace('\\', '/')


# Pergunta: Qual a média salarial por escolaridade?

query_teste = f""" 
    SELECT dfun.escolaridade AS 'Escolaridade', AVG(fcon.valor_salario) AS 'Total Salário'
    FROM '{path_fato_contrato}' fcon
    INNER JOIN '{path_dim_funcionario}' dfun ON dfun.cod_funcionario = fcon.cod_funcionario
    GROUP BY dfun.escolaridade ORDER BY AVG(fcon.valor_salario) ASC;
"""

resultado_dept = duckdb.query(query_teste).df()
print(resultado_dept)