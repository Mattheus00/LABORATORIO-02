import requests 
import csv

# Configuração
GITHUB_TOKEN = "GITHUB_TOKE"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}
QUERY = "language:Java stars:>1000"
PER_PAGE = 100

def get_repositories():
    repos = []
    for page in range(1, 11):
        url = f"https://api.github.com/search/repositories?q={QUERY}&sort=stars&order=desc&per_page={PER_PAGE}&page={page}"
        response = requests.get(url, headers=HEADERS)
        data = response.json()
        for repo in data.get("items", []):
            repos.append([repo["full_name"], repo["stargazers_count"], repo["created_at"], repo["pushed_at"], repo["size"]])
        print(f"Página {page} coletada!")
    return repos

def save_to_csv(repos):
    with open("top_java_repos.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Estrelas", "Criado Em", "Última Atualização", "Tamanho (KB)"])
        writer.writerows(repos)

if __name__ == "__main__":
    repos = get_repositories()
    save_to_csv(repos)
    print("Repositórios salvos em 'top_java_repos.csv'")
