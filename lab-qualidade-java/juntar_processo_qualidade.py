import pandas as pd
from datetime import datetime

df_qualidade = pd.read_csv("metricas_unificadas.csv")
df_processo = pd.read_csv("repositorios_java.csv")

# Extrai nome curto do repositório (última parte do 'owner/name')
df_processo["repositorio"] = df_processo["name"].apply(lambda x: x.split("/")[-1])

# Converte data para calcular idade (maturidade)
df_processo["created_at"] = pd.to_datetime(df_processo["created_at"])
df_processo["maturidade_anos"] = datetime.now().year - df_processo["created_at"].dt.year

# Junta os dois DataFrames
df_merged = pd.merge(df_qualidade, df_processo, on="repositorio", how="inner")

# Salva o resultado
df_merged.to_csv("analise_completa.csv", index=False)
print("✅ Arquivo 'analise_completa.csv' gerado com sucesso!")
