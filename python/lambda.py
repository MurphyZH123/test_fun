"""
1、Lambda函数，即Lambda 表达式(lambda expression)，是一个匿名函数（不存在函数名的函数），
Lambda表达式基于数学中的λ演算得名，直接对应于其中的lambda抽象(lambda abstraction)。

lambda x,y:x+y
<function __main__.<lambda>>

x和y是函数的两个参数，冒号后面的表达式（x+y）是函数返回值，
很明显，这个函数就是求两个变量的和，这里暂且给这个匿名函数绑定一个名字，这样使得我们调用匿名函数成为可能。



注意
匿名函数 lambda 和常规函数一样，返回的都是一个函数对象（function object）

与常规函数的区别

第一，lambda 是一个表达式（expression），并不是一个语句（statement）。
（1）lambda 可以用在一些常规函数 def 不能用的地方，比如，lambda 可以用在列表内部，而常规函数却不能
（2）lambda 可以被用作某些函数的参数，而常规函数 def 也不能

第二，lambda 的主体是只有一行的简单表达式，并不能扩展成一个多行的代码块。

"""


#例子01
l = [(lambda x: x*x)(x) for x in range(10)]
print(l)
# 输出
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]





#例子02
add = lambda x,y:x+y
add(3,4)
print(add)
#结果为7 

#等同于常规函数
def add2(x, y):
	return x+y
print(add2(3,4))












"""
2、lambda函数的使用场景
（1）函数式编程
（2）sorted、filter、map、reduce
（3）闭包
"""





#(1)函数式编程,结合sorted()使用
#例子01一个整数列表，要求按照列表中元素的绝对值大小升序排列
my_list = [3,5,-4,-1,0,-2,-6]
my_new_list = sorted(my_list, key=lambda x: abs(x))#abs()函数返回绝对值
print(my_new_list)



#例子02用 lambda 表达式对列表数据排序
students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}
]

# 按照 name 进行升序排序
students.sorted(key=lambda x : x['name'])
print(students)

# 按照 name 降序排序，reverse表示正序或者逆序，默认False正序
students.sorted(key=lambda x : x['name'], reverse=True)
print(students)

# 按照 age 升序排序
students.sorted(key=lambda x : x['age'])
print(students)


#例子03,对字典进行排序，排序完成后会变成list
"""
d.items()会输出如下结果:
dict_items([('mike', 10), ('lucy', 2), ('ben', 30)])
然后再对其进行排序

"""
#对字典的值进行排序
d = {'mike': 10, 'lucy': 2, 'ben': 30}
l=sorted(d.items(),key=lambda x : x[1],reverse=True)
print(l1)
#对字典的key进行排序
d = {'mike': 10, 'lucy': 2, 'ben': 30}
l2=sorted(d.items(),key=lambda x : x[0],reverse=True)
print(l2)




"""
02、sorted(t, key=lambda x:x[0])字典排序问题
 
key=lambda 元素: 元素[字段索引]

比如   print(sorted(C, key=lambda x: x[2]))   

x:x[]字母可以随意修改，排序方式按照中括号[]里面的维度进行排序，[0]按照第一维排序，[2]按照第三维排序


"""

d = {'b': 1, 'a': 2, 'c': 10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0]) # 根据字典键的升序排序
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1]) # 根据字典值的升序排序
d_sorted_by_key
[('a', 2), ('b', 1), ('c', 10)]
d_sorted_by_value
[('b', 1), ('a', 2), ('c', 10)]











#（2）函数式编程，结合filter()使用
#filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对list中的每个元素进行判断，返回 True或 False，
#filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。

#从list里面删除偶数
def is_odd(x):
	return x % 2 == 1
L1 = [1, 2, 3, 4, 5, 8]
L2 = filter(is_odd, L1)
print(list(L2))  # 加入list可输出结果


#删除None或者空字符串
def is_not_empty(s):
    return s and len(s.strip()) > 0
# 其中s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。
#当rm为空时，默认删除空白符（包括’\n’, ‘\r’, ‘\t’, ’ ')
print(list(filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])))


#结合lambda函数，与filter函数一起过滤
#过滤列表中的0，这里的 lambda x: True if x else False
list_num = [1, 2, 3, 0, 8, 0, 3]
print(list(filter(lambda x: x, list_num)))

#过滤掉列表中的大小写
list_num1 = ['a','B','c']
print(list(filter(lambda x:x.isupper(),list_num1)))

list_num2 = ['B','c','F']
print(list(filter(lambda x : x.islower()),list_num2))











#（3）函数式编程，结合map()使用
#第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，返回的是一个集合。
#把函数依次作用在list中的每一个元素上，得到一个新的list并返回。注意，map不改变原list，而是返回一个新list。

def square(x):
	return x ** 2
print(list(map(square,[1,2,3,4,5])))

#当不传入function时，map()就等同于zip()，将多个列表相同位置的元素归并到一个元组：
map(None,[2,4,6],[3,2,1])
#也可以返回一个指定的类型
s = " ".join(map(str, range(0, 10000)))

def add(x,y,z):
    return x,y,z

list1 = [1,2,3]
list2 = [1,2,3,4]
list3 = [1,2,3,4,5]
res = map(add, list1, list2, list3)
print(res)

#输出：
[(1, 1, 1), (2, 2, 2), (3, 3, 3), (None, 4, 4), (None, None, 5)]

#结合lambda函数，与map函数一起
#通过lambda函数返回一个列表
print(list(map(lambda x, y : x+y,[1,3,5,7,9],[2,4,6,8,10])))
#通过lambda函数返回一个元组
print(tuple(map(lambda x,y : (x**y,x+y),[2,4,6],[3,2,1])))










#(4)函数式编程，结合reduce()使用
#reduce接受两个参数，第一个是一个函数，函数必须接受两个参数，第二个是序列，
#reduce把结果继续和序列的下一个元素做累积计算，效果如下:

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
print(reduce(lambda x,y:x//y, (16,4)))













