
#01基本日志操作
# import logging
# #配置日志级别为debug 写入文件，文件权限为追加。
# logging.basicConfig(level =logging.DEBUG,filename='example.log',filemode='a')

# logging.debug("this is debug")
# logging.info("this is info")
# logging.warning("this is warning")
# logging.error("this is error")




# #02自定义日志
# import logging

# #自定义日志对象
# logger = logging.getLogger("practice")
# #设置日志级别
# logger.setLevel(logging.DEBUG)

# #设置日志格式  asctime 时间，name 名字，levelname 日志级别，message 日志信息
# formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s' )

# #设置命令行输出
# sh = logging.StreamHandler()

# #为命令行输出设置 显示格式
# sh.setFormatter(formater)

# #将命令行输出这个操作添加到自定义日志中
# logger.addHandler(sh)

# logger.debug('debug message')


#03创建一个既可以记录日志到文件，同时有了一讲日志输出到命令行的方式
import logging

#自定义日志对象
logger = logging.getLogger("practice")
#设置日志的级别
logger.setLevel(logging.DEBUG)

#设置日志格式
formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#设置命令行输出
sh = logging.StreamHandler()

#为命令行输出设置 显示格式
sh.setFormatter(formater)

#将命令行输出这个操作添加到自定义日志中
logger.addHandler(sh)

#定义文件记录日志配置
fh = logging.FileHandler(filename = 'mylog',encoding = 'utf8')

#配置日志文件记录格式
fh.setFormatter(formater)

#将文件记录配置存放到自定义logger中
logger.addHandler(fh)

logger.debug('debug message')




























