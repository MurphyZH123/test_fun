"""
原文链接：https://www.cnblogs.com/poloyy/p/12691240.html

实现方法一、使用命令行重复执行文件中的用例
py.test --count=1000 -x test_file.py(-x强制测试运行程序在第一次失败时停止)




实现方法二、在代码中将某些测试用例标记为执行重复多次
使用@pytest.mark.repeat(count)
@pytest.mark.repeat(5)
def test_repeat():
    print("测试用例执行")



添加覆盖默认的测试用例执行顺序，类似fixture的scope参数
--repeat-scope


"""
