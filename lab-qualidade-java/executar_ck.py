import os
import subprocess
import shutil

REPO_DIR = os.path.abspath("../repositorios")

OUT_DIR = "metricas"
CK_JAR = os.path.abspath("ck.jar")

os.makedirs(OUT_DIR, exist_ok=True)
repositorios = os.listdir(REPO_DIR)

for i, repo in enumerate(repositorios, start=1):
    repo_path = os.path.join(REPO_DIR, repo)
    class_saida = os.path.join(OUT_DIR, f"{repo}_class.csv")

    if not os.path.exists(repo_path) or not os.path.isdir(repo_path):
        print(f"[{i}] ❌ Repositório {repo} não encontrado. Pulando...")
        continue

    if os.path.exists(class_saida):
        print(f"[{i}] {repo}: Métricas já existem, pulando.")
        continue

    print(f"[{i}] Rodando CK para: {repo}")

    try:
        subprocess.run(
            ["java", "-jar", CK_JAR, repo_path, "true", "0"],
            check=True
        )

        # ✅ Move apenas o class.csv
        if os.path.exists("class.csv"):
            shutil.move("class.csv", class_saida)

    except subprocess.CalledProcessError:
        print(f"[{i}] ❌ Erro ao rodar CK em {repo}, pulando...")