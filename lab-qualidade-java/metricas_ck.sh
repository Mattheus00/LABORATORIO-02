#!/bin/bash

mkdir -p repositorios metricas

while IFS=',' read -r name stars created_at releases_url; do
    if [[ "$name" == "name" ]]; then
        continue
    fi

    echo "Clonando $name"
    repo_name=$(echo $name | cut -d'/' -f2)
    git clone https://github.com/$name.git repositorios/$repo_name

    echo "Executando CK para $repo_name"
    java -jar ck.jar repositorios/$repo_name true 0 metricas/$repo_name.csv
done < repositorios_java.csv
