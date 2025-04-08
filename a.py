from torch.utils.data import Dataset
from PIL import Image
import os

 
class MyData(Dataset):

    def __init__(self, root_dir, lable_dir):
        self.root_dir = root_dir
        self.lable_dir = lable_dir
        path=root_dir+lable_dir
        self.img_list = os.listdir(path)

    def __getitem__(self, index):
        img_path = os.path.join(self.root_dir, self.lable_dir, self.img_list[index])
        img = Image.open(img_path)
        return  img, self.lable_dir
    
    def __len__(self):
        return len(self.img_list)
    
root_dir = 'hymenoptera_data/train/'
ants_lable_dir = 'ants'
bees_lable_dir = 'bees'
ants_data = MyData(root_dir, ants_lable_dir)
bees_data = MyData(root_dir, bees_lable_dir)
print(len(ants_data))
print(ants_data[0])