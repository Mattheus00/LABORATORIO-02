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

## 3. Hipóteses
H1: Repositórios com maior atividade (mais releases) tendem a apresentar melhor qualidade de código, pois passam por mais ciclos de manutenção e revisão.

H2: Repositórios maiores (com mais linhas de código) podem apresentar menor coesão entre métodos (LCOM mais alto), devido ao aumento da complexidade do sistema.

H3: Repositórios mais maduros (com mais anos desde a criação) possuem maior acoplamento entre classes (CBO mais alto), devido à evolução do código ao longo do tempo.

H4: Repositórios com maior popularidade (mais estrelas) tendem a ter um DIT (profundidade da hierarquia de herança) maior, pois frequentemente seguem padrões arquiteturais mais sofisticados.

H5: Repositórios ativos (com mais releases) possuem menos issues abertas, pois há uma manutenção mais constante por parte dos desenvolvedores.

H6: Projetos menores (em LOC) apresentam métricas de qualidade mais equilibradas (baixo CBO, DIT e LCOM), pois são mais fáceis de manter e modularizar.


## 4. Resultados
