import time

# --- 1. IMPORTANDO OS SCRIPTS ---
# O Python vai procurar esses arquivos .py na mesma pasta onde o orquestrador está
import ingestao_full
import transform_dim_funcionario
import transform_dim_cargo
import transform_dim_centro_custo
import transform_dim_escala
import transform_dim_situacao
import transform_dim_tipo_contrato
import transform_fato_contrato
import transform_fato_ficha_financeira


def rodar_pipeline():
    print("="*60)
    print("INICIANDO PIPELINE DE DADOS - RH")
    print("="*60)
    
    # Marcamos o tempo de início para saber quanto tempo o processo demorou
    inicio_pipeline = time.time()

    try:
        # --- FASE 1: INGESTÃO (RAW -> BRONZE) ---
        print("\n[FASE 1/3] Extraindo dados para a camada Bronze...")
        
        # Aqui você coloca o nome da função que criou dentro do ingestao_full.py
        ingestao_full.executar_ingestao_full() 
        

        # --- FASE 2: DIMENSÕES (BRONZE -> SILVER) ---
        print("\n[FASE 2/3] Processando Dimensões (Camada Silver)...")
        transform_dim_funcionario.executar_transform_dim_funcionario
        transform_dim_cargo.executar_transform_dim_cargo
        transform_dim_centro_custo.executar_transform_centro_custo   
        transform_dim_escala.executar_transform_dim_escala
        transform_dim_situacao.executar_transform_dim_situacao
        transform_dim_tipo_contrato.executar_transform_dim_tipo_contrato
        

        # --- FASE 3: FATOS (BRONZE -> SILVER) ---
        # As fatos sempre rodam por último, pois elas dependem das chaves das dimensões!
        print("\n[FASE 3/3] Processando Fatos (Camada Silver)...")
        transform_fato_contrato.executar_transform_fato_contrato
        transform_fato_ficha_financeira.executar_transform_fato_ficha_financeira
        
        
        # --- SUCESSO ---
        fim_pipeline = time.time()
        tempo_total = round(fim_pipeline - inicio_pipeline, 2)
        
        print("\n" + "="*60)
        print(f"PIPELINE CONCLUÍDO COM SUCESSO! Tempo total: {tempo_total} segundos")
        print("="*60)

    except Exception as e:
        # --- TRATAMENTO DE ERRO ---
        # Se qualquer script quebrar, o código cai aqui e te avisa o motivo
        print("\n" + "="*60)
        print(f"ERRO CRÍTICO NO PIPELINE: {e}")
        print("="*60)

if __name__ == "__main__":
    rodar_pipeline()