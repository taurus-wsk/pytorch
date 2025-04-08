import torch
import torchvision
from torch.utils.tensorboard import SummaryWriter
import numpy as np

# 创建一个 SummaryWriter 实例
writer = SummaryWriter('logs')

# 创建一个简单的模型
model = torchvision.models.resnet18()

# 创建一些输入数据
inputs = torch.randn(1, 3, 224, 224)

# 记录模型结构
writer.add_graph(model, inputs)

# 生成一些随机损失值
for epoch in range(10):
    loss = np.random.random()
    writer.add_scalar('Loss/train', loss, epoch)

# 关闭 SummaryWriter
writer.close()

/Users/hezenghui/Downloads/flutter
