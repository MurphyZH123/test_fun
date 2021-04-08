# import pytest
# import requests
# test_data = [
# 	("http://49.233.108.117:3000/api/v1/topics",{"limit":1}),
# 	("http://49.233.108.117:3000/api/v1/topics",{"limit":2})
# ]
# @pytest.mark.parametrize("url,querydata",test_data)
# def test_d(url,querydata):
# 	r = requests.get(url,params = querydata)
# 	#print(f'执行结果：{r.json()}')
# 	print(r.request.url)
# 	print('*'*50)


#使用数据驱动的方式读取json文件实现自动化
import pytest
import requests
import json,os
from jsonschema import validate

test_data = [
	("http://49.233.108.117:3000/api/v1/topics",{"limit":1}),
	("http://49.233.108.117:3000/api/v1/topics",{"limit":2})
]

jsondatafile = os.path.join(os.path.dirname(__file__),'../testdata/test_json.json')


data = json.load(open(jsondatafile,encoding='utf8'))
print(data)
test_json_data = []
for key,value in data.items():
	test_json_data.append((key,value))

print(test_json_data)

@pytest.mark.parametrize("url,querydata",test_data)
def test_d(url,querydata):
	r = requests.get(url,params = querydata)
	#print(f'执行结果:{r,json()}')
	print(r.request.url)
	print('*'*50)

@pytest.mark.parametrize('title,test_data',test_json_data)
def  test_data_from_json(title,test_data:dict):
	print(f'开始执行:{title}')
	request_method = test_data.get('method')
	request_url = test_data.get('url')
	request_data = test_data.get('data')
	res_json_schema = test_data.get('json_schema')
	if request_method == "get":
		r = requests.get(url=request_url,params=request_data)
		validate(instance=r.json(),schema=res_json_schema)
	elif request_method == "post":
		r = requests.post(url=request_url,json=request_data)
		validate(instance=r.json(),schema=res_json_schema)
	print('执行结束')
	




















