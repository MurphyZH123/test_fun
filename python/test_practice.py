#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__title__  =
__Time__   = 2020-04-06 15:50
__Author__ = 小菠萝测试笔记
__Blog__   = https://www.cnblogs.com/poloyy/
"""

# import pytest

# def test_01(self):
#     pass

# @pytest.fixture(scope="session")
# def open():
#     # 会话前置操作setup
#     print("===打开浏览器===")
#     test = "测试变量是否返回"
#     yield test
#     # 会话后置操作teardown
#     print("==关闭浏览器==")


# @pytest.fixture
# def login(open):
#     # 方法级别前置操作setup
#     print(f"输入账号，密码先登录{open}")
#     name = "==我是账号=="
#     pwd = "==我是密码=="
#     age = "==我是年龄=="
#     # 返回变量
#     yield name, pwd, age
#     # 方法级别后置操作teardown
#     print("登录成功")


# def test_s1(login):
#     print("==用例1==")
#     # 返回的是一个元组
#     print(login)
#     # 分别赋值给不同变量
#     name, pwd, age = login
#     print(name, pwd, age)
#     assert "账号" in name
#     assert "密码" in pwd
#     assert "年龄" in age


# def test_s2(login):
#     print("==用例2==")
#     print(login)

# print(len('qwqwqwqwqwqwqwqwqwqw'))

# import pytest
# @pytest.mark.parametrize(('x','y'),[(1,1),(1,0),(0,1)])
# def test_simple_assume(x,y):
#     print(format('测试数据为{x},{y}'))
#     with assume :assert x==y
#     with assume :assert x+y>1
#     with assume :assert x>1
#     print("测试完成！")
#
# if __name__ =="__main__":
#     pytest.main(['-sv','test_practice.py'])


def test4(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)


test4(1)
test4(1, 1)
test4(1, *(1, 2, 3, 3, 4,))
test4(1, *(1, 2, 3, 3, 4,), cc=123, c=123)

lists = ["a", "b"]
dicts = {"key": 123}
test4(1, *lists, **dicts)




















