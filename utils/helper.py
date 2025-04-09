def save_model(model, filepath):
    """保存模型的状态字典到指定路径"""
    torch.save(model.state_dict(), filepath)

def load_model(model, filepath):
    """从指定路径加载模型的状态字典"""
    model.load_state_dict(torch.load(filepath))
    model.eval()  # 设置模型为评估模式