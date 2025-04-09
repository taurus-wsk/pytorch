from torch import nn
import torch

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        # 定义模型层，例如:

    def forward(self, x):
        # 定义前向传播逻辑
        x=x+1
        return x

mm=MyModel()
x=torch.tensor(1)
y=mm(x)
print(y)