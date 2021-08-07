
"""
编写规则
1、测试文件以test开头(以test结尾也可以)
2、测试类以Test开头,并且不能带有init方法
3、测试函数以test开头
4、断言使用基本的assert即可
"""

"""
console参数介绍
·-v用于显示每个测试函数的执行结果
·-q只显示整体的测试结果
·-s用于显示测试函数中print()函数输出
·-x，--exitfirst，在第一个错误或测试失败时立即退出
-h帮助
"""


"""
执行测试用例的过滤
1、pytest.main::['-k']
2、pytest.mark.do  pytest.mark.undo需要创建标记过滤文件pytest.ini
"""


"""
pytest参数化处理







"""
项目的根目录下创建  conftest.py 文件，是pytest的配置文件。文件会自动被pytest识别。
"""
import pytest

@pytest.fixture(scope="session",autouse=True)
def session():
    print("在所有的测试用例执行之前执行")

    yield

    print("执行所有的用例执行之后的操作")

@pytest.fixture(scope='module',autouse=True)
def module():
    print('每个py文件运行之前的操作')
    yield
    print('每个py文件运行之后的操作')

@pytest.fixture(scope='class',autouse=True)
def object():
    print('每个class类运行之前')
    yield
    print('每个class类运行之后的操作')

@pytest.fixture(scope='function',autouse=True)
def func():
    print('每个函数执行之前')
    yield
    print('每个函数执行之后')


"""
pytest 支持4个级别的执行顺序。
session    所有的测试用例之执行先后
module    整个py文件执行先后
class   每一个class 测试类执行之前和之后的操作
function  每一个函数执行之前之后

在使用pytest脚手架的时候， 主要使用到两个参数
scope= ""   表示区域
autouse =   是否自动使用。
"""
configure webviews for debugging#开启debug


def test_webview(driver:WebView)