"""
__new__(cls)方法
__new__(cls)必须要有一个参数cls,代表着要实例化的类，而且必须要有返回值，返回实例化出来的实例对象.

__new__(cls)和__init__(self)的区别：
__init__(self)有一个参数self,就是这个__new__(cls)返回来的实例，__init__(self)可以再__new__(cls)的基础上进行其他一些初始化的操作，而且不需要返回值。

__new__(cls)好比制造产品之前的原材料采购环节，而__init__(self)好比在买回来的原材料上进行加工的环节

"""


"""
Py中一个对象的创建流程：

调用__new__()方法来进行创建对象，这个new方法可以是object的，也可以是自己重写的，最后必须要return这个创建好的对象的引用。
调用__init__()方法来进行实例对象的初始化，__init__(self)接收的就是new方法return出来的那个创建好的对象的引用。
返回对象的引用。
所以我们可以很好的理解，__new__()只负责创建对象，而__init__()对创建好的对象进行初始化。

"""

"""
单例模式
单例模式指的是，不管创建多少次，都仅仅只有一个对象
如下:
"""
class Dog(object):
    pass

a = Dog()
b = Dog()
print( id(a) == id(b))  # False 所以指向的不是一个对象

"""
在上述例子中，a和b分别都指向创建好的2个不同的Dog类的实例对象。而单例模式指的就是，让a和b指向的是同一个对象，即不管重复创建Dog类的实例对象多少次，都只有一个实例对象。

那么实现这个模式的思路就是，第一次创建对象，第二次开始就沿用第一次创建好的对象，那么结合上面对__new__()的介绍，很容易想到是在new方法中进行处理的。

我们来使用类属性来表示当前是否是第一次创建，如下：
"""

class Dog(object):
    __instance = True # True表示是第一次创建
    __firstObj = None
    def __new__(cls):
        if cls.__instance:
            cls.__instance = False
            cls.__firstObj = object.__new__(cls)
            return cls.__firstObj # 如果是第一次创建 返回这个创建好的实例对象引用
        else:
            # 不是第一次创建  那么返回第一次创建好的对象引用
            return cls.__firstObj   

a = Dog()
b = Dog()
print( id(a) == id(b) )  # True



"""
这样就实现了功能，但是我们注意到里面有两个类属性，简化一下，其实可以写成一个，直接让__instance为None值，
第一次创建好对象之后将引用赋给__instance即可，如下：
"""

class Dog(object):
    __instance = None
    def __new__(cls):
        if cls.__instance == None: # None 就表示还没创建过对象
            cls.__instance = object.__new__(cls)
            return cls.__instance # 如果是第一次创建 返回这个创建好的实例对象引用
        else:
            # 不是第一次创建  那么返回第一次创建好的对象引用
            return cls.__instance   

a = Dog()
b = Dog()
print( id(a) == id(b) ) 

"""
实现了Python中的单例模式
"""





"""
另：
"""
class Dog(object):
    __instance = None
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
    
    def __init__(self):
        print('----init------')

a = Dog() # ----init------
b = Dog() # ----init------
"""
单例模式中，进行多次初始化实例对象的时候，虽然只会创建一次实例对象，但是__init__()会被重复调用来初始化实例对象。
我们现在如果只想让实例对象初始化一次，可以这么写
"""

class Dog(object):
    __instance = None
    __hasInit = False # 思路也是一样的  新增一个类属性表示是否第一次初始化
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
    
    def __init__(self):
        if self.__hasInit == False:
            print('----init------')
            self.__hasInit = True

a = Dog() # ----init------
b = Dog() # 不在重复初始化

















