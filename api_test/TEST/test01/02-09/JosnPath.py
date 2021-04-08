#列表推导式
#jsonpath的使用https://blog.csdn.net/fy_1852003327/article/details/106645204
test_array = [i for i in range(2)]
print(test_array)

from jsonpath_ng import parse
import requests
test_json = {
	"books":[
		{
		"title":"python学习手册",
		"price":35.00
		},
		{
		"title":"java学习手册",
		"price":40.00
		}
	]
}

#使用jsonpath_ng提供的功能解析字符串（要找到的数据）
expr = parse('books[*].title')

#从test_json中根绝上边提供的表达式查找数据
data = [match.value for match in expr.find(test_json)]
print(data)


def test_jsonpath_ng():
	url = "http://49.233.108.117:3000/api/v1/topics"
	query_data = {
		"page":	1,
		"tab":"ask",
		"limit":10,
		"mdrender":"flase"
	}
	r = requests.get(url=url,params = query_data)

	#服务器返回的结果
	result_data = r.json()
	#打印返回的结果
	expr = parse("$.data[*].title")
	find_value = [match.value for match in expr.find(result_data)]
	print(find_value)

	#断言返回结果的条数
	assert len(find_value) == query_data.get('limit')



	expr1 = parse("$.data[*].tab")
	find_value1 = [match.value for match in expr1.find(result_data)]
	print(find_value1)
	assert ["ask" for i in range(10)] == find_value1
test_jsonpath_ng()






















