"""
一、强制等待:sleep()
import time
sleep(5)

"""

"""
二、隐式等待
driver.implicitly_wait(10)
隐式等待10秒
"""

"""
三、显示等待：WebDriverWait()
WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
需要通过from selenium.webdriver.support.wait import WebDriverWait导入模块
driver:浏览器驱动
timeout:最长超时时间，默认以秒为单位
poll_frequency:检测的间隔步长，默认为0.5s
ignored_exceptions:超时后的抛出的异常信息，默认抛出NoSuchElementExeception异常

1、与until或者until_not()方法结合使用
WebDriverWait(driver,10).until(method，message="")
调用该方法提供的驱动程序作为参数，直到返回值为True

2、WebDriverWait(driver,10).until_not(method，message="")
调用该方法提供的驱动程序作为参数，直到返回值为False

在设置时间（10s）内，等待后面的条件发生。如果超过设置时间未发生，则抛出异常。
在等待期间，每隔一定时间（默认0.5秒)，调用until或until_not里的方法，直到它返回True或False.


"""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wait = WebDriverWait(driver,10,0.5)
element =wait.until(EC.presence_of_element_located((By.ID,"kw")),message="")




"""
显示等待，自定义等待条件
"""
#设置等待
wait = WebDriverWait(driver,10,0.5)
#使用匿名函数
wait.until(lambda diver:driver.find_element_by_id('kw'))



"""
expected_conditions类提供的预期条件判断的方法
"""






















