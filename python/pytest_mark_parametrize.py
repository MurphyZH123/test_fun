""""
pytest允许多个级别启用测试参数化：
a、pytest.fixture() 允许fixture有参数化功能（后面讲解）
b、@pytest.mark.parametrize 允许在测试函数或类中定义多组参数和fixtures
c、pytest_generate_tests 允许定义自定义参数化方案或扩展（拓展）


参数化场景：
自由测试数据和期望结果不一样，但操作步骤是一样的测试用例可以用上参数化

"""







"""
使用场景一,装饰测试类
当装饰器@pytest.mark.parametrize装饰测试类时，会将数据集合传递给类的所有测试用例方法
"""

@pytest.mark.parametrize('a, b, expect', data_1)
class TestParametrize:

    def test_parametrize_1(self, a, b, expect):
        print('\n测试函数11111 测试数据为\n{}-{}'.format(a, b))
        assert a + b == expect

    def test_parametrize_2(self, a, b, expect):
        print('\n测试函数22222 测试数据为\n{}-{}'.format(a, b))
        assert a + b == expect






"""
使用场景二、笛卡尔积，多个参数化装饰器

一个函数或一个类可以装饰多个 @pytest.mark.parametrize 
这种方式，最终生成的用例数是n*m，比如上面的代码就是：参数a的数据有3个，参数b的数据有2个，所以最终的用例数有3*2=6条
当参数化装饰器有很多个的时候，用例数都等于n*n*n*n*....
"""
# 笛卡尔积，组合数据
data_1 = [1, 2, 3]
data_2 = ['a', 'b']


@pytest.mark.parametrize('a', data_1)
@pytest.mark.parametrize('b', data_2)
def test_parametrize_1(a, b):
    print(f'笛卡尔积 测试数据为 ： {a}，{b}')








"""
使用场景三、参数化，传入字典数据

"""
# 字典
data_1 = (
    {
        'user': 1,
        'pwd': 2
    },
    {
        'user': 3,
        'pwd': 4
    }
)


@pytest.mark.parametrize('dic', data_1)
def test_parametrize_1(dic):
    print(f'测试数据为\n{dic}')
    print(f'user:{dic["user"]},pwd{dic["pwd"]}')




"""
使用场景四、参数化，标记数据
"""

# 标记参数化
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    pytest.param("6 * 9", 42, marks=pytest.mark.xfail),
    pytest.param("6*6", 42, marks=pytest.mark.skip)
])
def test_mark(test_input, expected):
    assert eval(test_input) == expected







"""
使用场景四、增加可读性
"""

# 增加可读性
data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]

# ids
ids = ["a:{} + b:{} = expect:{}".format(a, b, expect) for a, b, expect in data_1]


@pytest.mark.parametrize('a, b, expect', data_1, ids=ids)
class TestParametrize(object):

    def test_parametrize_1(self, a, b, expect):
        print('测试函数1测试数据为{}-{}'.format(a, b))
        assert a + b == expect

    def test_parametrize_2(self, a, b, expect):
        print('测试函数2数据为{}-{}'.format(a, b))
        assert a + b == expect






















