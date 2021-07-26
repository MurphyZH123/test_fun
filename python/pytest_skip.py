"""
原文链接https://cloud.tencent.com/developer/article/1554027
一、skips介绍及运用
在我们自动化测试过程中，经常会遇到功能阻塞、功能未实现、环境等一系列外部因素问题导致的一些用例执行不了
这时我们就可以用到skip用例，如果我们注释掉或删除掉，后面还要进行恢复操作
1、skip跳过成功，标识为s  ============================= 2 skipped in 0.04s ==============================

2、pytest.main(['-rs','test01.py']) 用-rs执行，跳过原因才会显示SKIPPED [1] test01.py:415: 跳过Test类，会跳过类中所有方法

3、skip跳过，无条件和原因@pytest.mark.skipif()

4、skip跳过，无需满足条件true、有跳过原因@pytest.mark.skipif(reason='无条件，只有跳过原因')

5、skip跳过，需满足条件true、且有跳过原因@pytest.mark.skipif(条件1==1,reason='跳过原因')

6、skip赋值变量，多处调用myskip=pytest.mark.skipif(1==1,reason='skip赋值给变量，可多处调用')

然后@myskip使用
"""


"""
二、@pytest.mark.skip()和@pytest.mark.skipif()两个标签，用他们装饰测试类

1、被标记的类中所有方法测试用例都会被跳过

2、被标记的类，当条件为ture时，会被跳过，否则不跳过
"""
#skip跳过类
import pytest,sys
@pytest.mark.skip(reason='跳过Test类，会跳过类中所有方法')
class Test(object):
	def test_one(self):
		assert 1==1
	def test_two(self):
		assert 1==2

if __name__=='__main__':
	pytest.main(['-rs','test01.py'])

 
#skip满足条件，skip跳过类
import pytest,sys
@pytest.mark.skipif(1==1,reason='跳过Test类，会跳过类中所有方法')
class Test(object):
    def test_one(self):
        assert 1==1
    def test_two(self):
        print('test_02')
        assert 1==2
if __name__=='__main__':
    pytest.main(['-rs','test01.py'])



"""
三、我们想要某个方法或跳过某条用例，在方法上加以下3种都可以

@pytest.mark.skip() #1、跳过方法或用例，未备注原因

@pytest.mark.skip(reason='跳过一个方法或一个测试用例') #2、跳过方法或用例，备注了原因

@pytest.mark.skipif(1==1,reason='跳过一个方法或一个测试用例')   #3、当条件满足，跳过方法或用例，备注了原因
"""
#1、跳过方法或用例，未备注原因
import pytest,sys
class Test(object):
    @pytest.mark.skip()
    def test_one(self):
        assert 1==2
    def test_two(self):
        print('test_02')
        assert 1==1
if __name__=='__main__':
    pytest.main(['-rs','test01.py'])

#2、跳过方法或用例，备注了原因
import pytest,sys
class Test(object):
    @pytest.mark.skip(reason='跳过一个方法或一个测试用例')
    def test_one(self):
        assert 1==2
    def test_two(self):
        print('test_02')
        assert 1==1
if __name__=='__main__':
    pytest.main(['-rs','test01.py'])

 
#3、当条件满足，跳过方法或用例，备注了原因
import pytest,sys
class Test(object):
    @pytest.mark.skipif(1==1,reason='跳过一个方法或一个测试用例')
    def test_one(self):
        assert 1==2
    def test_two(self):
        print('test_02')
        assert 1==1
if __name__=='__main__':
    pytest.main(['-rs','test01.py'])


"""
四、多个skip时，满足1个条件即跳过

我们在类和方法上分别加了skip，类中满足条件，方法中未满足条件，所以生效类中skip
"""
import pytest,sys
@pytest.mark.skipif(1==1,reason='多个条件时，有1个条件满足就跳过(类)')
class Test(object):
    @pytest.mark.skipif(1==2, reason='多个条件时，有1个条件满足就跳过(方法)')
    def test_one(self):
        assert 1==2
    def test_two(self):
        print('test_02')
        assert 1==1
if __name__=='__main__':
    pytest.main(['-rs','test01.py'])


"""
五、无论是@pytest.mark.skip()标签还是@pytest.mark.skipif()标签，如果你想在多个测试方法上装饰，
依次写起来很麻烦的话，你可以选择定义个变量让它等于标签，然后在装饰的时候用该变量代替标签。
这种方法，你还可以通过在其他模块中导入的变量的方式，在其他模块中共享标签；
如果可以这样的话，我们为什么不新建一个模块用来存放标签呢？这样是不是又方便了许多。

赋值：myskip=pytest.mark.skipif(1==1,reason='skip赋值给变量，可多处调用')

调用：@myskip

"""
import pytest,sys
myskip=pytest.mark.skipif(1==1,reason='skip赋值给变量，可多处调用')
class Test(object):
    @myskip
    def test_one(self):
        assert 1==2
    def test_two(self):
        print('test_02')
        assert 1==1
if __name__=='__main__':
    pytest.main(['-rs','test01.py'])



"""
六、pytest.skip()方法内跳过

除了通过使用标签的方式，还可以在测试用例中调用pytest.skip()方法来实现跳过，可以选择传入msg参数来说明跳过原因；
如果想要通过判断是否跳过，可以写在if判断里（_）
"""
import pytest,sys
class Test(object):
    def test_one(self):
        pytest.skip(msg='跳过')
        assert 1==2
    def test_two(self):
        print('test_02')
        assert 1==1
if __name__=='__main__':
    pytest.main(['-rs','test01.py'])

















