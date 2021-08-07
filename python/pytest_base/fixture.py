"""
一、fixture用途
1、做测试前后的初始化设置，如测试数据准备，链接数据库，打开浏览器等这些操作都可以使用fixture来实现
2、测试用例的前置条件可以使用fixture实现
3、支持经典的xunit fixture ，像unittest使用的setup和teardown
4.fixture可以实现unittest不能实现的功能，比如unittest中的测试用例和测试用例之间是无法传递参数和数据的，但是fixture却可以解决这个问题
"""


"""
二、fixture定义
fixture通过@pytest.fixture()装饰器装饰一个函数，那么这个函数就是一个fixture，看个实例
"""
import pytest

@pytest.fixture()
def fixtureFunc():
    return 'fixtureFunc'

def test_fixture(fixtureFunc):
    print('我调用了{}'.format(fixtureFunc))

if __name__=='__main__':
    pytest.main(['-v', 'test_fixture.py'])

"""
三、fixture使用
调用fixture有三种方式
1、Fixture名字作为用例的参数
"""
# test_fixture.py

import pytest

@pytest.fixture()
def fixtureFunc():
    return 'fixtureFunc'

def test_fixture(fixtureFunc):
    print('我调用了{}'.format(fixtureFunc))

class TestFixture(object):
    def test_fixture_class(self, fixtureFunc):
        print('在类中使用fixture "{}"'.format(fixtureFunc))

if __name__=='__main__':
    pytest.main(['-v', 'test_fixture.py'])


"""
2、使用@pytest.mark.usefixtures('fixture')装饰器
每个函数或者类前使用@pytest.mark.usefixtures('fixture')装饰器装饰
"""
# test_fixture.py
import pytest
@pytest.fixture()
def fixtureFunc():
    print('\n fixture->fixtureFunc')

@pytest.mark.usefixtures('fixtureFunc')
def test_fixture():
    print('in test_fixture')

@pytest.mark.usefixtures('fixtureFunc')
class TestFixture(object):
    def test_fixture_class(self):
        print('in class with text_fixture_class')

if __name__=='__main__':
    pytest.main(['-v','-s' 'test_fixture.py'])






"""
3、使用autouse参数
指定的fixture的参数autouse=Ture这样每个测试用例会自动调用fixture
(其实这里的说的不是很准确，因为还涉及到fixture的作用范围，那么我们这里默认是函数级别的，后面会具体说fixture的作用范围)
"""
# test_fixture.py
import pytest
@pytest.fixture(autouse=True)
def fixtureFunc():
    print('\n fixture->fixtureFunc')

def test_fixture():
    print('in test_fixture')

class TestFixture(object):
    def test_fixture_class(self):
        print('in class with text_fixture_class')

if __name__=='__main__':
    pytest.main(['-v', 'test_fixture.py'])


"""
综上，
如果测试用例需要使用fixture中返回的参数，那么通过后面这两种方式是无法使用返回的参数的，
因为fixture中返回的数据默认存在fixture名字里面存储，所以只能使用第一种方式才可以调用fixture中的返回值。
"""







"""
补充：
一、fixture作用范围
scope参数可以是session， module，class，function； 默认为function

1.session 会话级别（通常这个级别会结合conftest.py文件使用，所以后面说到conftest.py文件的时候再说）

2.module 模块级别： 模块里所有的用例执行前执行一次module级别的fixture

3.class 类级别 ：每个类执行前都会执行一次class级别的fixture

4.function ：前面实例已经说了，这个默认是默认的模式，函数级别的，每个测试用例执行前都会执行一次function级别的fixture

二、关于返回值
fixture是可以返回值的，如果没return默认返回None。用例调用fixture的返回值，直接就是把fixture的函数名称当成变量名称，
如下：
"""
# test_fixture1.py
import pytest

@pytest.fixture()
def user():
    print("获取用户名")
    a = "yoyo"
    return a

def test_1(user):
    assert user == "yoyo"

if __name__ == "__main__":
    pytest.main(["-s", "test_fixture1.py"])

"""
测试结果一般有三种：passed、failed、error（skip的用例除外）
如果在test_用例里面断言失败，那就是failed
如果在fixture里面断言失败了，那就是error
"""



#fixture之yield实现teardown
import pytest

def test_01(self):
    pass

@pytest.fixture(scope="session")
def open():
    # 会话前置操作setup
    print("===打开浏览器===")
    test = "测试变量是否返回"
    yield test
    # 会话后置操作teardown
    print("==关闭浏览器==")


@pytest.fixture
def login(open):
    # 方法级别前置操作setup
    print(f"输入账号，密码先登录{open}")
    name = "==我是账号=="
    pwd = "==我是密码=="
    age = "==我是年龄=="
    # 返回变量
    yield name, pwd, age
    # 方法级别后置操作teardown
    print("登录成功")


def test_s1(login):
    print("==用例1==")
    # 返回的是一个元组
    print(login)
    # 分别赋值给不同变量
    name, pwd, age = login
    print(name, pwd, age)
    assert "账号" in name
    assert "密码" in pwd
    assert "年龄" in age


def test_s2(login):
    print("==用例2==")
    print(login)

if __name__=='__main__':
    pytest.main(['-s','-v',"test_practice.py"])

"""
yield注意事项
如果yield前面的代码，即setup部分已经抛出异常了，则不会执行yield后面的teardown内容
如果测试用例抛出异常，yield后面的teardown内容还是会正常执行
"""


















