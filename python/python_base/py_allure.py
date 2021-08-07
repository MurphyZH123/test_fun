"""
基本用法
1、安装
pip install allure-pytest
2、官方文档
https://docs.qameta.io/
3、下载
https://dl.bintray.com/qameta/generic/qameta/allure/allure/2.7.0/
4、解压缩
5、进入command
	1、cd 存放allure的目录
	2、sudo mv allure-2.7.0 /usr/local/
	3、cd /usr/local/
	4、ls
	5、cd allure-2.7.0/
	6、ls
	7、cd bin
	8、pwd
	9、拷贝路径
	10、cd ~  #回到桌面
	11、vim .bash_profile
		PATH=$PAtH:/usr/local/allure-2.7.0/bin
		export JAVA_HOME
		export PAtH
12、:wq
13、source .bash_profile

"""

"""
以下是在在命令行中执行

一、执行用例的时候如何生成测试报告(必须在命令行中执行)
1、pwd 查看当前执行路径，进入在项目的根目录中
2、pytest --alluredir ./report testcase/pytest/test08.py
3、allure server ./report 

二、--clean-alluredir 参数，删除之前的测试报告
1、运行第一个测试用例
pytest test_1.py --alluredir=./allure
2、运行第二个测试用例
pytest test_2.py --alluredir=./allure --clean-alluredir
"""

"""
运行项目文件

import os

import pytest

# 创建测试报告目录
reports = os.path.join(os.path.dirname(os.path.abspath(__file__)),'reports')
if not os.path.exists(reports):
    os.mkdir(reports)

if __name__ == '__main__':
    pytest.main(['testcases','-s','-v',f'--alluredir={reports}'])

"""
