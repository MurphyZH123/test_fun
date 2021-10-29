"""
一、递归
它通常把一个大型复杂的问题层层转化为一个与原问题相似的规模较小的问题来求解，递归策略只需少量的程序就可描述出解题过程所需要的多次重复计算，大大地减少了程序的代码量

注意：
递归就是在过程或函数里面调用自身;
在使用递归时,必须有一个明确的递归结束条件,称为递归出口

递归，就是在运行的过程中调用自己。
构成递归需具备的条件：
1. 子问题须与原始问题为同样的事，且更为简单；
2. 不能无限制地调用本身，须有个出口，化简为非递归状况处理。

递归经典案例：
1斐波那契数列 2阶乘 3汉诺塔问题 4 全排列
参考链接https://blog.csdn.net/qq_40817827/article/details/89950325

二、迭代
迭代法也称辗转法，是一种不断用变量的旧值递推新值的过程，跟迭代法相对应的是直接法(或者成为一次解法），即一次性解决问题
迭代经典案例：
1斐波那契数列 2汉诺塔问题 3背包问题


三、迭代和递归的关系和区别
从概念上讲，递归就是指程序调用自身的编程思想，即一个函数调用本身；
迭代是利用已知的变量值，根据递推公式不断演进得到变量新值得编程思想。
简单地说，递归是重复调用函数自身实现循环。
迭代是函数内某段代码实现循环，而迭代与普通循环的区别是：循环代码中参与运算的变量同时是保存结果的变量，当前保存的结果作为下一次循环计算的初始值。

迭代与普通循环的区别是：迭代时，循环代码中参与运算的变量同时是保存结果的变量，当前保存的结果作为下一次循环计算的初始值。
递归与普通循环的区别是：循环是有去无回，而递归则是有去有回(因为存在终止条件)。

"""


# 试着用递归打印*号


#  demo1
def digun1(n):
    if n == 0:
        print('')
        return
    else:
        digun1(n - 1)
        print(('*' * n))


#  demo2
def digun2(n):
    if n == 0:
        print('')
        return
    else:
        print(('*' * n))
        digun2(n - 1)
    return n


# digun2(5)

#  斐波那契数列的迭代实现
def fib1(x):
    if x < 2:
        return 0 if x == 0 else 1
    else:
        return fib1(x - 1) + fib1(x - 2)


print(fib1(6))


# 递归实现斐波那契数列
def fib2(x):
    n1 = 1
    n2 = 1
    n3 = 1

    while x - 2 > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        x -= 1
    return n3


num = int(input('请输入一个正整数：'))
print(fib2(num))

"""
练习1
编写一个名为collatz()的函数，它有一个名为number 的参数。
如果参数是偶数，那么collatz()就打印出number// 2，并返回该值。
如果number 是奇数，collatz()就打印并返回3 * number + 1。
然后编写一个程序，让用户输入一个正整数，并不断对这个数调用collatz()，直到函数返回值１
"""


def collatz(num):
    if num == 1:
        return 0
    elif num % 2 == 0:
        print(num // 2)
        collatz(num // 2)
    elif num % 2 == 1:
        print(3 * num + 1)
        collatz(3 * num + 1)


# collatz(3)

"""
练习题2使用递归实现阶乘
"""


# 1)错误递归方法
def fac1(num):
    if num == 1:
        result = 1
    else:
        result = num * (num - 1)
        fac1(num - 1)
    return result


# 2)正确的递归方法
def fac2(num):
    if num == 1:
        result = 1
    else:
        result = num * fac2(num - 1)
    return result


# print(fac1(4))


#  使用迭代实现阶乘
def fac3(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


"""
练习题3 https://blog.csdn.net/qq_45556599/article/details/104872207
"""

"""
练习题
杨辉三角形,使用嵌套列表的方式
"""


def triangle(n):
    l = []
    for i in range(n):
        if i == 0:
            l.append(1)
        elif i == 1:
            l.append(1, 1)
        else:
            y = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    y.append(1)
                else:
                    y.append(l[i - 1][j - 1] + l[i - 1][j])
            l.append(y)
    return l


n = 12
x = triangle(n)
for i in range(x):
    print(i)

"""
杨辉三角形使用生成器的方式
"""


def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0]+a, a+[0])]
n=0
for t in triangles():
    print(t)
    n=n+1
    if n==10:
        break
