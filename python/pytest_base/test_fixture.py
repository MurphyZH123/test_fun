# import pytest

# @pytest.fixture()
# def fixtureFunc():
#     return 'fixtureFunc'

# def test_fixture(fixtureFunc):
#     print('我调用了{}'.format(fixtureFunc))

# if __name__=='__main__':
#     pytest.main(['-v', 'test_fixture.py'])
    


# test_fixture.py

# import pytest

# @pytest.fixture()
# def fixtureFunc():
#     return 'fixtureFunc'

# def test_fixture(fixtureFunc):
#     print('我调用了{}'.format(fixtureFunc))

# class TestFixture(object):
#     def test_fixture_class(self, fixtureFunc):
#         print('在类中使用fixture "{}"'.format(fixtureFunc))

# if __name__=='__main__':
#     pytest.main(['-v', 'test_fixture.py'])




# # test_fixture1.py
# import pytest

# @pytest.fixture()
# def user():
#     print("获取用户名")
#     a = "yoyo"
#     return a

# def test_1(user):
#     assert user == "yoyo"

# if __name__ == "__main__":
#     pytest.main(["-s", "test_fixture.py"])


import  pytest
@pytest.fixture()
def login():
    print("输入账号，密码先登录")

def test_s1(login):
    print("用例1：登录之后其它动作111")

def test_s2():  # 不传login
    print("用例2：不需要登录，操作222")

def test_s3(login):
    print("用例3：登录之后其它动作333")

if __name__ == "__main__":
    pytest.main(["-s", "test_fix.py"])