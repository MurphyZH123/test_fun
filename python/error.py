
import sys
try:
    f = open('file.txt', 'r')
    # some data processing
except OSError as err:
    print('OS error: {}'.format(err))
except:
    print('Unexpected error:', sys.exc_info()[0])
finally:
    print('获取文档结束')




class MyInputError(Exception):
    """Exception raised when there're errors in input"""
    def __init__(self, value): # 自定义异常类型的初始化
        self.value = value
    def __str__(self): # 自定义异常类型的string表达形式
        return ("{} is invalid input".format(repr(self.value)))
    
try:
    raise MyInputError(1) # 抛出MyInputError这个异常
except MyInputError as err:
    print('error: {}'.format(err))



#两个书写异常的代码对比简洁程度

"""
第一种代码简洁程度比第二种要好，
当程序中存在多个 except block 时，
最多只有一个 except block 会被执行。
换句话说，
如果多个 except 声明的异常类型都与实际相匹配，
那么只有最前面的 except block 会被执行，其他则被忽略。
"""
#第一种
try:
    db = DB.connect('<db path>') # 可能会抛出异常
    raw_data = DB.queryData('<viewer_id>') # 可能会抛出异常
except (DBConnectionError,DBQueryDataError) err:
    print('Error: {}'.format(err))


#第二种
try:
    db = DB.connect('<db path>') # 可能会抛出异常
    try:
        raw_data = DB.queryData('<viewer_id>')
    except DBQueryDataError as err:
         print('DB query data error: {}'.format(err))
except DBConnectionError as err:
     print('DB connection error: {}'.format(err))






