

#引入，函数的核心概念

#01
"""
在 Python 中，函数是一等公民（first-class citizen），函数也是对象。
我们可以把函数赋予变量，比如下面这段代码：
"""

def func(message):
    print('Got a message: {}'.format(message))
    
send_message = func
send_message('hello world')

# 输出
#Got a message: hello world

def student_study(lesson):
	print(f'i am studing {lesson}')

xiaowang = student_study
xiaowang('math')


#02
"""
我们可以把函数当作参数，传入另一个函数中
"""

def get_message(message):
    return 'Got a message: ' + message


def root_call(func, message):
    print(func(message))
    
root_call(get_message, 'hello world')

# 输出
#Got a message: hello world

def student_study(lesson):
	return 'i am studing'+lesson

def student_score(func,lesson):
	print(student_study(lesson)+','+'my score is 80')
	
student_score(student_study,'chinese')


#03
"""
我们可以在函数里定义函数，也就是函数的嵌套。
"""

"""
这段代码中，我们在func()函数里面有重新定义了一个函数get_message()
调用后,作为 func() 的返回值返回。
"""

def func(message):
    def get_message(message):
        print('Got a message: {}'.format(message))
    return get_message(message)

func('hello world')

# 输出
#Got a message: hello world


"""
这段代码中，在student_study()函数里面定义了get_lesson()函数
调用后，作为 studeng_study()的返回值返回
"""

def student_study(lesson):
	def get_lesson(lesson):
		print(f'i am studing {lesson}')
	return get_lesson(lesson)

student_study('math')



#04
"""
要知道，函数的返回值也可以是函数对象（闭包）
"""

"""
函数 func_closure() 的返回值是函数对象 get_message 本身，
之后，我们将其赋予变量 send_message，再调用 send_message(‘hello world’)，
最后输出了'Got a message: hello world'。
"""
def func_closure():
    def get_message(message):
        print('Got a message: {}'.format(message))
    return get_message

send_message = func_closure()
send_message('hello world')

# 输出
#Got a message: hello world


"""
函数 student_study() 的返回值是函数对象 get_lesson 本身
之后，我们将其赋予变量 study_lesson,再调用 get_lesson('english')
最后输出了''
"""
def student_study():
	def get_lesson(lesson):
		print(f'i am studing {lesson}')
	return get_lesson

study_lesson  = student_study()
study_lesson('english')












#装饰器


#01简单的装饰器


"""
原始示例如下：
变量 greet 指向了内部函数 wrapper()，
而内部函数 wrapper() 中又会调用原函数 greet()，
因此，最后调用 greet() 时，
就会先打印'wrapper of decorator'，然后输出'hello world'

这里的函数 my_decorator() 就是一个装饰器，
它把真正需要执行的函数 greet() 包裹在其中，
并且改变了它的行为，但是原函数 greet() 不变。
"""

def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper

def greet():
    print('hello world')

greet = my_decorator(greet)
greet()

# 输出
# wrapper of decorator
# hello world



def student(func):
	def lesson():
		print('let\'s studing')
		func()
	return lesson

def study_lesson():
	print('my major is math')

study_lesson = student(study_lesson)
study_lesson()


"""
更简单的表示装饰器
@my_decorator就相当于前面的greet=my_decorator(greet)语句，只不过更加简洁。
这里的@，我们称之为语法糖。

"""

def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper

@my_decorator
def greet():
    print('hello world')

greet() #



def student(func):
	def lesson():
		print('let\'s studing')
		func()
	return lesson

@student()
def study_lesson():
	print('my major is math')

study_lesson()










#02带一个参数的装饰器
"""
如果原函数 greet() 中，有参数需要传递给装饰器怎么办？
一个简单的办法，是可以在对应的装饰器函数 wrapper() 上，加上相应的参数
"""

def my_decorator(func):
    def wrapper(message):
        print('wrapper of decorator')
        func(message)
    return wrapper


@my_decorator
def greet(message):
    print(message)


greet('hello world')

# 输出
# wrapper of decorator
# hello world

