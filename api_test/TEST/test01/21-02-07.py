# import os,sys
# sys.path.append(os.getcwd())  
# #导入文件
# # import apis.topic_api as tapi
# # import pytest
# #导入具体文件的某个方法或者类
# from apis.topic_api import create_topic,collect_topic
# def test_collect_topic():
# 	"""
# 	测试收藏话题功能
# 	前提条件是现有话题
# 	:return:
# 	"""
# 	#1.先创建一个话题
# 	r = create_topic(token='',title='去AAAAA级景区旅游',tab='ask',content='有推荐的景点么')
# 	#2.获取话题ID
# 	tid = r.json().get("topic_id")
# 	#3.收藏话题
# 	r2 = collect_topic(accesstoken = '',topic_id = tid)
# 	#添加断言
# 	assert r.status_code == 200
# 	assert r.json().get('success') == True
# 	assert r2.status_code == 200
# 	assert r2.json().get('success') == True



# #发送get请求
# import requests
# import json
# import pprint

# query_data = {
# 	"page":1,
# 	"tab":"ask",
# 	"limit":1,
# 	"mdrender":"flase"
# }
# url = "http://49.233.108.117:3000/api/v1/topics"
# requests.post()
# try:
# 	r=requests.get(url,json=query_data)
# 	print(r.status_code)
# 	pp = pprint.PrettyPrinter(indent = 2)
# 	pp.pprint(r.json())
# except Exception:
# 	print('程序在执行的过程中出现了异常')


{
	"主题首页":{
		"method":"get",
		"url":"http://49.233.108.117:3000/api/v1/topics",
		"data":{
			"page":1,
			"tab":"ask",
			"limit":1,
			"mdrender":"flase"
		}
	},
	"发布话题":{
		"method":"post"
		"url":"http://49.233.108.117:3000/api/v1/topics",
		"data"={
			"accesstoken":" ",
			"title":"一起去追风啊",
			"tab":"ask",
			"content":"追风可还行"
		}
	}
}

import json
import requests
#加载测试文件数据
test_data:dict = json.load(open('test_data.json',encoding='utf-8'))


for test_title,test_content in test_data.items():
	print(f'开始测试:{test_title}')
	print(f'测试信息:{test_content}')
	print(f'{test_content.get("method")}')

	#获取字典中method字段值
	method = test_content.get('method')#获取json中的value值的method字段
	url = test_content.get('url')#获取json中的value值的url字段
	data = test_content.get('data')#获取json中的value值的data值

	#如果数据中请求方法为get
	if method == 'get':
		r = requests.get(url = url,params = data)
	elif method == 'post':
		r = requests.post(url = url,json = data)



	#打印服务器响应结果
	print(f'响应状态码:{r.status_code}')
	print(f'响应结果:{r.json()}')
	















