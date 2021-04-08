##
# #示例1
# """
# 定义类的基本语法
# class 类名：
#     代码块
# 类名的命名规范使用英文, 首字母大写
# """
# class Person:
#     name = "xiaoming"  # 类变量
#     age = 17


# # 使用类名.类变量的方式来访问
# print(Person.name)

# # 类变量的修改
# Person.name = "Tom"
# print(Person.name)






# ##
# #示例2
# class Person:
# 	name = "xiaoming"
# 	age = 17
# print(Person.name)#使用类名.类变量的方式来访问

# Person.name = "zhangsan"#修改类变量
# print(Person.name) #此时打印出的结果为zhangsan

# #实例化类01
# p1 = Person()
# print(p1.name,p1.age)

# p1.name = "xiaoming"
# p1.age = 20
# print("p1:",p1.name,p1)

# #实例化类02
# p2 = Person()
# print(p2.name,p2.age)

# p2.name = "lisi"
# p2.age = 21
# print("p2:",p2.name,p2.age)






# ##
# #构造器，使用构造器可以为实例化对象的属性赋值
# class Person:
# 	#类中的特殊方法
# 	def __init__(self,a,b):
# 		"""
# 		构造器函数，在实例化类，必须要传入a,b两个参数。
# 		:param a:
# 		:param b:
# 		"""
# 		self.name = a
# 		self.age = b
# 		print('已经生成一个Person实例化对象')
# #实例化对象的时候
# p1 = Person('xiaoming',20)
# print(p1.name,p1.age)

# p2 = Person('zhangsan',21)
# print(p2.name,p2.age)




# ##
# #接口测试的时候，每个接口都有如下3个字段特征：method、url、jsondata
# #创建模型,单个方法
# """
# 创建模拟请求类
# 有基本的三个属性
# method 请求方法
# URL 请求地址
# jsondata 请求地址
# """
# class ApiClient:

# 	def __init__(self,method,url,jsondata=None):
# 		self.method = method
# 		self.url = url
# 		self.jsondata = jsondata

# 	def send(self):
# 		print(f'发送{self.method}请求,请求url{self.url},请求数据:{self.jsondata}')


# api1 = ApiClient('get',"http://49.233.108.117:3000/api/v1/topics")
# api1.send()


# j2data={
# 	'accesstoken':'xxxxxxx',
#     'title':'xxxxx',
#     'tab':'ask',
#     'content':'xxxxxx'
# }
# api2 = ApiClient('get','http://49.233.108.117:3000/api/v1/topics',jsondata=j2data)
# api2.send()



# ##
# #多个方法之间的调用
# class ApiClient:

# 	def __init__(self,method,url,jsondata=None):
# 		self.method = method
# 		self.url = url
# 		self.jsondata = jsondata

# 	def send(self):
# 		print(f'发送{self.method}请求,请求url{self.url},请求数据:{self.jsondata}')
# 		self.result_tree()

# 	def result_tree(self):
# 		print('响应状态码为200，响应数据为{"success":ture}')

# api1 = ApiClient('get',"http://49.233.108.117:3000/api/v1/topics")
# api1.send()


# j2data={
# 	'accesstoken':'xxxxxxx',
#     'title':'xxxxx',
#     'tab':'ask',
#     'content':'xxxxxx'
# }
# api2 = ApiClient('get','http://49.233.108.117:3000/api/v1/topics',jsondata=j2data)
# api2.send()



# ##
# #多个方法之间的调用
# class Iphone:

#     def __init__(self,name,version,color,password):
#         self.name = name   # 手机型号
#         self.version = version  # 系统配置版本
#         self.color = color  # 机身颜色
#         self.password = password # 设置密码
#         print(f'出货一台Iphone: {self.name}, {self.version},{self.color},激活并设置密码 {self.password}')

#     def unlock(self,passwd):
#         # 如果输入进来的密码与设置的密码一致。 解锁成功，进入系统
#         if passwd == self.password:
#             print('解锁成功，进入系统')
#             return True  # 返回True 表示解锁成功
#         else:
#             print('解锁失败')
#             return False # 返回False 表示解锁失败

