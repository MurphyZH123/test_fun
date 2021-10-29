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
for i in range(0, len(a)):
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
import re

while True:
    email = input("请输入你的邮箱:")
    if email.upper() == "Q":
        break
    res = re.findall(".com$", email)
    if not res:
        print("incorrect email format")
    temp = email.split("@")
    name = temp[0]
    com = temp[1].split(".")[0]
    print(f'username:{name},company:{com}')

# 第四题
"""
如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。  
例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
那么问题来了，求1000以内的水仙花数（3位数）
"""
import math

lists = []
for i in range(101, 1000):
    i = str(i)
    i1, i2, i3 = int(i[0]), int(i[1]), int(i[2])
    if int(i) == int(math.pow(i1, 3) + math.pow(i2, 3) + math.pow(i3, 3)):
        lists.append(i)

print(lists)

# 第五题
"""
打印99乘法表
思路：
1、外层循环，获取被乘数
2、内层循环，获取乘数
"""
for i in range(1, 10):
    for j in (1, i + 1):
        print(f'{i}*{j}={i * j}', end='')
    print()

# 第六题
"""
问题1.对列表a 中的数字从小到大排序
问题2.排序后去除重复的数字
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8] 
思路:
1、非算法方案
内置排序函数
内置去重函数
内置列表函数
2、算法方案
冒泡算发排序
内置去重函数
内置列表函数
"""
# 非算法方案
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 6, 8]
a = sorted(a)
a = set(a)
a = list(a)
print(a)

