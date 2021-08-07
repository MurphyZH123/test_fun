#01初学例子
def my_func(message):
    print('Got a message: {}'.format(message))

# 调用函数 my_func()
my_func('Hello World')
# 输出
#Got a message: Hello World




"""
02isinstance()函数，
功能，是判断python中的设定函数的类型,
语法，是isinstance(object,classinfo)，其中object就是你的对象名称，classinfo就是你要判断的类型
与type()的区别，isinstance()考虑了继承关系，会认为子类是一种父类类型，而type()不考虑
"""

def find_largest_element(l):
    if not isinstance(l, list):
        print('input is not type of list')
        return
    if len(l) == 0:
        print('empty input')
        return
    largest_element = l[0]
    for item in l:
        if item > largest_element:
            largest_element = item
    print('largest element is: {}'.format(largest_element)) 
      
find_largest_element([0, 1,-3, 2, 8])

# 输出
#largest element is: 8




#03函数嵌套
"""
函数嵌套主要有两个好处
第一，函数的嵌套能够保证内部函数的隐私。
内部函数只能被外部函数所调用和访问，不会暴露在全局作用域，
因此，如果你的函数内部有一些隐私数据（比如数据库的用户、密码等），
不想暴露在外，那你就可以使用函数的的嵌套，将其封装在内部函数中，只通过外部函数来访问。
第二，合理的使用函数嵌套，能够提高程序的运行效率。
"""
def f1():
    print('hello')
    def f2():
        print('world')
    f2()
f1()

# 输出
# hello
# world


#第二个优点实例

def factorial(input):
    # validation check
    if not isinstance(input, int):
        raise Exception('input must be an integer.')
    if input < 0:
        raise Exception('input must be greater or equal to 0' )
    ...

    def inner_factorial(input):
        if input <= 1:
            return 1
        return input * inner_factorial(input-1)
    return inner_factorial(input)


print(factorial(5))





"""
04函数变量作用域
"""
#如果我们在函数内使用全局变量，且要改变全局的变量的值，那么我们需要在使用时，在函数内用global声明一下
min_number = 1
max_number = 4
def judge_number(value):
    global min_number
    global max_number
    min_number += 1
    max_number += value
    return max_number

max_number1= judge_number(2)
print(max_number1)

#如果遇到函数内部局部变量和全局变量同名的情况，那么在函数内部，局部变量会覆盖全局变量
min_number = 2
def judge_number(i):
    min_number = 3
    if min_number > i:
        min_number = i
    return min_number

min_number1 = judge_number(1)
print(min_number1)



#对于嵌套函数来说，内部函数可以访问外部函数定义的变量，但是无法修改，若要修改，必须加上 nonlocal 这个关键字:
def outer():
    x = "local"
    def inner():
        nonlocal x # nonlocal关键字表示这里的x就是外部函数outer定义的变量x
        x = 'nonlocal'
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
# 输出
# inner: nonlocal
# outer: nonlocal

def judge_num(value):
    min_number = 1
    def save_num():
        nonlocal min_number#加上nonlocal后，全局变量min_number的值被修改
        if value < min_number:
            min_number = value
        print(min_number)
    save_num()
    print(min_number)
judge_num(0)

#如果不加上 nonlocal 这个关键字，而内部函数的变量又和外部函数变量同名，那么同样的，内部函数变量会覆盖外部函数的变量。
def outer():
    x = "local"
    def inner():
        x = 'nonlocal' # 这里的x是inner这个函数的局部变量
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
# 输出
# inner: nonlocal
# outer: local



"""
05闭包
"""
#闭包其实和刚刚讲的嵌套函数类似，不同的是，这里外部函数返回的是一个函数，而不是一个具体的值。

#例子01
def nth_power(exponent): 
    def exponent_of(base): 
        return base ** exponent 
    return exponent_of # 返回值是exponent_of函数
square = nth_power(2) # 计算一个数的平方，输出<function __main__.nth_power.<locals>.exponent(base)>
cube = nth_power(3) # 计算一个数的立方，输出<function __main__.nth_power.<locals>.exponent(base)>
print(square(6))#计算6的平方
print(cube(7))#计算7的平方
""""
这里外部函数 nth_power() 返回值，是函数 exponent_of()，而不是一个具体的数值。
需要注意的是，在执行完square = nth_power(2)和cube = nth_power(3)后，外部函数 nth_power() 的参数 exponent，
仍然会被内部函数 exponent_of() 记住。
这样，之后我们调用 square(2) 或者 cube(2) 时，
程序就能顺利地输出结果，而不会报错说参数 exponent 没有定义了。
"""



#总结和拓展
#闭包相关知识  https://zhuanlan.zhihu.com/p/26934085





