#     def call(self,nums):
#         print(f'给{nums}打电话。。。')

# iPhone4s = Iphone('iphone4s','8G','black','1234')

# iphone_passwd =input('请输入密码：')


# # 调用unlock方法解锁。将解锁的结果 赋值给变量 isunlock
# isunlock = iPhone4s.unlock(iphone_passwd)  # 如果解锁成功。isunlock 值为True, 否则结果为 False


# # 如果解锁成功 才能调用打电话的方法
# if isunlock:
#     phone_nums = input('请输入电话号码：')
#     iPhone4s.call(phone_nums)
# # 否则需要重试密码
# else:
#     print('重试输入密码')



# ##
# #文档字符串
# class Iphone:

# 	def  __init__(self,name,version,color,password):
# 		"""
# 		Iphone类的构造器，定义一个Iphone实例的属性
# 		:param name: str 手机型号
# 		:param version: str 手机版本
# 		:param color: str 手机颜色
# 		:param password: str 手机激活密码
# 		"""

# 		self.name = name #手机型号
# 		self.version = version #系统配置版本
# 		self.color = color #机身颜色
# 		self.password = password # 设置密码
# 		print(f'出货一台Iphone:{self.name},{self.version},{self.color},激活并设置密码{self.password}')



# 	def unlock(self,passwd):
# 		"""
# 		手机解锁的方法，如果输入进来的密码与设置的密码一致，解锁成功，进入系统
# 		:param passwd:输入进来的密码
# 		:return :Boolean
# 		"""
# 		if passwd == self.password:
# 			print('解锁成功，进入系统')
# 			return True #返回True 表示解锁成功
# 		else:
# 			print('解锁失败')
# 			return False #返回False 表示解锁失败



# 	def  call(self,nums):
# 		"""
# 		拨打电话方法
# 		:param nums:手机号码
# 		:return :
# 		"""
# 		print(f'给{self.nums}'打电话。。。)


# iPhonex = Iphone('iphonex','128G','黑色','1233')
# passwd1 = input('请输入密码:')
# isunlock = unlock(passwd1)
# if isunlock:
# 	phone_nums = input('请输入电话号码:')
# 	iphonex.call(phoen_nums)
# else:
# 	print('请重新输入密码')




# ##
# #输出测试结果
# class TestCase:
# 	"""
# 	创建测试类
# 	"""
# 	def __init__(self,id,title,step,except_result,level,comment=None):
# 		"""
# 		创建类构造器
# 		:param id:编号
# 		:param title:测试用例标题
# 		:param step:测试用例步骤
# 		:param except_result:预期结果
# 		:param level:优先级
# 		:param comment:备注信息
# 		"""
# 		self.id=id
# 		self.title = title
# 		self.step = step
# 		self.except_result = except_result
# 		self.level = level
# 		self.comment = comment

# 	def execute(self):
# 		"""
# 		执行程序
# 		:return:
# 		"""
# 		print(f'正在执行用例{self.id},{self.title}{self.step},{self.except_result},{self.level},{self.comment}')


# t1 = TestCase(1,'用户登录','输入用户名和密码','登录成功','高')
# t2 = TestCase(2,'用户登录','输入错误的用户名和密码','登录失败','高')
# t3 = TestCase(3,'用户登录','输入用户名和错误的密码','登录失败','高')

# for t in t1,t2,t3:
# 	t.execute()





# ##
# #添加执行结果
# import random#导入random
# class TestCase:
# 	"""
# 	创建测试类
# 	"""
# 	def __init__(self,id,title,step,except_result,level,comment=None):
# 		"""
# 		创建类构造器
# 		:param id:编号
# 		:param title:测试用例标题
# 		:param step:测试用例步骤
# 		:param except_result:预期结果
# 		:param level:优先级
# 		:param comment:备注信息
# 		"""
# 		self.id = id
# 		self.title = title
# 		self.step = step
# 		self.except_result = except_result
# 		self.level =level
# 		self.comment = comment



# 	def execute(self):
# 		"""
# 		执行程序
# 		:return:
# 		"""
# 		print(f'正在执行用例{self.id},{self.title}{self.step},{self.except_result},{self.level},{self.comment}')
		
