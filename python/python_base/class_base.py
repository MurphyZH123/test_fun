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

print(harry_potter_book.__context) # __context是似有属性，不允许在类之外的地方被访问
"""
1、
类：一群有着相似性的事物的集合，这里对应 Python 的 class。
对象：集合中的一个事物，这里对应由 class 生成的某一个 object，比如代码中的 harry_potter_book。
属性：对象的某个静态特征，比如下面代码中的 title、author 和 __context。
函数：对象的某个动态能力，比如下面代码中的 intercept_context () 函数。

2、init函数，表示构造函数，意即一个对象生成时会被自动调用的函数。
如harry_potter_book = Document(...)这一行代码被执行的时候，'init function called'字符串会被打印出来。

3、get_context_length() 和 intercept_context() 则为类的普通函数，我们调用它们来对对象的属性做一些事情。

4、class Document 还有三个属性，title、author 和 __context 分别表示标题、作者和内容，通过构造函数传入。
这里代码很直观，我们可以看到， intercept_context 能修改对象 harry_potter_book 的 __context 属性。
如果一个属性以 __ （注意，此处有两个 _） 开头，我们就默认这个属性是私有属性。私有属性，是指不希望在类的函数之外的地方被访问和修改的属性。
所以，你可以看到，title 和 author 能够很自由地被打印出来，但是 print(harry_potter_book.__context)就会报错。
"""
