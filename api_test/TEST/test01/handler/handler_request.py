# -*- coding: utf-8 -*-
import json
import requests
#加载测试文件数据
test_data:dict = json.load(open('../test_data/test_data.json',encoding='utf8'))


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
