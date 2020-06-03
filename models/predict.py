import torch

t = torch.load('/home/fuhrer/Desktop/Placement-analysis/data/classifier')
print(t['linear.bias'].shape)