"""
原文链接：https://www.cnblogs.com/chenhuabin/p/11288797.html
"""

"""
1.1在python中，我们把所有可以迭代的对象统称为可迭代对象，有一个类专门与之对应：Iterable
要判断一个类是否可迭代，只要判断是否是Iterable类的实例即可
只要一个对象定义了__iter__()方法，那么它就是可迭代对象。
如下：

"""
from collections.abc import Iterable
class A():
    def __iter__(self):
        pass
print('A()是可迭代对象吗：',isinstance(A(),Iterable))



"""
1.2迭代器是对可迭代对象的改造升级，
如果一个对象同时实现了__iter__()和__next()__方法，那么它就是迭代器
在python中，也有一个类与迭代器对应：Iterator。所以，要判断一个类是否是迭代器，只要判断是否是Iterator类的实例即可
"""

from collections.abc import Iterable
from collections.abc import Iterator
class B():
    def __iter__(self):
        pass
    def __next__(self):
        pass
print('B()是可迭代对象吗：',isinstance(B(), Iterable))
print('B()是迭代器吗：',isinstance(B(), Iterator))


"""
for循环的本质
说到__iter__()__next__()方法


































