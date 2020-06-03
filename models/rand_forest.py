import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score,recall_score,f1_score,accuracy_score

data = pd.read_csv('/home/fuhrer/Desktop/Placement-analysis/data/train.csv',header=None)
data = data.drop([0],axis=1)
_X_ = data.drop([13],axis=1)
_X_ = _X_.drop([14],axis=1)
_y_ = data[13]
X_train, X_test, y_train, y_test = train_test_split(_X_, _y_,test_size=0.23, random_state=39)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train,y_train)
y = model.predict(X_test)
print('accuracy:'+str(accuracy_score(y_test,y)))
print('precision:'+str(precision_score(y_test,y)))
print('recall:'+str(recall_score(y_test,y)))
print('f1 score:'+str(f1_score(y_test,y)))