def student(func):
	def get_lesson(lesson):
		print('we are studing')
		func(lesson)
	return get_lesson

@student
def study_lesson(lesson):
	print(f'we are good at {lesson}')

study_lesson('math')









#03带多个参数的装饰器

"""
通常情况下，我们会把*args和**kwargs，作为装饰器内部函数 wrapper() 的参数。
*args和**kwargs，表示接受任意数量和类型的参数，
"""
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name,position):
	print(f'hello,{name},{position}')

greet('Mrs zhang','Supervisor')









#04带有自定义参数的装饰器

"""
定义一个参数，来表示装饰器内部函数被执行的次数
"""
def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)
        return wrapper
    return my_decorator


@repeat(4)
def greet(message):
    print(message)

greet('hello world')

# 输出：
# wrapper of decorator
# hello world
# wrapper of decorator
# hello world
# wrapper of decorator
# hello world
# wrapper of decorator
# hello world

"""
普通写法
"""

def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)
        return wrapper
    return my_decorator



def greet(message):
    print(message)

greet=repeat(4)(greet)#<function repeat.<locals>.my_decorator at 0x7fb96a9aedc0>
greet('hello world')











#05添加装饰器之后，原函数还是原函数吗？

"""
变量 greet 指向了内部函数 wrapper()，
而内部函数 wrapper() 中又会调用原函数 greet() 
所以原函数不变，
确实 def greet() 那部分没有变 

但是下面执行了 greet = my_decorator() 的时候，
greet就已经变了，它指向了内部函数 wrapper
"""

def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper

def greet():
    print('hello world')

greet = my_decorator(greet)
greet()
#我们试着打印出greet()函数的一些元信息
print(greet.__name__)#运行结果：wrapper


def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper

@my_decorator
def greet():
    print('hello world')

greet()
#我们试着打印出greet()函数的一些元信息
print(greet.__name__)#运行结果：wrapper





"""
为了解决这个问题，
我们通常使用内置的装饰器@functools.wrap，
它会帮助保留原函数的元信息
（也就是将原函数的元信息，拷贝到对应的装饰器函数里）。


保留元信息的意义是
我们用同一个装饰器my_decorator 装饰多个不同的函数，
那么这多个函数就都被 my_decorator 中的 wrapper 函数取代，
用 .__name__ 查看函数应该都是 'wrapper'，你到这里应该就觉得不对头了。

"""

import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)
    return wrapper
    
@my_decorator#此处相当于my_decorator(greet)
def greet(message):
    print(message)

print(greet.__name__)# 输出'greet'
greet('hello world')












#06类装饰器
"""
类装饰器主要依赖于函数__call__()，每当你调用一个类的示例时，函数__call__()就会被执行一次。
"""


class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)#这里和之前的函数装饰器不同 之前装饰器函数最后 return wrapper 而这里不仅返回了函数名称 ，还有对应的参数 return self.func(*args, *kargs) --- 之前的内部函数 wrapper 中都会有 func(*args, *kargs) 意思一样

@Count
def example():
    print("hello world")

example()

# 输出
# num of calls is: 1
# hello world

example()

# 输出
# num of calls is: 2
# hello world






"""
如上，当解释器遇到装饰器的时候就会执行bar=boo(bar)，实际上bar就变成了类装饰器的一个实例，
所以重复执行bar，成员属性自然就会不断增长。
"""
def boo(test):
    num = 0
    def wrapper():
        print(num)
    wrapper()

@boo
def bar():
    print("Hello World!")












#07装饰器的嵌套
"""
Python 也支持多个装饰器，比如写成下面这样的形式：
"""

@decorator1
@decorator2
@decorator3
def func():
    ...


#等价于
#多个装饰器装饰的顺序是从里到外(就近原则)，而调用的顺序是从外到里（就远原则）
decorator1(decorator2(decorator3(func)))


#这样，'hello world'这个例子，就可以改写成下面这样：
#多个装饰器装饰的顺序是从里到外(就近原则)，而调用的顺序是从外到里（就远原则）
import functools

def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator1')
        func(*args, **kwargs)
    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator2')
        func(*args, **kwargs)
    return wrapper


