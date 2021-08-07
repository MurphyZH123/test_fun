# coding=utf-8
# import os

# lists = [
#     {"yoyo1": "111111"},
#     {"yoyo2": "222222"},
#     {"yoyo3": "333333"},
# ]
# with open("test.txt", "w+") as f:
#     for data in lists:
#         for key, value in data.items():
#             f.write("{},{}\n".format(key, value))
#
"""
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e"]
how to get : c = ["a1", "b2", "c3", "d4", "e5"]
"""
# a = [1, 2, 3, 4, 5]
# b = ["a", "b", "c", "d", "e"]
# c = []
# for i in range(0, len(a)):
#     a1 = a[i]
#     b1 = b[i]
#     c.append("{}{}".format(a1, b1))
# print(c)


"""
写一个小程序：控制台输入邮箱地址（格式为 username@companyname.com）， 程序识别用户名和公司名后，将用户名和公司名输出到控制台。 
要求： 
1. 校验输入内容是否符合规范（xx@polo.com）, 如是进入下一步，如否则抛出提 示"incorrect email format"。注意必须以.com 结尾 
2. 可以循环“输入--输出判断结果”这整个过程 
3. 按字母 Q（不区分大小写）退出循环，结束程序 
"""

import re

while True:
    email = raw_input("请输入你的邮箱:")
    if email.upper() == "Q":
        break
    res = re.findall(".com$", email)
    if not res:
        print("incorrect email format")
    temp = email.split("@")
    name = temp[0]
    com = temp[1].split(".")[0]
    print("username:{name} , companyName:{com}".format(name, com))

# coding=utf8
# import re
#
# while True:
#     email = raw_input("请输入你的邮箱:")
#     if email.upper() == "Q":
#         break
#     res = re.findall(".com$", email)
#     if not res:
#         print("请输入正确的邮箱")
#     tem = email.split("@")
#     username = tem[0]
#     companyName = tem[1].split(".")[0]
#     print("username:{},companyName:{}".format(username, companyName))


# """
# a = [1, 2, 3, 4, 5]
# b = ["a", "b", "c", "d", "e"]
# how to get : c = ["a1", "b2", "c3", "d4", "e5"]
# """
# a = [1, 2, 3, 4, 5]
# b = ["a", "b", "c", "d", "e"]
# c = []
# for i in range(0,len(a)):
#     tem1 = a[i]
#     tem2 = b[i]
#     c.append("{}{}".format(tem1, tem2))
# print c
# print "hello world"


# lists = [
#     {"yoyo1": "111111"},
#     {"yoyo2": "222222"},
#     {"yoyo3": "333333"},
# ]

# lists = [
#     {"yoyo1": "111111"},
#     {"yoyo2": "222222"},
#     {"yoyo3": "333333"},
# ]
# for data in lists:
#     for key, value in data.items():
#         print key, value
#
# """
# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
# 例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
# 那么问题来了，求1000以内的水仙花数（3位数）
# """
# import math
# lists = []
# for num in range(101, 1000):
#     i = str(num)
#     i1, i2, i3 = int(i[0]), int(i[1]), int(i[2])
#     if int(i) == int(math.pow(i1, 3))+int(math.pow(i2, 3))+int(math.pow(i3, 3)):
#         lists.append(num)
# print lists
#


# """
# 打印九九乘法表
# """
# for i in range(1, 10):
#     strs = ""
#     for j in range(1, i + 1):
#         print(f'{i}*{j}={i*j}', end='\t')
#     print()

"""
问题1.对列表a 中的数字从小到大排序
问题2.排序后去除重复的数字
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
"""
# a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
# a = sorted(a)
# a = set(a)  # set集合是无序的不重复元素序列
# a = list(a)
# print(a)

# a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
# for i in range(0,len(a)-1):
#     for j in range(0,len(a)-1-i):
#         if a[j] > a[j+1] :
#             a[j], a[j+1] = a[j+1], a[j]
#
# a = set(a)
# a = list(a)
# print(a)
import audioop

# """
# 如果有一个列表a=[1,3,5,7,11]
# 问题：1如何让它反转成[11,7,5,3,1]
# 2.取到奇数位值的数字，如[1,5,11]
# """
#
# # 方法一
# a = [1,3,5,7,11]
# a.reverse()
# print(a)
# print(a[::2])
#
# # 方法二
# a = [1, 3, 5, 7, 11]
# print(a[::-1])
# print(a[::2])
#
# # 方法三
# a = [1, 3, 5, 7, 11]
# m = int(len(a)/2)
# for i in range(m):
#     a[i], a[len(a)-1-i] = a[len(a)-1-i], a[i]
# print(a)

"""
要求：判断数组元素是否对称。例如[1，2，0，2，1]，[1，2，3，3，2，1]这样的都是对称数组
用Python代码判断，是对称数组打印True，不是打印False,如：
x = [1, "a",  0, "2", 0, "a", 1]
"""
x = [2, "a",  1, "2", 0, "a", 1]

for i in range(0, int(len(x)/2)):
    flag = True
    if x[i] != x[len(x)-1-i]:
        flag = False
        break
print(flag)




