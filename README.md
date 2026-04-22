# Machine Learning Project

Projeto final de Aprendizagem de Maquina organizado por fase do pipeline, nao por integrante.

## Estrutura

```text
machine-learning-project/
|- README.md
|- requirements.txt
|- .gitignore
|- data/
|  |- Final_Augmented_dataset_Diseases_and_Symptoms.csv
|  |- dataset_tratado.csv
|  |- dataset_3_doencas.csv
|  \- figs/
|- notebooks/
|  |- 01_preparacao_dados.ipynb
|  |- 02_experimentos_modelagem.ipynb
|  \- final_projeto.ipynb
|- src/
|  \- utils.py
|- models/
|  |- best_model.joblib
|  \- metadata.json
\- specs/
   \- SPEC.md
```

## Arquitetura de trabalho

O projeto passa a seguir um fluxo unico e compartilhado:

1. `notebooks/01_preparacao_dados.ipynb`
   - carrega o dataset bruto
   - faz inspecao inicial e limpeza
   - gera `data/dataset_tratado.csv`
   - filtra as 3 doencas alvo e gera `data/dataset_3_doencas.csv`
2. `notebooks/02_experimentos_modelagem.ipynb`
   - faz split estratificado
   - executa feature selection ou PCA
   - treina e compara pelo menos 2 modelos
   - salva o modelo vencedor em `models/`
3. `notebooks/final_projeto.ipynb`
   - consolida resultados
   - organiza o artigo em formato Jupyter
   - centraliza tabelas, graficos e conclusoes

Nao existe mais notebook por integrante. Se mais de uma pessoa trabalhar em paralelo, a separacao deve ser por secao, branch ou bloco funcional, nunca por arquivo pessoal.

## Como baixar o dataset

1. Acesse o dataset no Kaggle:
   `https://www.kaggle.com/datasets/dhivyeshrk/diseases-and-symptoms-dataset/data`
2. Baixe o arquivo CSV.
3. Renomeie, se necessario, para `Final_Augmented_dataset_Diseases_and_Symptoms.csv`.
4. Coloque o arquivo dentro de `data/`.

Caminho esperado:

```text
data/Final_Augmented_dataset_Diseases_and_Symptoms.csv
```

## Como usar o projeto

1. Crie e ative um ambiente virtual.
2. Instale as dependencias:

```bash
pip install -r requirements.txt
```

3. Escolha as 3 classes alvo.
4. Atualize `CLASSES_ALVO` em `src/utils.py`.
5. Execute `notebooks/01_preparacao_dados.ipynb`.
6. Execute `notebooks/02_experimentos_modelagem.ipynb`.
7. Consolide a entrega em `notebooks/final_projeto.ipynb`.

## Regras de organizacao

- `specs/SPEC.md` e a fonte de verdade da arquitetura.
- Codigo reutilizavel vai para `src/utils.py`.
- `random_state=42` deve ser mantido em todo o pipeline.
- Dataset e artefatos grandes nao entram no Git.
- O notebook final so deve consumir resultados ja produzidos nas fases anteriores.
