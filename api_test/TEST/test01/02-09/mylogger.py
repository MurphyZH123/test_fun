import logging 

#自定义日志对象
import logging

# 自定义日志对象
logger = logging.getLogger("practice")
# 设置日志级别
logger.setLevel(logging.DEBUG)

# 设置日志的格式  asctime 时间   name 名字    levelname 日志级别  message 日志信息
formater = logging.Formatter('[%(asctime)s] - %(name)s  [%(filename)s]- %(levelname)s - %(message)s')

# 设置命令行输出
sh = logging.StreamHandler()
# 为命令行输出设置 显示格式
sh.setFormatter(formater)

# 将命令行输出这个操作添加到自定义日志中
logger.addHandler(sh)
# 定义文件记录日志配置
fh = logging.FileHandler(filename='mylog01',encoding='utf8')
# 配置日志文件记录格式
fh.setFormatter(formater)
# 将文件记录配置存放到自定义logger 中
logger.addHandler(fh)