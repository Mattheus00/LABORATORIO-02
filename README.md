# LABORATORIO-02
Relatório Final - Análise de Repositórios Java

Introdução

O objetivo deste trabalho é analisar a qualidade de 1.000 repositórios Java populares no GitHub, utilizando métricas de qualidade calculadas pela ferramenta CK. A análise busca correlacionar popularidade, maturidade, atividade e tamanho dos repositórios com características de qualidade como CBO, DIT e LCOM.

Metodologia

Coleta de Dados: Os repositórios foram coletados usando a API do GitHub.

Métricas de Processo: Popularidade (número de estrelas), Tamanho (LOC e linhas de comentários), Atividade (número de releases) e Maturidade (idade do repositório).

Métricas de Qualidade: CBO (Coupling Between Objects), DIT (Depth of Inheritance Tree) e LCOM (Lack of Cohesion of Methods).

Ferramentas Utilizadas: CK (versão 0.7.0), Python (pandas, matplotlib, seaborn).

Hipóteses

Repositórios mais populares têm menor acoplamento (CBO).

Repositórios mais antigos apresentam maior profundidade de herança (DIT).

Repositórios mais ativos possuem maior coesão de métodos (LCOM).

Repositórios maiores possuem maior acoplamento (CBO).

Coleta e Análise de Dados

Os dados foram coletados usando scripts Python e armazenados em arquivos CSV.