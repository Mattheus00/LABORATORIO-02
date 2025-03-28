## Relatório Final
## 1. Introdução

No desenvolvimento de sistemas open-source, diversos desenvolvedores colaboram em um mesmo repositório, o que pode afetar a qualidade do código. Aspectos como modularidade, manutenibilidade e legibilidade são críticos para a evolução do software.

Este estudo busca analisar a qualidade de código de repositórios Java populares, correlacionando suas métricas de qualidade com atributos do processo de desenvolvimento. As principais questões de pesquisa incluem:

RQ 01: Qual a relação entre a popularidade dos repositórios e suas características de qualidade?

RQ 02: Qual a relação entre a maturidade dos repositórios e suas características de qualidade?

RQ 03: Qual a relação entre a atividade dos repositórios e suas características de qualidade?

RQ 04: Qual a relação entre o tamanho dos repositórios e suas características de qualidade?

## 2. Coleta de Dados

Utilizamos a API REST do GitHub para obter os 1.000 repositórios Java mais populares.

As seguintes informações foram extraídas e armazenadas em um arquivo CSV:

Nome do repositório

URL

Número de estrelas (popularidade)

Número de releases (atividade)

Data de criação (maturidade)

2.2. Análise de Qualidade

Clonamos os repositórios e executamos a ferramenta CK para coletar as métricas de qualidade:

CBO: Acoplamento entre objetos

DIT: Profundidade da árvore de herança

LCOM: Falta de coesão entre métodos

Os dados foram sumarizados por repositório utilizando medidas estatísticas (média, mediana e desvio padrão).

Testes de correlação (Pearson/Spearman) foram aplicados para analisar relações entre as métricas coletadas.

3. Resultados
