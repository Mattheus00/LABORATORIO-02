#!/bin/bash

mkdir repos && cd repos

while IFS=, read -r nome _; do
    [[ $nome == "Nome" ]] && continue
    echo "Clonando $nome..."
    git clone --depth=1 "https://github.com/$nome.git"
    pasta=$(basename "$nome")
    echo "Executando CK em $pasta..."
    java -jar ../ck-0.7.1-jar-with-dependencies.jar "$pasta" false 0 false ./results/
done < ./top_java_repos.csv

