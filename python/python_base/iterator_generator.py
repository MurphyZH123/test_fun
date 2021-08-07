"""
迭代器iterator
迭代器（iterator）提供了一个 next 的方法
通过 iter() 函数返回一个迭代器，再通过 next() 函数就可以实现遍历。for in 语句将这个过程隐式化


迭代器isinstance(obj, Iterable)


"""


def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False


params = [
    1234,
    '1234',
    [1, 2, 3, 4],
    set([1, 2, 3, 4]),
    {1: 1, 2: 2, 3: 3, 4: 4},
    (1, 2, 3, 4)
]

for param in params:
    print('{} is iterable? {}'.format(param, is_iterable(param)))


########## 输出 ##########

# 1234 is iterable? False   #除了数字之外，其他都可以迭代
# 1234 is iterable? True
# [1, 2, 3, 4] is iterable? True
# {1, 2, 3, 4} is iterable? True
# {1: 1, 2: 2, 3: 3, 4: 4} is iterable? True
# (1, 2, 3, 4) is iterable? True


# 给定一个 list 和一个指定数字，求这个数字在 list 中的位置。
# enumerate()的作用是返回列表中元素的索引号和值。

def index_normal(L, target):
    result = []
    for i, num in enumerate(L):
        if num == target:
            result.append(i)
    return result


print(index_normal([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2))

########## 输出 ##########

# [2, 5, 9]
