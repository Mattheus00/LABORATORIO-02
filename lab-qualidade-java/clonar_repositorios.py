import csv
import os
import subprocess

REPO_DIR = "repositorios"
os.makedirs(REPO_DIR, exist_ok=True)

with open("repositorios_java.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    total = sum(1 for _ in open("repositorios_java.csv")) - 1
    csvfile.seek(0)
    next(reader)

    for i, row in enumerate(reader, start=1):
        full_name = row["name"]
        owner, repo = full_name.split("/")
        local_path = os.path.join(REPO_DIR, repo)

        if os.path.exists(local_path):
            print(f"[{i}/{total}] {repo} já foi clonado. Pulando...")
            continue

        # Opcional: ignorar repositórios gigantes
        if int(row["stars"]) > 120000:
            print(f"[{i}/{total}] {repo} ignorado (repositório muito grande)")
            continue

        print(f"[{i}/{total}] Clonando {repo} de {full_name}...")
        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", f"https://github.com/{full_name}.git", local_path],
                check=True
            )
        except subprocess.CalledProcessError:
            print(f"❌ Erro ao clonar {full_name}. Pulando...")
            with open("clonagem_erros.log", "a", encoding="utf-8") as log:
                log.write(f"{full_name}\n")
