from torch.utils.data import Dataset
import os
from decompress_nii import decompress_nii_gz
from jpg import nii_to_jpg
from utils import *

from torchvision import transforms
transform=transforms.Compose([
    transforms.ToTensor()
])

class MyDataset(Dataset):
    def __init__(self, path):
        self.path = path
        self.name = os.listdir(os.path.join(path,"Segmentation"))
       

    def __len__(self):
        return len(self.name)
    
    #make dataset
    def __getitem__(self, index):
        segment_name = self.name[index]  # xx.nii
        segment_path = os.path.join(self.path, "Segmentation", segment_name)
        image_path = os.path.join(self.path, "JPEGImage", segment_name.replace("nii", "jpg"))

        if not os.path.isfile(segment_path):
            raise FileNotFoundError(f"no file or error path: {segment_path}")
        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"no file or error path: {image_path}")
    
        segment_image = keep_image_size_open(segment_path)
        image = keep_image_size_open(image_path)
        return transform(image), transform(segment_image)
    
    

if __name__ == "__main__":
   

    # decompress_nii_gz
    input_folder = "/home/leoniea/IP/U-Net/src/Segmentation/Task01_BrainTumour"  # 输入路径，包含 .nii.gz 文件
    output_folder = "/home/leoniea/IP/U-Net/src/Segmentation/ngz"
    os.makedirs(output_folder, exist_ok=True)
    decompress_nii_gz(input_folder, output_folder)
    print(f"decompress_nii: {os.listdir(output_folder)}")

    # nii_to_jpg
    input_folder = "/home/leoniea/IP/U-Net/src/Segmentation/ngz"  # 输入路径，包含 .nii 文件
    output_folder = "/home/leoniea/IP/U-Net/src/JPEGImage"        # 输出路径，保存转换后的 .jpg 文件
    os.makedirs(output_folder, exist_ok=True)
    nii_to_jpg(input_folder, output_folder)  # 调用转换函数
    print(f"nii_to_jpg: {os.listdir(output_folder)}") 


    data = MyDataset("/home/leoniea/IP/U-Net/src")
    print(data[0][0].shape)
    print(data[0][1].shape)