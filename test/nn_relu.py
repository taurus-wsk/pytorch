from torch import nn
from torch.nn import ReLU, Sequential
from torch.utils.data import DataLoader
import torch
import torchvision

input= torch.tensor([1,-0.5],[-1,3])
input = torch.reshape(input, (-1, 1, 2, 2))
print(input.shape)

dataset=torchvision.dataset.CIFAR10(root='../data', train=False, download=True,transform=torchvision.transforms.ToTensor())

dataloader=DataLoader(dataset, batch_size=4)

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.relu = ReLU()
        self.sequential = Sequential()

    def forward(self, x):
        x = self.sequential(x)
        return x