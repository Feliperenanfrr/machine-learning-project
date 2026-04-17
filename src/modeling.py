import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from scipy import csr_matrix # tentando utilizar o Matrix para rodar o sv
import numpy as ny

# from utils import DATA_PATH 
# apesar de estar chamando não está encontrando o arquivo, verficar dps

df = pd.read_csv(r"D:\mateu\Documents\machine-learning-project\data\Final_Augmented_dataset_Diseases_and_Symptoms.csv")

target_colunm = 'diseases'

X = df.drop(columns=[target_colunm])
y = df[target_colunm]

# convertendo para matrix pra ver se da certo
print("comprimindo para Matrix")
X_sparse = csr_matrix(X.values)

model = RandomForestClassifier(n_estimators= 50, max_depth= 20, random_state= 42, n_jobs= 2)
skf = StratifiedKFold(n_splits= 5, shuffle= True, random_state= 42)

results = cross_val_score(model, X_sparse, y, cv=skf, scoring= 'accuracy') 

print(f"\nResultados de 5 testes: {results}")
print(f"Acurácia: {np.mean(results)}")
