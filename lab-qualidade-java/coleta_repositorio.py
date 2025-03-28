import requests
import csv
import time

TOKEN = "" 

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {TOKEN}"
}

repos = []

for page in range(1, 11):  # 10 páginas = 1000 repositórios
    print(f"Coletando página {page}...")
    url = f"https://api.github.com/search/repositories?q=language:Java&sort=stars&order=desc&per_page=100&page={page}"
    response = requests.get(url, headers=headers)
    data = response.json()
    
    for item in data.get("items", []):
        repos.append({
            "name": item["full_name"],
            "stars": item["stargazers_count"],
            "created_at": item["created_at"],
            "releases_url": item["releases_url"].replace("{/id}", "")
        })
    
    time.sleep(1)  # Evita limite de rate

with open("repositorios_java.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "stars", "created_at", "releases_url"])
    writer.writeheader()
    writer.writerows(repos)

print("Repositorios salvos em repositorios_java.csv")
