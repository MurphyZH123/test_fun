"""
封装Logzero类地址:https://www.cnblogs.com/poloyy/p/12324024.html
"""


import logging
import logzero
from logzero import logger

class Logzero(object):
	__instance = None

	def __new__(cls,*args,**kwargs):
		if not cls.__instance:
			cls.__instance = object.__new__(cls,*args,**kwargs)
		return cls.__instance

	def __init__(self):
		self.logger = logger

		#console控制台输入日志格式 - 带颜色
		self.console_format = '%(color)s'\
								'[%(asctime)s]-[%(levelname)1.1s]-[%(filename)s]-[%(funcName)s:%(lineno)d] 日志信息: %(message)s ' \
								'%(end_color)s'

		#创建一个Formatter对象
		self.formater = logzero.LogFormatter(fmt=self.console_format)

		#将formatter提供给setup_default_logger方法的formatter参数
		logzero.setup_default_logger(formatter=self.formatter

		#设置日志文件输出格式
		self.formmater =logging.Formatter(
			'[%(asctime)s]-[%(levename)s]-[%(filename)s]-[%(funcName)s:%(lineno)d]日志信息: %(message)s')

		#设置日志文件等级
		logzero.loglevel(logging.DEBUG)

		#输出日志文件路径和格式
		logzero.logfile('F:\\imocInterface\\log/tests.log", formatter=self.formater')

		#输出日志格式为json格式
		logzero.json()



	def debug(self,msg):
		self.logger.debug(msg = msg)


	def info(self,msg):
		self.logger.info(msg = msg)


	def warning(self,msg):
		self.logger.warning(msg = msg)

	def error(self,msg):
		self.logger.error(msg = msg)

	def exception(self,msg):
		self.logger.exception(msg = msg)


logzero = Logzero()


if __name__ == "__main__":
	logzero.debug("debug")
	logzero.info("info")
	logzero.warning("warning")
	logzero.error("error")
	a = 5
	b = 0
	try:
		c = a/b
	except Exception as e:
		logzero.exception("Exception occurred")



"""
logzero原文文档地址:https://logzero.readthedocs.io/en/latest/

"""





