# 算法方案
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 6, 8]
for i in range(0, len(a) - 1):
    for j in range(0, len(a) - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

a = set(a)
a = list(a)
print(a)

# 第七题
"""
如果有一个列表a=[1,3,5,7,11]
问题：
1如何让它反转成[11,7,5,3,1]
2.取到奇数位值的数字，如[1,5,11]
思路：
1、非算法方案：内置排序函数、切片操作
2、算法方案：for循环，循环次数取列表长度的一半,头尾对称位置的值互换

"""
# 非算法方案一,取反
a = [1, 3, 5, 7, 11]
a = a[::-1]
print(a)

# 非算法方案二，取反
a = [1, 3, 5, 7, 11]
a.reverse()
print(a)

# 算法取反
a = [1, 3, 5, 7, 11]
lens = len(a)
for i in range(0, int(lens / 2)):
    a[i], a[lens - i - 1] = a[lens - i - 1], a[i]
print(a)

# 取奇数值
a = [1, 3, 5, 7, 11]
a = a[::2]
print(a)

# 第八题
"""
要求：判断数组元素是否对称。例如[1，2，0，2，1]，[1，2，3，3，2，1]这样的都是对称数组
用Python代码判断，是对称数组打印True，不是打印False,如：
x = [1, "a",  0, "2", 0, "a", 1]
思路：
取列表的1/2之一长度，根据索引判断对称两端的数值是否相等
"""
a, b, c = [1, 2, 0, 2, 1], [1, 2, 3, 3, 2, 1], [1, 2, 3, 4, 5]


def duicheng(lists):
    lens = len(lists)
    flag = True
    for i in range(0, int(lens / 2)):
        if lists[i] != lists[lens - 1 - i]:
            flag = False
            break
    print(flag)


duicheng(a)
duicheng(b)
duicheng(c)

# 第九题
"""
已知一个数列：1、1、2、3、5、8、13、。。。。的规律为从 3 开始的每一项都等于其前两项的和，这是斐波那契数列。
求满足规律的 100 以内的所有数据
思路：
初始lists=[1,1],每一个值等于该项前两项的和
"""
lists = [1, 1]
for i in range(2, 100):
    sum = lists[i - 1] + lists[i - 2]
    if sum < 100:
        lists.append(sum)
    else:
        break
print(lists)

# 第十题
"""
使用列表生成式语法，将列表中[1, 3, -3, 4, -2, 8, -7, 6],找出大于0的数
思路:
列表生成式 + 三元表达式
"""
a = [1, 3, -3, 4, -2, 8, -7, 6]
numbers = [i for i in range(a) if i > 0]
print(numbers)

# 第十一题
"""
如果一个正整数等于除它本身之外其他所有除数之和，就称之为完全数。
例如：6是完全数，* 因为6 = 1+2+3；
下一个完全数是28 = 14+7+4+2+1。 
求1000以下的完全数
思路：
找出当前数字的所有除数(取余为0)，然后判断是否是完全数
"""
lists = []
for i in range(6, 10001):
    num = []
    for j in range(1, i):
        if i % j == 0:
            num.append(j)
    if sum(num) == i:
        lists.append(i)
print(lists)

# 第十二题
"""
请写一个函数find_odd，参数是1个列表，请返回该列表中出现奇数次的元素
比如 
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1
find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5
find_odd([10]) ➞ 10
思路:
循环列表
调用列表内置统计函数计算当前元素出现次数
出现次数模2是否不等于0
"""


# 第一种方法：字典
def get_count(l):
    dict = {}
    for i in l:
        # 如果元素之前在字典里，那么元素对应的value值+1
        if i in dict.keys():
            dict[i] = int(dict[i]) + 1
        # 如果不在，字典中新增对应的items
        else:
            dict[i] = 1
    print(dict)


# 第二种方法
def find_odd(list1):
    res = []
    for i in list1:
        num = list1.count(i)
        if num % 2 != 0:
            res.append(i)
            return res


lists1 = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
lists2 = [20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]
lists3 = [10]
print(find_odd(lists1))
print(find_odd(lists2))
print(find_odd(lists3))

# 第十三题
"""
写一个函数，该函数 参数为1个字符串，请分析并返回包含字符串中所有大写字母索引的有序列表。
比如 
indexOfCaps("eDaBiT") ➞ [1, 3, 5]
indexOfCaps("eQuINoX") ➞ [1, 3, 4, 6]
indexOfCaps("determine") ➞ []
"""


def indexOfCaps(str1):
    list1 = list(str1)
    index1 = []
    for i in list1:
        if i.isupper():
            index1.append(list1.index(i))
    return index1


print(indexOfCaps("eDaBiT"))
print(indexOfCaps("eQuINoX"))

# 第十四题
"""
请写一个函数，该函数 参数为数字列表，请算出另外一个列表，里面每个元素依次是参数列表里面元素的累计和。
比如 参数为[1, 2, 3, 4]
结果计算方法为[1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]
返回结果就应该是[1, 3, 6, 10]
思路:
外循环获取列表每个元素
内循环获取当前元素and 之前的所有元素，最后相加
为了不影响原列表的值，需要新创建一个列表来存放相加后的值
"""


def count_list(lists):
    res = []
    lens = len(lists)
    for i in range(0, lens):
        res.append(lists[i])
        for j in range(0, i):
            res[i] = res[i] + lists[j]
    return res


lists = [1, 2, 3, 4]
print(count_list(lists))

# 第十五题
"""
请写一个函数，该函数 参数为一个字符串，请验证该字符串是否是一个合法的电话号码，合法返回True，否则返回False
规则如下
1、该字符串必须全部都是数字。
2、该字符串长度为11位。
3、该字符必须以数字1开头。
比如
validate_phone("13423445566") ➞ True
validate_phone(".23rfs") ➞ False
思路:

"""


def validate_phone(phone):
    validate_statue = True
    ret = re.findall(r"^1\d{10}", phone)
    if not ret:
        validate_statue = False
    return validate_statue


print(validate_phone("13423445566"))

# 第十六题
"""
写一个函数replace，该函数参数是两个字符串，
第一个参数给出一个源，
第二个参数是指定范围。
要求该函数将 第一个参数里面的字符串中 落在第二个参数指定范围内的字符串替换为 # 号

比如
replace("abcdef", "c-e") ➞ "ab###f"
replace("rattle", "r-z") ➞ "#a##le"
replace("microscopic", "i-i") ➞ "m#croscop#c"
replace("", "a-z") ➞ ""
"""
'''方法一'''
import re


def replace(str1, str2):
    start, end = str2.split("-")
    for i in str1:
        if start <= i <= end:
            str1 = str1.replace(i, "#")
    return str1


print(replace("abcdef", "c-e"))
'''方法二'''
import re


def replace(str1, str2):
    num1 = list(str1)
    lens = len(num1)
    temp = str2.split("-")
    for i in range(0, lens):
        if temp[0] <= num1[i] <= temp[1]:
            num1[i] = "#"
    num1 = "".join(num1)
    return num1


print(replace("abcdef", "c-e"))
print(replace("rattle", "r-z"))
print(replace("microscopic", "i-i"))
print(replace("", "a-z"))

# 第十七题
"""
写一个函数alphabet_index，该函数参数是1个字符串，
要求该函数返回一个新字符串，里面是 参数字符串中每个字母依次对应的 数字。如果是非字母，则忽略它
字母"a" 和"A" 都对应 1, "b"和"B"都对应2, "c"和"C"对应3， 依次类推
比如
alphabet_index("Wow, does that work?")
➞ "23 15 23 4 15 5 19 20 8 1 20 23 15 18 11"
alphabet_index("The river stole the gods.")
➞ "20 8 5 18 9 22 5 18 19 20 15 12 5 20 8 5 7 15 4 19"
alphabet_index("We have a lot of rain in June.")
➞ "23 5 8 1 22 5 1 12 15 20 15 6 18 1 9 14 9 14 10 21 14 5"
"""


def alphabet_index(strs):
    strs = strs.upper()
    temp = 64
    res = ""
    for i in strs:
        if i.isalpha():
            res += str(ord(i) - temp) + " "
    return res


print(alphabet_index("Wow, does that work?"))
print(alphabet_index("The river stole the gods."))
print(alphabet_index("We have a lot of rain in June."))