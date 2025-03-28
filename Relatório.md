## Relatório Final
## 1. Introdução

No desenvolvimento de sistemas open-source, diversos desenvolvedores colaboram em um mesmo repositório, o que pode afetar a qualidade do código. Aspectos como modularidade, manutenibilidade e legibilidade são críticos para a evolução do software.

Este estudo busca analisar a qualidade de código de repositórios Java populares, correlacionando suas métricas de qualidade com atributos do processo de desenvolvimento. As principais questões de pesquisa incluem:

RQ 01: Qual a relação entre a popularidade dos repositórios e suas características de qualidade?

RQ 02: Qual a relação entre a maturidade dos repositórios e suas características de qualidade?

RQ 03: Qual a relação entre a atividade dos repositórios e suas características de qualidade?

RQ 04: Qual a relação entre o tamanho dos repositórios e suas características de qualidade?

## 2. Coleta de Dados

A coleta foi realizada utilizando a API do GitHub, buscando os repositórios mais populares em Java, ordenados pelo número de estrelas. Os seguintes atributos foram extraídos:

- Nome do repositório  
- URL  
- Estrelas  
- Data de criação  
- Última atualização  
- Tamanho do repositório (KB)  
- Forks  
- Issues abertas  
- Watchers  
- Commits  
- Releases

Em seguida, os repositórios foram clonados e analisados por meio da ferramenta **CK**, que extrai métricas de qualidade de software, como acoplamento, herança, coesão e linhas de código.

2.2. Análise de Qualidade

Clonamos os repositórios e executamos a ferramenta CK para coletar as métricas de qualidade:

CBO: Acoplamento entre objetos

DIT: Profundidade da árvore de herança

LCOM: Falta de coesão entre métodos

Os dados foram sumarizados por repositório utilizando medidas estatísticas (média, mediana e desvio padrão).

Testes de correlação (Pearson/Spearman) foram aplicados para analisar relações entre as métricas coletadas.

3. Resultados
