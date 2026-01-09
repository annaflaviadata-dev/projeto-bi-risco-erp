import sqlite3
import pandas as pd
import numpy as np
import os

# 1. LOCALIZAÇÃO DO BANCO (Caminho inteligente)
# O script está em /scripts, então subimos um nível (..) para achar a pasta /data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'data', 'bascomm_erp_simulado.db')

# 2. CONECTAR E EXTRAIR
conn = sqlite3.connect(DB_PATH)

query = """
SELECT 
    canal_marketing,
    COUNT(*) as total_vendas,
    SUM(CASE WHEN status = 'Atrasado' THEN valor_total ELSE 0 END) as valor_atraso,
    SUM(valor_total) as faturamento_total
FROM vendas_financeiro
GROUP BY canal_marketing
"""

df = pd.read_sql_query(query, conn)

# 3. INTELIGÊNCIA ESTATÍSTICA (Z-Score)
# Calculamos a taxa de inadimplência (quanto do faturamento está atrasado)
df['taxa_inadimplencia'] = df['valor_atraso'] / df['faturamento_total']

# Média e Desvio Padrão para o Z-Score
media = df['taxa_inadimplencia'].mean()
desvio_padrao = df['taxa_inadimplencia'].std()

# Cálculo do Z-Score: Identifica o que foge do normal
df['z_score'] = (df['taxa_inadimplencia'] - media) / desvio_padrao
df['prioridade'] = np.where(df['z_score'] > 1, '🚨 CRÍTICO', '✅ Normal')

# 4. EXIBIR NO TERMINAL
print("\n" + "="*60)
print("       RELATÓRIO ESTRATÉGICO DE RISCO - BASCOMM ERP")
print("="*60)
print(df[['canal_marketing', 'taxa_inadimplencia', 'z_score', 'prioridade']].sort_values(by='z_score', ascending=False))
print("="*60)

# 5. GERAR ARQUIVO PARA POWER BI
CSV_PATH = os.path.join(BASE_DIR, 'data', 'resultado_bi.csv')
df.to_csv(CSV_PATH, index=False, sep=';', decimal=',', encoding='utf-8-sig') # Alterei o ponto pela vírgula na exportação
print(f"✅ Dados prontos para o Power BI em: {CSV_PATH}\n")

conn.close()