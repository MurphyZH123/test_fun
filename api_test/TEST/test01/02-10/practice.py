 import requests
 class RequestsHandler:
 	def __init__(self):
 		"""
 		session管理器
 		"""
 		self.session=requests.session()
 	def visit(self,method,url,params=None,data=None,json=None,headers=None,**kwargs):
 		return self.seesion.request(self,method,url,params=None,data=None,json=None,headers=None,**kwargs)
 	def close_session(self):
 		"""
 		关闭session
 		"""
 		self.session.close()
if __name__ == '__main__':
	
 		