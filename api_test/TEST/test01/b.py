import a #导入a模块 module
import apis.user_api as api #导入包与模块路径 as 起别名

#调用a模块中的f1()
a.f1()

#通过别名来访问
api.check_token(1)