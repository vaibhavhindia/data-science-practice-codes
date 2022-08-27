import pandas as pd 
from sklearn.linear_model import LogisticRegression
from pickle import dump

claimants = pd.read_csv('claimants.csv')
claimants.drop(['CASENUM'], inplace=True, axis=1)
claimants = claimants.dropna()

X = claimants.iloc[:,[1,2,3,4,5]]
Y = claimants.iloc[:,0]

model = LogisticRegression(max_iter=300)
model.fit(X,Y)

dump(model, open('logistic_model.sav','wb'))

