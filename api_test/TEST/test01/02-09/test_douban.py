import pytest
import requests
@pytest.mark.parametrize("tagtype,num",[("最新",20),("热门",20),("冷门佳片",20),("华语",20)])
def test_douban(tagtype,num):
	url = "https://movie.douban.com/j/search_subjects"
	query_data = {
		"type":"movie",
		"tag":tagtype,
		"page_limit":num,
		"page_start":0
	}
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
	}
	res = requests.get(url,params=query_data,headers=headers)
	print(res.json())