import torch
import torch.nn as nn
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import torch.nn.functional as F
torch.manual_seed(14)
# hyper parameters

input_size = 12
num_classes = 1
num_epochs = 10000
batch_size = 10
learning_rate = 0.01

# loading data

data = pd.read_csv('train.csv',header=None)
_y_ = data[13]
data = data.drop([0],axis=1)
_X_ = data.drop([13],axis=1)
_X_ = _X_.drop([14],axis=1)

X_train, X_test, y_train, y_test = train_test_split(_X_, _y_,test_size=0.23, random_state=30)

X_train = torch.tensor(X_train.values.astype(np.int))
X_test = torch.tensor(X_test.values.astype(np.int))
y_train = torch.tensor(y_train.values.astype(np.int).reshape(-1,1))
y_test = torch.tensor(y_test.values.astype(np.int).reshape(-1,1))

# logistic regression class

class LogisticRegression(torch.nn.Module):
    
    def __init__(self,input_size, num_classes):
        super(LogisticRegression,self).__init__()
        self.linear = torch.nn.Linear(input_size,1)

    def forward(self,x):
        y_pred = torch.sigmoid(self.linear(x.float()))
        return y_pred

model = LogisticRegression(input_size, num_classes)

# loss function and optimizer

criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr= learning_rate)

for epochs in range(num_epochs):
       
    y_pred = model(X_train)
    optimizer.zero_grad()
    loss = criterion(y_pred,y_train.float())
    loss.backward()
    optimizer.step()
    print(loss.data)
    
for parameter in model.parameters():
    print(parameter)

#prediction

y_pred = model.forward(X_test)
for i in range(0,X_test.shape[0]):
    if(y_pred[i]>0.5 or y_pred[i]==0.5):
        y_pred[i] = 1
    else:
        y_pred[i] = 0

count = 0
for i in range(0,X_test.shape[0]):
    if(y_pred[i]==y_test[i]):
        count = count + 1

print(count/X_test.shape[0])