# 		#使用python内置的随机模块，生成一个(0,1)之间随机数字。
# 		n = random.random()
# 		#如果随机大于0.5，假设执行成功
# 		if n>0.5:
# 			print('执行成功')
# 			return True
# 		else:
# 			print('执行失败')


# t1 = TestCase(1,'用户登录','输入用户名和密码',"登录成功","高")
# t2 = TestCase(2,'用户登录','输入错误的用户名和密码',"登录失败","高")
# t3 = TestCase(3,'用户登录','输入用户名和错误密码',"登录失败","高")
# t4 = TestCase(4,'用户登录','输入用户名和错误密码',"登录失败","高")
# t5 = TestCase(5,'用户登录','输入用户名和错误密码',"登录失败","高")


# total = 0 #总执行次数
# success = 0 #成功的次数
# failed = 0 #失败的次数


# for t in t1,t2,t3,t4,t5:
# 	total = total+1#每循环一次，总数增加1.
# 	result = t.execute()#执行完成之后，返回执行结果
# 	#当结果为True 表示执行成功
# 	if result:
# 		success = success + 1#成功的话，success增加1
# 	else:
# 		failed = failed+1#失败的话，failed增加1
# print('测试报告'.center(30,'*'))
# print(f'本次执行总共执行了{total}个测试用例')
# print(f'成功:{success}个')
# print(f'失败:{failed}个')




# class Animal:
# 	def __init__(self,name):
# 		self.name = name

# 	def talk(self,voice):
# 		print(f'{self.name} is talking, using {voice}')
# """
# 子类继承父类
# 会将父类中的构造器和定义的方法继承过来
# """
# class Dog(Animal):
# 	pass

# #实例化Dog
# d1 = Dog('wangcai')
# d1.talk('wofu')#调用父类中的方法



# class Animal:
# 	def __init__(self,name):
# 		self.name = name

# 	def talk(self,voice):
# 		print(f'{self.name} is talking, using {voice}')
# """
# 子类继承父类
# 会将父类中的构造器和定义的方法继承过来
# """
# class Dog(Animal):
# 	def run(self):
# 		print(f'{self.name} is running')

# #实例化Dog
# d1 = Dog('wangcai')
# d1.talk('wofu')#调用父类中的方法
# #调用本类中的方法
# d1.run()

# ##
# #私有，父类中如果有些方法或者属性不希望被子类继承，可以在 属性名 或者 方法名 前边添加 __ 即可
# class Animal:
# 	def __init__(self,name):
# 		self.name = name
# 		self.__secret = "这是一个天大的秘密，只有我知道"

# 	def talk(self,voice):
# 		print(f'{self.name} is talking,using {voice}')

# class Dog(Animal):
# 	pass

# d1 = Dog('ww')
# print(d1.__secret)#私有变量不能被子类继承，所以代码执行会报错。




# ##
# #私有方法，也不能被继承
# class Animal:
# 	def __init__(self,name):
# 		self.name = name
# 		self.__secret = "这是一个天大的秘密，只有我知道"

# 	def talk(self,voice):
# 		print(f'{self.name} is talking')

# 	def __gongfu():
# 		print('这是我的功夫')

# class Dog(Animal):
# 	pass

# d1 = Dog(Animal)
# d1.__gongfu()#父类的私有方法不能被继承，执行会报错




# ## 接口
# #导入 requests
# import requests

# #发送get请求
# r = requests.get("http://49.233.108.117:3000/api/v1/topics")
# #打印状态码
# print(r.status_code)

# #打印服务器响应结果
# print(r.json)


# #导入requests
# import requests

# query = {
# 	"page" : 1,
# 	"tab" : "ask",
# 	"limit" : 1,
# 	"mdrender" : "false"
# }

# #发送get请求
# r = requests.get("http://49.233.108.117:3000/api/v1/topics",params=query) 
# #打印 状态码
# print(r.status_code)

# #打印服务器响应结果
# print(r.json())
# res_json = r.json()
# print(type(res_json))
# #访问data字段值
# print(res_json.get('data'))
# #打印data的长度
# print(len(res_json.get('data')))

