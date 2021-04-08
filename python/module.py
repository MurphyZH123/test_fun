"""
01简单模块化


# utils.py

def get_sum(a, b):
    return a + b



# class_utils.py

class Encoder(object):
    def encode(self, s):
        return s[::-1]

class Decoder(object):
    def decode(self, s):
        return ''.join(reversed(list(s)))



# main.py

from utils import get_sum
from class_utils import *

print(get_sum(1, 2))

encoder = Encoder()
decoder = Decoder()

print(encoder.encode('abcde'))
print(decoder.decode('edcba'))

########## 输出 ##########

3
edcba
abcde
"""


"""
02层级模块-01

# utils/utils.py

def get_sum(a, b):
    return a + b


# utils/class_utils.py

class Encoder(object):
    def encode(self, s):
        return s[::-1]

class Decoder(object):
    def decode(self, s):
        return ''.join(reversed(list(s)))


# src/sub_main.py

import sys
sys.path.append("..")

from utils.class_utils import *

encoder = Encoder()
decoder = Decoder()

print(encoder.encode('abcde'))
print(decoder.decode('edcba'))

########## 输出 ##########

edcba
abcde


文件结构如下
.
├── utils
│   ├── utils.py
│   └── class_utils.py
├── src
│   └── sub_main.py
└── main.py


注意：sys.path.append("..") 表示将当前程序所在位置向上提了一级，之后就能调用 utils 的模块了。
import 同一个模块只会被执行一次，这样就可以防止重复导入模块出现问题。
"""



"""
03项目模块化
模块化的思想，那就是以项目的根目录作为最基本的目录，所有的模块调用，都要通过根目录一层层向下索引的方式来 import。


创建一个项目
.
├── proto
│   ├── mat.py
├── utils
│   └── mat_mul.py
└── src
    └── main.py



# proto/mat.py

class Matrix(object):
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.m = len(data[0])




# utils/mat_mul.py

from proto.mat import Matrix

def mat_mul(matrix_1: Matrix, matrix_2: Matrix):
    assert matrix_1.m == matrix_2.n
    n, m, s = matrix_1.n, matrix_1.m, matrix_2.m
    result = [[0 for _ in range(n)] for _ in range(s)]
    for i in range(n):
        for j in range(s):
            for k in range(m):
                result[i][k] += matrix_1.data[i][j] * matrix_2.data[j][k]

    return Matrix(result)



# src/main.py

from proto.mat import Matrix
from utils.mat_mul import mat_mul


a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])

print(mat_mul(a, b).data)

########## 输出 ##########

[[19, 22], [43, 50]]


注意：
尝试使用命令行进入 src 文件夹，直接输入 Python main.py，报错，找不到 proto。你不甘心，
退回到上一级目录，输入Python src/main.py，继续报错，找不到 proto。































