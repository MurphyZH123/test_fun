#例子01
class Document():
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context # __开头的属性是私有属性

    def get_context_length(self):
        return len(self.__context)

    def intercept_context(self, length):
        self.__context = self.__context[:length]

harry_potter_book = Document('Harry Potter', 'J. K. Rowling', '... Forever Do not believe any thing is capable of thinking independently ...')

print(harry_potter_book.title)
print(harry_potter_book.author)
print(harry_potter_book.get_context_length())

harry_potter_book.intercept_context(10)

print(harry_potter_book.get_context_length())

print(harry_potter_book.__context)



"""
class Document 定义了 Document 类，
再往下能看到它有三个函数，这三个函数即为 Document 类的三个函数。
其中，init 表示构造函数，意即一个对象生成时会被自动调用的函数。
我们能看到， harry_potter_book = Document(...)这一行代码被执行的时候，
'init function called'字符串会被打印出来。

而 get_context_length() 和 intercept_context() 则为类的普通函数，我们调用它们来对对象的属性做一些事情。
class Document 还有三个属性，title、author 和 __context 分别表示标题、作者和内容，通过构造函数传入。
这里代码很直观，我们可以看到， intercept_context 能修改对象 harry_potter_book 的 __context 属性。


这里唯一需要强调的一点是，如果一个属性以 __ （注意，此处有两个 _） 开头，我们就默认这个属性是私有属性。
私有属性，是指不希望在类的函数之外的地方被访问和修改的属性。
所以，你可以看到，title 和 author 能够很自由地被打印出来，但是 print(harry_potter_book.__context)就会报错。
"""

#例子02

class Document():
    
    WELCOME_STR = 'Welcome! The context for this book is {}.'
    
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context
    
    # 类函数
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context='nothing')
    
    # 成员函数
    def get_context_length(self):
        return len(self.__context)
    
    # 静态函数
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)


empty_book = Document.create_empty_book('What Every Man Thinks About Apart from Sex', 'Professor Sheridan Simove')


print(empty_book.get_context_length())
print(empty_book.get_welcome('indeed nothing'))



"""
01针对如何在一个类中定义一些常量，每个对象都可以方便访问这些常量而不用重新构
使用WELCOME_STR，用大写来表示常量，因此我们可以在类中使用 self.WELCOME_STR ，或者在类外使用 Entity.WELCOME_STR ，来表达这个字符串。

02如果一个函数不涉及到访问修改这个类的属性，而放到类外面有点不恰当，怎么做才能更优雅呢？
我们提出了类函数、成员函数和静态函数三个概念。
它们其实很好理解，前两者产生的影响是动态的，能够访问或者修改对象的属性；
而静态函数则与类没有什么关联，最明显的特征便是，静态函数的第一个参数没有任何特殊性。

具体来看这几种函数。
一般而言，静态函数可以用来做一些简单独立的任务，既方便测试，也能优化代码结构。
 1静态函数还可以通过在函数前一行加上 @staticmethod 来表示，代码中也有相应的示例。
 而类函数的第一个参数一般为 cls，表示必须传一个类进来。
 2类函数最常用的功能是实现不同的 init 构造函数，
 比如上文代码中，我们使用 create_empty_book 类函数，来创造新的书籍对象，其 context 一定为 'nothing'。
 这样的代码，就比你直接构造要清晰一些。类似的，类函数需要装饰器 @classmethod 来声明。
 3成员函数则是我们最正常的类的函数，它不需要任何装饰器声明，第一个参数 self 代表当前对象的引用，可以通过此函数，来实现想要的查询 / 修改类的属性等功能。

03既然类是一群相似的对象的集合，那么可不可以是一群相似的类的集合呢？
可以通过类的继承来实现
"""



#例子03
'''
类的继承
指的是一个类既拥有另一个类的特征，也拥有不同于另一个类的独特特征。
在这里的第一个类叫做子类，另一个叫做父类，特征其实就是类的属性和函数。
'''
class Entity():
    def __init__(self, object_type):
        print('parent class init called')
        self.object_type = object_type
    
    def get_context_length(self):
        raise Exception('get_context_length not implemented')
    
    def print_title(self):
        print(self.title)

class Document(Entity):
    def __init__(self, title, author, context):
        print('Document class init called')
        Entity.__init__(self, 'document')
        self.title = title
        self.author = author
        self.__context = context
    
    def get_context_length(self):
        return len(self.__context)
    
class Video(Entity):
    def __init__(self, title, author, video_length):
        print('Video class init called')
        Entity.__init__(self, 'video')
        self.title = title
        self.author = author
        self.__video_length = video_length
    
    def get_context_length(self):
        return self.__video_length

harry_potter_book = Document('Harry Potter(Book)', 'J. K. Rowling', '... Forever Do not believe any thing is capable of thinking independently ...')
harry_potter_movie = Video('Harry Potter(Movie)', 'J. K. Rowling', 120)

print(harry_potter_book.object_type)
print(harry_potter_movie.object_type)

harry_potter_book.print_title()
harry_potter_movie.print_title()

print(harry_potter_book.get_context_length())
print(harry_potter_movie.get_context_length())

"""
父与子类的构造函数继承关系
其中父类是Entity，子类是Document、Video
情况一：子类需要自动调用父类的方法：子类不重写__init__()方法，实例化子类后，会自动调用父类的__init__()的方法。
情况二：子类不需要自动调用父类的方法：子类重写__init__()方法，实例化子类后，将不会自动调用父类的__init__()的方法。 
情况三：子类重写__init__()方法又需要调用父类的方法：使用super关键词。
"""



