# #发送post请求
# import requests
# post_url = 'http://49.233.108.117:3000/api/v1/topics'
# post_data = {
# 	"accesstoken":"",
# 	"title":"今天下小雨哦",
# 	"tab":"ask",
# 	"content":"ahh,雨水是蓝色的哦"
# }
# r = requests.post(url = post_url,data = post_data) 
# print(r.status_code)
# print(r.json)
# #data 参数与json参数的区别

# #查看请求头的信息
# print(r.request.headers)


# #获取access_token
# import requests

# url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
# query_data = {
# 	"corpid":"ww88fc20d87e4cdfa1",
# 	"corpsecret":"gPo9q2e_9qmsDxcGnrPfCzMI9-OHzN3mC_Ut3oVvqAs"
# }
# r = requests.get(url,params = query_data)
# print(r.status_code)
# print(r.request.url)
# print(r.json)

# import requests

# def create_topic(token):
# 	"""
# 	发布话题
# 	:param token:
# 	:return:
# 	"""
# 	url = "http://49.233.108.117:3000/api/v1/topics"
# 	post_data = {
# 		"accesstoken":token,
# 		"title":"helloworld",
# 		"tab":"ask",
# 		"content":"过新年啦"
# 	}
# 	return requests.post(url,post_data)

# def update_topic(token,topic_id):
# 	"""
# 	更新话题
# 	:param token:用户的token
# 	:param topic_id: 话题的id
# 	:return:
# 	"""
# 	url = "http://49.233.108.117:3000/api/v1/topics/update"
# 	post_data = {
# 		"accesstoken":token,
# 		"topic_id":topic_id,
# 		"title":"worldhello",
# 		"tab":"share",
# 		"content":"天气好，吃烧烤"
# 	}
# 	return requests.post(url,json = post_data)
# def topic_detail(topic_id):
# 	"""
# 	查看话题详情
# 	:param topic_id:话题ID
# 	:return:
# 	"""
# 	url = f'http://49.233.108.117:3000/api/v1/topic/{topic_id}'
# 	query_data = {
# 		"mdrender":"false"
# 	}
# 	return requests.get(url,params=query_data)

# if __name__ == '__main__':
# 	token = '6c4f83c6-52a3-4a35-b7f9-f9f8b21403f7'
# 	#创建话题返回的结果
# 	r = create_topic(token)
# 	print(r.status_code)
# 	print(r.json())

# 	#获取创建话题中的topic_id值
# 	res_data = r.json()
# 	topic_id = res_data.get('topic_id')
# 	print(topic_id)

# 	#更新话题
# 	r2 = update_topic(token,topic_id)
# 	print(r2.status_code)
# 	print(r2.json())

	

# #函数的参数
# def myself(name,age,*hobby,**others):
# 	"""
# 	*hobby 可变长度的元组
# 	**others 可变长度的字典
# 	:param name:姓名
# 	:param age:年龄
# 	:param hobby:爱好
# 	:return:
# 	"""
# 	print(f'我的姓名是{name},今年{age}')
# 	print(f'我的爱好是{hobby}')
# 	print(f'其他信息:{others}')

# myself('zhangsan',18)
# myself('lisi',23,'game','reading','money','work')
# myself('wangwu',24,'game','reading','money','work',workyear = 3,goodat = 'apitest')


#处理带cookie的请求
import requests

def get_token():
	url = "http://49.233.108.117:3000/user/refresh_token"
	header ={
		"Cookie":"node_club=s%3A5f4cb4d3c7aa303436a87706%24%24%24%24.Prpcnv4HFHL3Zdlkv5PEHuF2Csn%2F01%2FjIwbQgOXlTwM; connect.sid=s%3AtbiiNPEHOy6cj45tjrlEUxUtkq5mWrwa.jZgDowuuYnDibkbKH2IoG20Kn5TpplFls%2Bs1lzt6W7g"
	}
	return requests.post(url,headers=header)
if __name__ == '__main__':
	r = get_token()
	print(r.status_code)
	print(r.json()) 














