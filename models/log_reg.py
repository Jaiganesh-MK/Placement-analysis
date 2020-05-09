import torch
import torch.nn as nn
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import torch.nn.functional as F
from torch.utils.data import DataLoader,Dataset
from sklearn.metrics import precision_score,recall_score,f1_score,accuracy_score
torch.manual_seed(14)

# hyper parameters

input_size = 12
num_classes = 1
num_epochs = 600
batch_size = 1
learning_rate = 0.00002

# loading data

data = pd.read_csv('/home/mk/Desktop/placement/data/train.csv',header=None)
_y_ = data[13]
data = data.drop([0],axis=1)
_X_ = data.drop([13],axis=1)
_X_ = _X_.drop([14],axis=1)
X_train, X_test, y_train, y_test = train_test_split(_X_, _y_,test_size=0.23, random_state=30)
y_test = torch.tensor(y_test.values.astype(np.float32).reshape(-1,1))
X_test = torch.tensor(X_test.values.astype(np.float32))

class placement_data(Dataset):
    
    def __init__(self):
        self.x = torch.tensor(X_train.values.astype(np.float32))
        self.y = torch.tensor(y_train.values.astype(np.float32))     

    def __getitem__(self,index):
        return self.x[index], self.y[index]
        
    def __len__(self):
        return self.x.shape[0]

dataset = placement_data()
dataloader = DataLoader(dataset=dataset,batch_size=batch_size,shuffle=False)

# logistic regression class

class LogisticRegression(torch.nn.Module):
    
    def __init__(self,input_size, num_classes):
        super(LogisticRegression,self).__init__()
        self.linear = torch.nn.Linear(input_size,1)

    def forward(self,x):
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred

model = LogisticRegression(input_size, num_classes)

# loss function and optimizer

criterion = nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr= learning_rate)

for epochs in range(num_epochs):
       
    for i,(inputs,labels) in enumerate(dataloader):

        y_pred = model(inputs)
        optimizer.zero_grad()
        loss = criterion(y_pred,labels.float())
        loss.backward()
        optimizer.step()

    print({epochs},{loss.data})    
    
for parameter in model.parameters():
    print(parameter)

#prediction

model.eval()
y_pred = model(X_test)
for i in range(0,X_test.shape[0]):
    if(y_pred[i]>0.5 or y_pred[i]==0.5):
        y_pred[i] = 1
    else:
        y_pred[i] = 0

print('precision:'+str(precision_score(y_test.detach().numpy(),y_pred.detach().numpy())))
print('accuracy:'+str(accuracy_score(y_test.detach().numpy(),y_pred.detach().numpy())))
print('f1 score:'+str(f1_score(y_test.detach().numpy(),y_pred.detach().numpy())))
print('recall:'+str(recall_score(y_test.detach().numpy(),y_pred.detach().numpy())))
