"""
原文bloghttps://www.cnblogs.com/se7enjean/p/13513131.html
"""




"""
1、基本用法：
·下面的实现方式是简单的实现，高级用法可以查看官方文档
·以下方式是在TestCase类下面编写的用例
·首先我们需要在用例开始的位置打上一个装饰器@pytest.mark.dependency()，这是代表这条用例作为主条件，如果这条用例失败，关联它的用例会跳过执行。
·在被关联的用例上，也打上带参数的装饰器@pytest.mark.dependency()，depends接受的参数是关联的依赖用例名。
·在depends也可以用别名的方式指定用例名。

1.1Test类下实现方式
1.2函数下实现方式
1.3通过别名制定方式
"""


import pytest
class TestCase:
	@pytest.mark.dependency()
	def test_01(self):
		assert 2==1#断言失败，这条用例会failed

	@pytest.mark.dependency(depends=["TestCase::test_01"])#test_01失败，因此test_02就跳过
	def test_02():
		assert 2==2
if __name__=='__main__':
	pytest.main()


import pytest
@pytest.mark.dependency()
def test_03():
	assert 2==1
@pytest.mark.dependency(depends=["test_03"])#test_03失败，因此test_04会跳过
def test_04():
	assert 1==1
if __name__=='__main__':
	pytest.main()


import pytest
@pytest.mark.dependency(name='a')
def test_05():
	assert 2==1
@pytest.mark.dependency(depends=["a"])
def test_06():
	assert 1==1
if __name__=='__main__':
	pytest.main()

"""
2、定义依赖范围
scope可以接受四种参数定义的类型('session','package','module','class')
2.1 scope='class'
作用于所属的类，外部类不会被关联
2.2 scope='module'
不传递scope，默认参数是'module'，作用于当前文件
只会查找当前文件的复合条件的文件名，类里同名的方法不会被依赖
2.3scope='module'
作用于当前目录同级的依赖函数，跨目录无法找到依赖的函数
2.4scope='session'
作用域全局，可跨目录调用。但被依赖的用例必须先执行,否则用例会执行跳过
"""
#01
import pytest
class TestClass1(object):
 	@pytest.mark.dependency()
 	def test_one(self):
 		assert False
class TestClass2(object):
	@pytest.mark.dependency()
	def test_one(self):
		pass
	@pytest.mark.dependency(depends=["test_one"],scope='class')#指向当前类里面的test_one
	def test_d(self):
		pass



#02不传递scope的话，默认参数是'module',作用于当前文件
import pytest

@pytest.mark.dependency()
@pytest.mark.xfail(reason="deliberate fail")
def test_a():
	assert False


class TestClass1(object):
	@pytest.mark.dependency()
	def test_b(self):
		pass
class TestClass2(object):
	@pytest.mark.dependency()
	def test_a(self):
		pass
	@pytest.mark.dependency(depends=["test_a"])#只会调用最上面的test_a
	def test_c(self):
		pass


#03scope=package，只在当前目录有效
import pytest

class TestClass1(object):
	@pytest.mark.dependency()
	def test_b(self):
		pass
class TestClass2(object):
	@pytest.mark.dependency()
	def test_a(self):
		pass
	@pytest.mark.dependency(depends=['testLogin/test_demo.py::test01'],scope='package')#testLogin目录名test_demo.py文件名test_01方法名
	def test_c(self):
		pass

#04scope='session',testLogin/test_login.py

import pytest
class TestClass1(object):
	@pytest.mark.dependency():
	def test_b(self):
		pass

class TestClass2(object):
	@pytest.mark.dependency()
	def test_a(self):
		pass

	@pytest.mark.dependency(depends=['testA/test_p1.py::test01'],scope='session')#被依赖的test01先执行
	def test_c(self):
		pass



















