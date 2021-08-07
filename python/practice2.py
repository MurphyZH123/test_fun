# coding = utf-8
# 第一题
"""
lists = [
    {"yoyo1": "111111"},
    {"yoyo2": "222222"},
    {"yoyo3": "333333"},
]
how to get：
yoyo1,111111
yoyo2,222222
yoyo3,333333
"""
lists = [
    {"yoyo1": "111111"},
    {"yoyo2": "222222"},
    {"yoyo3": "333333"},
]
for data in lists:
    for key, value in data.items():
        print(f"{key},{value}")


# 第二题
"""
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e"]
how to get : c = ["a1", "b2", "c3", "d4", "e5"]
"""
a = [1, 2, 3, 4, 5]
b = ["a", "b", "c", "d", "e"]
c = []
for i in range(0,len(a)):
    a1 = a[i]
    b1 = b[i]
    c.append(f'{a1}{b1}')
print(c)


# 第三题
"""
写一个小程序：控制台输入邮箱地址（格式为 username@companyname.com）， 程序识别用户名和公司名后，将用户名和公司名输出到控制台。 
要求： 
1. 校验输入内容是否符合规范（xx@polo.com）, 如是进入下一步，如否则抛出提 示"incorrect email format"。注意必须以.com 结尾 
2. 可以循环“输入--输出判断结果”这整个过程 
3. 按字母 Q（不区分大小写）退出循环，结束程序 
"""

while True:
    email = input("请输入你的邮箱:")
    if email.upper() == "Q":
        break



