import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.ensemble import HistGradientBoostingClassifier
import numpy as np

# from utils import DATA_PATH 
# apesar de estar chamando não está encontrando o arquivo, verficar dps

df = pd.read_csv(r"D:\mateu\Documents\machine-learning-project\data\Final_Augmented_dataset_Diseases_and_Symptoms.csv")
df.head().T

target_colunm = 'diseases'

X = df.drop(columns=[target_colunm])
y = df[target_colunm]

X = X.astype('int8')
#ta estourando meu pc pra rodar, vamos ver se vai agr


model = HistGradientBoostingClassifier(random_state= 42, early_stopping= False)
skf = StratifiedKFold(n_splits= 5, shuffle= True, random_state= 42)

results = cross_val_score(model, X, y, cv=skf, scoring= 'accuracy') 

print(f"\nResultados de 5 testes: {results}")
print(f"Acurácia: {np.mean(results)}")
