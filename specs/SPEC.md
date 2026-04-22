# Spec-Driven Development - Projeto Final de Aprendizagem de Maquina (2026.1)

> Documento de referencia do projeto, derivado de
> [Projeto - Aprendizagem de maquina 2026.1.md](../Projeto%20-%20Aprendizagem%20de%20m%C3%A1quina%202026.1.md).
> Esta especificacao define o que precisa ser entregue, como a solucao se organiza
> e qual fluxo deve ser seguido no repositorio.

---

## 1. Visao Geral

### 1.1. Problema

Dado um conjunto de sintomas de um paciente, prever qual, dentre 3 doencas
previamente escolhidas pela equipe, e o diagnostico mais provavel.

### 1.2. Tipo de problema

Classificacao multiclasse com 3 classes mutuamente exclusivas.

### 1.3. Dataset

- Fonte: Kaggle - [dhivyeshrk/diseases-and-symptoms-dataset](https://www.kaggle.com/datasets/dhivyeshrk/diseases-and-symptoms-dataset)
- Arquivo bruto: [data/Final_Augmented_dataset_Diseases_and_Symptoms.csv](../data/Final_Augmented_dataset_Diseases_and_Symptoms.csv)
- Formato: 378 colunas (1 coluna `diseases` + 377 sintomas binarios 0/1), 773 doencas distintas
- Arquivo tratado: [data/dataset_tratado.csv](../data/dataset_tratado.csv)

### 1.4. Entregaveis obrigatorios

1. Modelo de classificacao treinado e avaliado.
2. Matriz de confusao e metricas complementares.
3. Etapa obrigatoria de Feature Selection ou Reducao de Dimensionalidade.
4. Artigo cientifico em Jupyter no formato pedido pela disciplina.
5. Apresentacao com os resultados.
6. Codigo organizado, nomeado e documentado.

### 1.5. Restricoes

- Ferramentas: Python + Jupyter + scikit-learn + pandas + numpy + matplotlib + seaborn.
- Equipe de no maximo 3 pessoas.
- O dataset nao deve ser commitado no repositorio.

---

## 2. Decisao Arquitetural

### 2.1. Regra principal

O projeto nao deve mais ser estruturado por integrante. Nao ha notebooks individuais.

### 2.2. Arquitetura adotada

A organizacao passa a ser por etapa do pipeline:

1. Preparacao dos dados.
2. Experimentos de modelagem.
3. Consolidacao do artigo final.

### 2.3. Consequencias praticas

- Cada notebook tem uma responsabilidade unica e clara.
- Todo codigo que se repete em 2 ou mais notebooks sobe para `src/utils.py`.
- O trabalho em paralelo acontece por branch, secao ou modulo, nao por notebook pessoal.
- O notebook final deixa de ser um lugar de experimentacao e passa a ser apenas consolidacao.

---

## 3. Estrutura Alvo do Repositorio

```text
data/
|- Final_Augmented_dataset_Diseases_and_Symptoms.csv   # bruto, fora do git
|- dataset_tratado.csv                                 # limpo, fora do git
|- dataset_3_doencas.csv                               # filtrado para as classes alvo
\- figs/                                               # figuras auxiliares

src/
\- utils.py                                            # funcoes compartilhadas
   |- load_data()
   |- load_clean_data()
   |- filter_diseases()
   |- save_dataset()
   |- split_data()
   |- evaluate_model()
   \- plot_confusion_matrix()

models/
|- best_model.joblib                                   # modelo final
\- metadata.json                                       # classes, features, metricas

notebooks/
|- 01_preparacao_dados.ipynb                           # EDA, limpeza e geracao dos datasets
|- 02_experimentos_modelagem.ipynb                     # split, selecao de features, modelos
\- final_projeto.ipynb                                 # artigo cientifico e resultados finais
```

Fluxo de dados:

```text
CSV bruto
  -> 01_preparacao_dados.ipynb
  -> dataset_tratado.csv
  -> dataset_3_doencas.csv
  -> 02_experimentos_modelagem.ipynb
  -> models/best_model.joblib + metadata.json
  -> final_projeto.ipynb
  -> apresentacao
```

---

## 4. Responsabilidade de Cada Notebook

### 4.1. `01_preparacao_dados.ipynb`

Objetivo:

- carregar o dataset bruto
- fazer EDA inicial
- aplicar limpeza e downcast
- remover sintomas raros ou quase constantes
- apoiar a escolha das 3 doencas alvo
- gerar `dataset_tratado.csv`
- gerar `dataset_3_doencas.csv`

Saidas esperadas:

- estatisticas descritivas
- graficos exploratorios
- CSV tratado
- CSV filtrado para as 3 classes

### 4.2. `02_experimentos_modelagem.ipynb`

Objetivo:

- carregar `dataset_3_doencas.csv`
- executar split treino/validacao/teste estratificado
- rodar baseline sem selecao de features
- comparar feature selection e PCA
- treinar pelo menos 2 modelos candidatos
- comparar metricas
- salvar o melhor modelo em `models/`

Saidas esperadas:

- baseline documentado
- comparacao entre selecao de features e PCA
- comparacao entre modelos
- metricas de validacao e teste
- modelo final persistido

### 4.3. `final_projeto.ipynb`

Objetivo:

- consolidar o artigo cientifico
- reapresentar metodologia e resultados
- incluir graficos, tabelas e interpretacao
- registrar limitacoes, conclusoes e trabalhos futuros

Saidas esperadas:

- notebook final executavel de ponta a ponta
- artigo pronto para exportacao

---

## 5. Estado Atual vs. Requisitos

Legenda: `OK` pronto, `PARCIAL` iniciado, `PENDENTE` ainda nao atendido.

| # | Requisito | Status | Evidencia / Gap |
|---|-----------|--------|-----------------|
| R1 | Estrutura do repositorio | OK | Pastas principais existem |
| R2 | Dependencias declaradas | OK | `requirements.txt` cobre o basico |
| R3 | Dataset bruto esperado em `data/` | OK | Caminho definido e documentado |
| R4 | EDA inicial | OK | `notebooks/01_preparacao_dados.ipynb` |
| R5 | Otimizacao de memoria | OK | Notebook 01 |
| R6 | Remocao de sintomas raros/constantes | OK | Notebook 01 |
| R7 | Analise de correlacao | OK | Notebook 01 |
| R8 | Escolha das 3 doencas alvo | OK | `pneumonia`, `gout`, `anxiety` em `src/utils.py` |
| R9 | Dataset filtrado para 3 doencas | OK | `data/dataset_3_doencas.csv` gerado |
| R10 | Split treino/validacao/teste estratificado | OK | Notebook 02, via `split_data` |
| R11 | Feature Selection / Reducao de Dimensionalidade | OK | `SelectKBest(chi2)` com K=25, comparado com PCA |
| R12 | Treinamento de pelo menos 2 modelos | OK | Regressao Logistica + Random Forest |
| R13 | Comparacao entre modelos | OK | Notebook 02 secao 7 |
| R14 | Matriz de confusao | OK | Notebook 02 secao 8.1 e notebook final |
| R15 | Metricas adicionais | OK | ROC-AUC, PR, log-loss |
| R16 | Persistencia do modelo final em `models/` | OK | `best_model.joblib`, `feature_selector.joblib`, `metadata.json` |
| R17 | `src/utils.py` com helpers compartilhados | OK | Implementado |
| R18 | Notebook 01 de preparacao dos dados | OK | Existe e reaproveita o trabalho util ja feito |
| R19 | Notebook 02 de experimentos e modelagem | OK | Baseline, FS, PCA, 2 modelos, avaliacao |
| R20 | Notebook final consolidado | OK | Artigo completo em `notebooks/final_projeto.ipynb` |
| R21 | Artigo cientifico | OK | Todas as secoes obrigatorias preenchidas |
| R22 | Apresentacao | PENDENTE | Fora do escopo do repositorio |

---

## 6. Especificacao por Fase

### Fase 0 - Alinhamento

**F0.1. Escolher as 3 doencas alvo**

- Entrada: `data/dataset_tratado.csv` e as analises do notebook 01.
- Saida: lista com 3 strings documentada em `README.md`, `SPEC.md` e `src/utils.py`.
- Criterio de aceite:
  - cada classe com volume suficiente para split estratificado
  - classes com justificativa no artigo

### Fase 1 - Preparacao dos dados

**F1.1. Limpeza e padronizacao**

- Entrada: dataset bruto.
- Saida: `dataset_tratado.csv`.
- Criterio de aceite:
  - sem nulos inesperados
  - sem duplicatas
  - tipos otimizados

**F1.2. Filtragem das classes alvo**

- Entrada: `dataset_tratado.csv` + lista de classes.
- Saida: `dataset_3_doencas.csv`.
- Criterio de aceite:
  - somente as 3 classes alvo
  - colunas 100% zeradas removidas depois do filtro

### Fase 2 - Feature Selection / Reducao de Dimensionalidade

**F2.1. Baseline sem selecao**

- Modelo simples com todas as features para registrar a referencia inicial.

**F2.2. Feature Selection**

- Ferramentas sugeridas: `VarianceThreshold`, `SelectKBest(chi2)` e `mutual_info_classif`.
- Criterio de aceite:
  - reducao relevante de dimensionalidade
  - comparacao explicita entre antes e depois

**F2.3. PCA**

- Executar como alternativa de comparacao.
- Escolher a abordagem final por desempenho e interpretabilidade.

### Fase 3 - Modelagem

**F3.1. Modelo A - baseline interpretavel**

- Sugestao: Regressao Logistica ou Arvore de Decisao.
- Deve usar validacao cruzada e ajuste de hiperparametros.

**F3.2. Modelo B - modelo mais forte**

- Sugestao: Random Forest, Gradient Boosting ou MLPClassifier.
- Mesmo protocolo de avaliacao do Modelo A.

**F3.3. Selecao do modelo final**

- Criterio principal: `f1_macro` na validacao.
- Desempates: interpretabilidade, estabilidade e custo de inferencia.

### Fase 4 - Avaliacao

**F4.1. Avaliacao final no conjunto de teste**

Metricas obrigatorias:

- matriz de confusao
- accuracy
- precision, recall e F1 por classe
- F1-macro

Metricas recomendadas:

- ROC-AUC one-vs-rest
- curva precision-recall
- log-loss

**F4.2. Analise de erros**

- Identificar padroes de confusao entre classes.
- Explicar os erros mais relevantes no artigo.

### Fase 5 - Artigo Cientifico

Estrutura minima:

- titulo, autores e afiliacao
- resumo e abstract
- introducao
- trabalhos relacionados
- metodologia
- resultados
- discussao
- conclusao
- referencias

Checklist:

- sem secoes vazias
- sem erros claros de portugues
- todos os graficos com titulo, eixo e legenda
- todas as tabelas legiveis

### Fase 6 - Apresentacao

- 8 a 12 slides
- problema, dados, metodo, resultados, conclusoes
- cada integrante apresenta uma parte

---

## 7. Regras de Codigo e Boas Praticas

- Reprodutibilidade: usar `random_state=42`.
- Nomenclatura: snake_case no codigo.
- Reuso: tudo que aparece em 2 ou mais notebooks vai para `src/utils.py`.
- Notebooks: secoes numeradas, imports no topo e sem celulas mortas.
- Git: nao versionar dataset, checkpoints e modelos pesados.
- Colaboracao: trabalho concorrente por branch ou secao funcional, nao por notebook pessoal.

---

## 8. Definition of Done

O projeto esta pronto quando:

1. `data/dataset_3_doencas.csv` existir e for gerado por funcao versionada.
2. Houver pelo menos 2 modelos treinados e comparados.
3. `models/best_model.joblib` e `models/metadata.json` existirem.
4. A matriz de confusao e as metricas aparecerem em `notebooks/final_projeto.ipynb`.
5. Feature selection ou reducao de dimensionalidade estiver documentada.
6. O notebook final executar sem erro em uma maquina limpa.
7. O artigo cobrir todas as secoes obrigatorias.
8. O README estiver alinhado com a arquitetura real do repositorio.

---

## 9. Proximos Passos Imediatos

1. Preparar a apresentacao (8 a 12 slides) cobrindo problema, dados, metodo, resultados e conclusoes (artefato externo ao repositorio).
