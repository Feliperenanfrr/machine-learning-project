# Machine Learning Project

Projeto simples de faculdade para trabalhar em grupo com o menor atrito possivel.

## Estrutura

```text
machine-learning-project/
|- README.md
|- requirements.txt
|- .gitignore
|- data/
|- notebooks/
|  |- final_projeto.ipynb
|  \- individuais/
|     |- felipe_notebook.ipynb
|     |- tiago_notebook.ipynb
|     \- mateus_notebook.ipynb
|- src/
|  \- utils.py
\- models/
```

## Como baixar o dataset

1. Acesse o dataset no Kaggle:
   https://www.kaggle.com/datasets/dhivyeshrk/diseases-and-symptoms-dataset/data
2. Baixe o arquivo do dataset.
3. Extraia o CSV e renomeie, se necessario, para:
   `Final_Augmented_dataset_Diseases_and_Symptoms.csv`
4. Coloque o arquivo dentro da pasta `data/`.

O caminho final do arquivo deve ficar assim:

```text
data/Final_Augmented_dataset_Diseases_and_Symptoms.csv
```

## Como usar o projeto

1. Crie e ative um ambiente virtual.
2. Instale as dependencias com:

```bash
pip install -r requirements.txt
```

3. Use os notebooks individuais para testes e exploracao.
4. Use `notebooks/final_projeto.ipynb` para consolidar a versao final do trabalho.
5. Coloque funcoes reutilizaveis em `src/utils.py`.

## Organizacao do grupo

- Cada pessoa trabalha no proprio notebook individual.
- Evitem editar o mesmo notebook ao mesmo tempo.
- O dataset nao deve ser enviado para o GitHub.
- O notebook final deve ser atualizado apenas quando os testes individuais estiverem prontos.
