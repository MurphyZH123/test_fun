"""
定义要执行的测试用例集
"""
import pytest

# 冒烟测试
def smoke_test():
    # 运行包含 test_m 的测试用例  -v 显示详细的执行结果
    pytest.main(['-k','test_m','-v'])



if __name__ == '__main__':
    smoke_test()
