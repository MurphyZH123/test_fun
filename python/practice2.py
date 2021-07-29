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
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]







