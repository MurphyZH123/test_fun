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