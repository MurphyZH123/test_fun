import requests
from jsonschema import validate

def test_index_topic():
	#查看主题详情
	url = 'http://49.233.108.117:3000/api/v1/topics'
	query_data = {
		"page":1,
		"tab":"share",
		"limit":2,
		"mdrender":"false"
	}

	#服务器响应结果
	r = requests.get(url,params = query_data)

	#对结果进行验证
	#1.1 状态码应该为200
	assert r.status_code == 200

	#1.2 limit = 1 返回结果应该为1条数据
	rejson = r.json()
	print('服务器响应结果',rejson)
	#返回数据中的data字段长度应该为入参中的limit字段
	assert len(rejson.get('data')) == query_data.get('limit')

	#1.3 tab值进行断言
	res_data = rejson.get('data')
	for obj in res_data:
		print('获取到的数据',obj)
		print('*'*40)
		#每一个话题的tab值都应该为入参中的tab值
		assert obj['tab'] == query_data.get('tab')

def test_topic_schema():
	#发布话题
	url = 'http://49.233.108.117:3000/api/v1/topics'
	post_data = {
		"accesstoken":" ",
		"title":"气温过山车",
		"tab":"share",
		"content":"有推荐的好去处么"
	}
	r = requests.post(url,post_data)

	#实际运行结果
	jsondata = r.json()

	#使用schema描述数据的结果
	schema = {
		"type":"object",
		"properties":{
			"success":{"type":"boolean"},
			"topic_id":{"type":"string"}
		}
	}
	#使用jsonschema中提供的validata方法对结果进行验证
	validate(instance = jsondata,schema = schema)
























