import os
import random


class FileManager:
    @staticmethod
    def generate_attachment(size_in_mb, filename):
        # 计算文件大小的字节数
        size_in_bytes = size_in_mb * 1024 * 1024

        # 创建资源文件夹（如果不存在的话）
        resource_folder = 'resource'
        if not os.path.exists(resource_folder):
            os.makedirs(resource_folder)

        # 生成文件路径
        file_path = os.path.join(resource_folder, filename)

        # 创建并写入随机数据
        with open(file_path, 'wb') as file:
            file.write(random.getrandbits(size_in_bytes * 8).to_bytes(size_in_bytes, byteorder='big'))
