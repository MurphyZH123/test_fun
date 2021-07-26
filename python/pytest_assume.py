"""
原文链接：https://www.cnblogs.com/poloyy/p/12704658.html

pytest中可以用python的assert断言，也可以写多个断言，但一个失败，后面的断言将不再执行

安装插件：pip3 install pytest-assume -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

前提：assert多重断言时，该断言遇到失败的就不会继续执行，包括正常的代码：
	def test_add1():
	    assert 1 + 4 == 5
	    assert 1 + 3 == 3
	    assert 2 + 5 == 7
	    assert 2 + 5 == 9
	    print("测试完成
	


场景：pytest.assure多重断言
def test_add2():
    pytest.assume(1 + 4 == 5)
    pytest.assume(1 + 3 == 3)
    pytest.assume(2 + 5 == 7)
    pytest.assume(2 + 5 == 9)
    print("测试完成")



上下文管理器，pytest.assume 也可以使用上下文管理器去断言
import pytest
from pytest import assume
@pytest.mark.parametrize(('x', 'y'),[(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
	print("测试数据x=%s, y=%s" % (x, y))
	with assume: assert x == y
	with assume: assert x+y > 1
	with assume: assert x > 1
	print("测试完成！")

注意，每个with块只能有一个断言，如果一个with下有多个断言，当地一个断言失败的时候，后面的断言就不会起作用的

"""