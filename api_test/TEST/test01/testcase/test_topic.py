import sys
sys.path.append('/Users/00422829/Desktop/api_test/apis')  
#导入文件
# import apis.topic_api as tapi
# import pytest
#导入具体文件的某个方法或者类
from topic_api import create_topic,collect_topic
def test_collect_topic():
	"""
	测试收藏话题功能
	前提条件是现有话题
	:return:
	"""
	#1.先创建一个话题
	r = create_topic(token='9d8c58bb-b6be-4814-b7ce-ede1b2025738',title='去AAAAA级景区旅游',tab='ask',content='有推荐的景点么')
	#2.获取话题ID
	tid = r.json().get("topic_id")
	#3.收藏话题
	r2 = collect_topic(accesstoken = '9d8c58bb-b6be-4814-b7ce-ede1b2025738',topic_id = tid)
	#添加断言
	assert r.status_code == 200
	assert r.json().get('success') == True
	assert r2.status_code == 200
	assert r2.json().get('success') == True


#sys.path 若是导入模块有误时，输入此命令查看python搜索路径

