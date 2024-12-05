import os
import gzip
import shutil

def decompress_nii_gz(input_folder, output_folder):
# 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.nii.gz'):  # 只处理 .nii.gz 文件
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace('.nii.gz', '.nii'))
            
            # 解压文件
            with gzip.open(input_path, 'rb') as f_in:
                with open(output_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            print(f"解压文件：{input_path} 到 {output_path}")