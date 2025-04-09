import torch

input =torch.tensor([[1,2,0,3,1],
                     [0,1,2,3,1],
                     [1,2,1,0,0],
                     [2,1,0,1,1]])
input =torch.reshape(input, (-1,1, 5, 5))
print(input)

class MyModel(torch.nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.pool = torch.nn.MaxPool2d(2, ceil_mode=True)
    def forward(self, x):
        x=self.pool(x)
        return x

mm=MyModel()
output=mm(input)
print(output)