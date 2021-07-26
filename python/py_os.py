# 一、os关于目录路径的方法如下
import os

# 获取当前路径
path = os.getcwd()

# 获取当前绝对路径
os.path.abspath(path)

# 创建一级目录
os.mkdir(path)

# 删除空目录
os.rmdir(path)

# 创建多级目录
os.makedirs(path)

# 删除多级空目录
os.removedirs(path)

# 修改路径为path
os.chdir(path)

# 二、os关于文件的方法
import logzeros
# 获取当前路径下所有文件、文件夹
os.listdir(path)

# 创建文件方式一
f = os.open(path + 'test.txt', flags=os.O_CREAT | os.O_RDWR)

# 写入文件
os.write(f, bytes("123", encodings='utf-8'))

# 读取文件
print(os.read(f,12))

# 关闭文件
os.close(f)

# 重命名文件
os.rename(path + "test.txt", path + "tests.txt")

# 删除文件
os.remove(path + "tests.txt")

# 递归返回path下的目录（包括path目录）、子目录、文件名的三元组
for root, dirname, filenames in os.walk(path):
    logzeros.debug(root)
    logzeros.debug(dirname)
    logzeros.debug(filenames)
"""
listdir 返回的是一个列表，若没有文件则返回空列表
os.write(fd, str) 用于写入bytes字符串到文件描述符 fd 中. 返回实际写入的字符串长度
os.read(fd,n) 用于从文件描述符 fd 中读取最多 n 个字节，返回包含bytes字符串
"""

# 三、os.path相关
os.path.relpath(__file__)

# 获取当前文件所在目录
path = os.path.realpath(__file__)
print(path)

# 获取当前path所在路径
path = os.path.abspath(".")
print(path)

path = os.path.abspath(os.path.realpath(__file__))
print(path)


# os.path.dirname(path)
# 返回path的所在目录的路径
print(os.path.dirname(r'C:\Users\user\Desktop\py\moocInterface\learn\os_path_learn.py'))

print(os.path.dirname(r'C:\Users\user\Desktop\py\moocInterface\learn'))

# 表示获取当前文件所在目录的上一级目录，即项目所在目录C:\Users\user\Desktop\py\moocInterface
print(os.path.dirname(os.path.abspath('.')))


# os.path.split(path)
# 分离文件名和扩展名，返回(filename文件名，fileextension文件扩展名)二元组
# 目录
os.path.split(os.getcwd())

# 文件
os.path.split(os.path.realpath(__file__))

# os.path.join()
# 用于路径拼接，将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# 拼接目录
new_path = os.path.join(os.getcwd(), "test")
print(new_path)

# 拼接文件
new_path = os.path.join(os.getcwd(), "test.txt")
print(new_path)

# 拼接多重目录
new_path = os.path.join(os.getcwd(), "test/test/test")
print(new_path)

# 拼接多个目录、文件
new_path = os.path.join(os.getcwd(), "test", "Test", "ok.txt")
print(new_path)

















