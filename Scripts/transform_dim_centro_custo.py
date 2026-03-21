# 1 - Bibliotecas

import pandas as pd
import openpyxl
import os

# 2 - Lendo arquivo dim_centro_custo.parquet

input_path = "../Data/2 - Bronze/dim_centro_custo.parquet"
output_path = "../Data/3 - Silver"


df = pd.read_parquet(input_path)

df

# 3 - Renomeando colunas

df = df.rename(columns={'Cód C.Custo': 'cod_centro_custo', 
                        'Centro Custo': 'centro_custo',
                      })

# 4 - Tipando as colunas do data frame

tipos = { 
    'cod_centro_custo': 'string',
    'centro_custo': 'string',

}

df = df.astype(tipos)

# 5 - Envindo dim_centro_custo para a camada silver

df.to_parquet(os.path.join(output_path, "dim_centro_custo.parquet"), index=False)


