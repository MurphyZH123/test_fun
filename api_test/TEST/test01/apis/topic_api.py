#Python中如何处理接口中上下游关系

#现将每个接口封装成函数
"""
话题相关
"""
import requests
base_url = "http://49.233.108.117:3000/api/v1"

def  create_topic(token,title,tab,content):
	"""
	发布话题
	:param token:用户的唯一token值
	:param title:话题的标题
	:param tab:话题类型
	:param content:话题内容
	:return:
	"""
	url = "http://49.233.108.117:3000/api/v1/topics"
	post_data = {
		"accesstoken":token,
		"title":title,
		"tab":tab,
		"content":content
	}
	return requests.post(url,json = post_data)

def update_topic(token,topic_id,title,tab,content):
	"""
	更新话题
	:param token:用户的唯一token
	:param topic_id:话题的ID
	:param title:话题的标题
	:param tab:话题的类型
	:param content:话题的内容
	:return:
	"""
	url = "http://49.233.108.117:3000/api/v1/topics/update"
	post_data={
		"accesstoken":token,
		"topic_id":topic_id,
		"title":title,
		"tab":tab,
		"content":content
	}
	return requests.post(url,json = post_data)

def topic_detail(topic_id):
	"""
	查看话题详情
	:param topic_id:话题的ID
	:param mdrender:
	:return:
	"""
	url = f"http://49.233.108.117:3000/api/v1/topic/{topic_id}"
	query_data={
		"mdrender":'flase'
	}
	return requests.get(url,params=query_data)

def topic_index_page(page=1,tab="ask",limit=20,mdrender='ture'):
	"""
	主题首页
	:param page:页数
	:param tab:话题类型
	:param limit:话题页面展示条数
	:param mdrender:
	:return:
	"""
	url = base_url+'/topics'
	query_data={
		"page":page,
		"tab":tab,
		"limit":limit,
		"mdrender":mdrender
	}
	return requests.get(url,params = query_data)

def collect_topic(accesstoken,topic_id):
	"""
	收藏话题
	:param accesstoken:token值
	:param topic_id: 话题ID
	:return:
	"""
	url = base_url+'/topic_collect/collect'
	post_data = {
		"accesstoken":accesstoken,
		"topic_id":topic_id
	}
	return requests.post(url,json=post_data)

def de_collect_topic(accesstoken,topic_id):
	"""
	取消收藏话题
	:param accesstoken:token值
	:param topic_id:话题ID
	:return:
	"""
	url = base_url+'/topic_collect/de_collect'
	post_data = {
		"accesstoken":accesstoken,
		"topic_id":topic_id
	}
	return requests.url(url,json = post_data)

def  collect_by_user(loginname):
	"""
	用户收藏的话题
	:param loginname:
	:return:
	"""
	url = base_url+f'/topic_collect/{loginname}'
	return requests.get(url)


def reply_topic(topic_id,accesstoken,content,reply_id=None):
	"""
	回复话题
	:param topic_id:话题ID
	:pranm accesstoken:token值
	:param content:话题内容
	:return:
	"""
	url = base_url+f'/topic/{topic_id}/replies'
	post_data = {
		"accesstoken":accesstoken,
		"content":content
	}
	if not reply_id == None:
		post_data['reply_id']=reply_id
	return requests.post(url,json = post_data)