@my_decorator1
@my_decorator2
def greet(message):
    print(message)


greet('hello world')

# 输出
# execute decorator1
# execute decorator2
# hello world






"""




一、熟悉Python函数的特点
Python 函数具有以下 4 个特点:
1. 函数也是对象, 可以把函数的**名字**赋值给变量;
2. 函数(的名字)可以当做另一个函数的参数;
3. 函数可以嵌套, 即在函数里面可以定义函数;
4. 函数对象(函数名字)可以作为函数的返回值.

上面提到的 函数对象 = 函数的名字, 就把"函数的名字"当成普通的变量对待就好了,
普通的变量可以赋值, 也可以作为函数参数;
函数的名字(函数对象)同样可以赋值, 也可以作为函数参数

上面 4 个特点的例子对应文中的示例 1 - 4

1-1
def func(message):
    print('Got a message: {}'.format(message))
    
send_message = func
send_message('hello world')

# 输出
Got a message: hello world



1-2
def get_message(message):
    return 'Got a message: ' + message


def root_call(func, message):
    print(func(message))
    
root_call(get_message, 'hello world')

# 输出
Got a message: hello world


1-3
def func(message):
    def get_message(message):
        print('Got a message: {}'.format(message))
    return get_message(message)

func('hello world')

# 输出
Got a message: hello world



1-4
def func_closure():
    def get_message(message):
        print('Got a message: {}'.format(message))
    return get_message

send_message = func_closure()
send_message('hello world')

# 输出
Got a message: hello world

分别根据这 4 个示例, 来做一下完形填空(下面每一点分别对应示例 1 - 4, 这里就不重复列出了):
1. get_message 函数也是对象, 可以把 get_message 赋值给变量 send_message;
2. get_message 可以当做另一个函数(root_call)的参数;
3. get_message 函数定义在 func 函数里面;
4. 内层函数 get_message 作为外层函数 func_closure 的返回值(return get_message).

这 4 个特点看上应该还是很好理解的, 不过, 还需要补充一个知识点:

我们经常使用函数, 使用函数无非就 2 点: 定义函数和使用函数(调用函数).
我们是如何调用函数的? 在函数名后面加一对圆括号 "()" 就表示调用函数. 圆括号里加点调料, 这些调料叫参数
如: get_message 是函数名, 调用这个函数: get_message("hello decorator")

函数名后面可以加圆括号进行调用, 因此这个函数就称为"可调用". 因此, "函数名"是"可调用"的.
除了函数名可调用, 还有什么是"可调用"呢? 类实例(注意, 是"实例")也可以为"可调用", 在类里实现 __call__ 方法即可.

好了, 下面开始出大招, 请接招.







二、什么是装饰器

装饰器是同时满足上面 4 个特点的函数.

解释一下:
1. 装饰器是一个函数
2. 这个函数内部至少有一个嵌套函数
3. 这个函数或其内部函数, 至少有一个参数是函数对象(可调用)
4. 这个函数的返回值是函数对象(内部函数名)

装饰器就是这么贪心, 全部特点它都有.

既然装饰器是一个函数, 那么无非就是: 定义函数和使用函数.

1. 定义函数
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator1')
        func(*args, **kwargs)
        print('wrapper of decorator2')
    return wrapper
```

2. 使用函数

```python
def greet():
    print('hello decorator')
    
greet = my_decorator(greet)
greet()
```

```python
@my_decorator
def greet():
    print('hello decorator')
    
greet()
```

上面两种方式是等价的, 我们学习装饰器的过程:
1. 先学习将函数 4 大特征运用在函数里(定义)
2. 传入函数对象, 调用函数, 返回同名函数, 最后再调用

然而我们在大多数情况下都是直接看到 @ 语法糖, 然后不知所措, 一脸懵逼.
为了解决这个问题, 鄙人认为, 需要这样做:
- 看到 @ 语法糖的装饰器, 需要一双火眼金睛, 看出它的本来面目, 还原为最原始的使用方式.
- 原则: 上面修饰下面, 即@语法糖的函数修饰下面的函数


比如:

简单一点的:
```python
@my_decorator
def celebrate(name, message):
    pass

'''
看到什么这段代码, 火眼金睛一看, 现原形:
celebrate = my_decorator(celebrate)
'''
```

复杂一点的:
```python
@repeat(4)
def greet(msg):
    print(msg)
    
'''
老孙的火眼金睛, 难不倒我:
greet = repeat(4)(greet)
'''
```


再复杂一点的:
```python
class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        print('Count __init__')

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)

@Count
def example():
    print("hello Count")

example()
example()

'''
类装饰器又如何:
example = Count(example) # 这个不就是实例化对象么
example() # 调用类实例对象, 由 __call__ 实现
example()
'''
```

注意, 上面这个例子, 评论区很多同学不知道为什么第二次运行 example() 时, 会输出 2.
从上面的"真实面目"来看, num_calls 就是实例属性, 并不是类属性:
1. example = Count(example), 实例化对象后, 赋值给 example
2. example(), 第一次调用类实例, 调用了 __call__() 方法
3. example(), 上面调用一次 example 后, example 还没被释放呢, 既然没释放, 其内部的 num_calls 属性还保留着, 因此这里第二次调用, 不会再次初始化, 输出 2.

不知道大家注意到没有, 上面的 Count 初始化方法里, 我增加了一句 `print('Count __init__')`, 我们来运行一下上面这段代码, 结果如下:

```
Count __init__
num of calls is: 1
hello Count
num of calls is: 2
hello Count
```

Count 只初始化了一次, 输出结果与预期相符.



你看, 将装饰器还原本来面目后, 装饰器的所有问题, 请先还原为本来面目后再慢慢分析, 还有什么不会的?

大家不要被装饰器经过一番修饰之后就不认得了, 不管 @ 怎么化妆, 你都能认出它, 所以, 要学好装饰器, 你需要的是练就一双火眼金睛, 揭开层层面纱, 见其真面目的本领.

明白了这一点之后, 再回到文稿中, 看老师的讲解, 应该会明白一些.


最后, 用上面的方法, 分析一下多重装饰器修饰的问题. 借用老师给出的实例, 并稍作修改:

```python

import functools

def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('my_decorator1 - 1')
        func(*args, **kwargs)
        print('my_decorator1 - 2')
    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('my_decorator2 - 1')
        func(*args, **kwargs)
        print('my_decorator2 - 2')
    return wrapper

def my_decorator3(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('my_decorator3 - 1')
        func(*args, **kwargs)
        print('my_decorator3 - 2')
    return wrapper


@my_decorator1
@my_decorator2
@my_decorator3
def greet(message):
    print(message)

greet('hello world')
```

我们一起来揭开面纱, 根据"上面修饰下面"原则, 本来面目为:

```
greet = my_decorator1(my_decorator2(my_decorator3(greet)))
greet('hello world')
```


我们看一下这个嵌套函数 my_decorator1(my_decorator2(my_decorator3(greet)))

1. 运行 my_decorator3(greet), 出来的是一个函数对象, 此时还没有被调用, 修饰之后核心部分是这样的:

```python
print('my_decorator3 - 1')
func(*args, **kwargs)
print('my_decorator3 - 2')
```

这一部分, 就是函数体

2. my_decorator2(my_decorator3(greet)), 同理, 在上面结果的基础上, 用 my_decorator2 修饰一下

```python
print('my_decorator2 - 1')
print('my_decorator3 - 1')
func(*args, **kwargs)
print('my_decorator3 - 2')
print('my_decorator2 - 2')
```

3. my_decorator1(my_decorator2(my_decorator3(greet))), 在上面结果的基础上, 用 my_decorator2 修饰一下

```python
print('my_decorator1 - 1')
print('my_decorator2 - 1')
print('my_decorator3 - 1')
func(*args, **kwargs)
print('my_decorator3 - 2')
print('my_decorator2 - 2')
print('my_decorator1 - 2')
```

这样, 结果显而易见了, 大家自己运行以下, 自己分析一下.

试着用这套方法, 分析一下装饰器传参的情况.


"""





























