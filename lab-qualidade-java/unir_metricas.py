import pandas as pd
import os

CAMINHO_METRICAS = "metricas"
arquivos = [f for f in os.listdir(CAMINHO_METRICAS) if f.endswith("_class.csv")]

dataframes = []

for arquivo in arquivos:
    repo_nome = arquivo.replace("_class.csv", "")
    try:
        df = pd.read_csv(os.path.join(CAMINHO_METRICAS, arquivo), encoding="latin1")  # 🔥 aqui!
        df["repositorio"] = repo_nome
        dataframes.append(df)
    except Exception as e:
        print(f"❌ Erro ao ler {arquivo}: {e}")

df_unificado = pd.concat(dataframes, ignore_index=True)
df_unificado.to_csv("metricas_unificadas.csv", index=False)

print("✅ Arquivo 'metricas_unificadas.csv' gerado com sucesso!")
