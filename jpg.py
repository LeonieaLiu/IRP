import os
import nibabel as nib
from PIL import Image
import numpy as np

def nii_to_jpg(input_folder, output_folder):
    """
    将 .nii 文件转换为 .jpg 格式，保存到输出文件夹。
    
    参数:
    input_folder (str): 包含 .nii 文件的输入文件夹路径。
    output_folder (str): 保存转换后的 .jpg 文件的输出文件夹路径。
    """
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的所有 .nii 文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.nii'):  # 只处理 .nii 文件
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace('.nii', '.jpg'))

            # 加载 .nii 文件
            nii_image = nib.load(input_path)
            image_data = nii_image.get_fdata()  # 获取影像数据

            # 将影像数据转为2D图像 (假设我们只取其中一个切片)
            slice_data = image_data[:, :, image_data.shape[2] // 2]  # 选择中心切片
            slice_data = np.uint8(slice_data / np.max(slice_data) * 255)  # 归一化并转换为 0-255 的像素值

            # 将 numpy 数组转换为 PIL Image 对象
            image = Image.fromarray(slice_data)

            # 保存为 .jpg 格式
            image.save(output_path)
            print(f"转换完成：{input_path} 到 {output_path}")

