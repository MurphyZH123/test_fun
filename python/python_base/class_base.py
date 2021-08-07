# coding=utf-8

class Document(object):
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context  # __开头的属性是私有属性

    def get_context_length(self):
        return len(self.__context)

    def intercept_context(self, length):
        self.__context = self.__context[:length]


harry_potter_book = Document('Harry Potter', 'J. K. Rowling',
                             '... Forever Do not believe any thing is capable of thinking independently ...')

print(harry_potter_book.title)
print(harry_potter_book.author)
print(harry_potter_book.get_context_length())

harry_potter_book.intercept_context(10)

print(harry_potter_book.get_context_length())

print(harry_potter_book.__context)
"""
类：一群有着相似性的事物的集合，这里对应 Python 的 class。
对象：集合中的一个事物，这里对应由 class 生成的某一个 object，比如代码中的 harry_potter_book。
属性：对象的某个静态特征，比如下面代码中的 title、author 和 __context。
函数：对象的某个动态能力，比如下面代码中的 intercept_context () 函数。

init函数，表示构造函数，意即一个对象生成时会被自动调用的函数。
"""
