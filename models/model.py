class MyModel(torch.nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        # 定义模型层，例如：
        self.fc = torch.nn.Linear(10, 2)  # 示例：输入10维，输出2维

    def forward(self, x):
        # 定义前向传播逻辑
        return self.fc(x)