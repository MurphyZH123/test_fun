"""
原文链接：https://www.cnblogs.com/poloyy/p/12687308.html

环境前提：python3.5以上，pytest5.0以上

安装插件：pip3 install pytest-rerunfailures -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

命令行参数：--returns n (重新运行次数) ， --returns-delay m (等待运行秒数)
装饰器参数：return=n(重新运行次数)，returns_delay=m(等待运行秒数)
