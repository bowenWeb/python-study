# r 只读，文件不存在报错
# w 只写，文件不存在创建
# a 追加，只能写，不能读，文件不存在创建
# r+ 读写，可同时读写，不覆盖原有内容，文件不存在报错
# w+ 读写，可同时读写，文件不存在创建
# a+ 读写，可同时读写，写在末尾，文件不存在创建
# 二进制文件操作需要加 b,eg：rb,wb 

with open('./a.txt','r',encoding='utf-8') as file:
    print(f'读取到的内容是1{file.read(8)}')

with open(r'C:\Demo\python-study\file.py','r',encoding='utf-8') as file:
    print(f'读取到的内容是2{file.read(8)}')

with open('a.txt','r',encoding='utf-8') as file:
    print(f'读取第一行内容是{file.readline()}')
    print(f'读取第二行内容是{file.readline()}')

with open('a.txt','a+',encoding='utf-8') as file:
    file.write("\n我是第三行")


import os

# os.rename(源路径，目标路径)，重命名，移动，不支持夸盘
os.rename('a.txt','b.txt')

# os.remove(文件路径),文件删除

# os.mkdir(目录路径),创建文件夹

# os.rmdir(目录路径) 删除目录，只能删除为空的目录

# os.getcwd() ,查看当前目录

# os.listdir(目录路径),查看目录内容

# os.path.exists(文件或目录) 判断是否存在

# os.path.isfile(路径) 判断是否是文件

# os.path.isdir(路径) 判断是否为文件夹