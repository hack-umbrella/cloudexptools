#批量读文件，将内容读到同一个文件中，方便下载后，本地敏感信息读取
import os

# 指定文件夹路径、333.txt 和 444.txt 的文件名
folder_path = "path/to/folder"
input_filename = "333.txt"
output_filename = "444.txt"

# 读取333.txt文件中的所有*.properties文件的路径并存储到列表中
with open(os.path.join(folder_path, input_filename)) as file:
    properties_files = [line.strip() for line in file if line.strip().endswith('.properties')]

# 遍历列表，读取每个*.properties文件的内容并将其写入到444.txt文件中
with open(os.path.join(folder_path, output_filename), 'w') as output_file:
    for properties_file in properties_files:
        with open(os.path.join(folder_path, properties_file)) as input_file:
            output_file.write(f"File: {properties_file}\n")
            output_file.write(input_file.read())
            output_file.write("\n")
