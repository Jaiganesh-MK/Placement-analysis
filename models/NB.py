import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('/home/mk/Desktop/placement/data/train.csv',header=None)
data = data.drop([0],axis=1)
_X_ = data.drop([13],axis=1)
_X_ = _X_.drop([14],axis=1)
_y_ = data[13]
X_train, X_test, y_train, y_test = train_test_split(_X_, _y_,test_size=0.23, random_state=30)
model = LogisticRegression()
model.fit(X_train,y_train)
score = model.score(X_test, y_test)
print(score)