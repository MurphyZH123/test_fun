import requests
from mylogger import logger
"""
封装自定义请求类
"""
class Client:
    def __init__(self,url,method):
        # 请求路径
        self.url = url
        # 请求方法
        self.method = method

    def handler_request(self,params=None,data=None, json=None, **kwargs):
        if self.method == 'get':
            logger.debug(f"发送get请求,请求路径:{self.url},请求参数:{params},{kwargs}")
            r = requests.get(url=self.url,params=params,**kwargs)
            logger.debug(f'请求结束,结果为{r.status_code},{r.text}')
            return r
        elif self.method == "post":
            logger.debug(f"发送post请求,请求路径:{self.url},请求参数:{data},{json},{kwargs}")
            r = requests.post(url=self.url, data=data, json=json, **kwargs)
            logger.debug(f'请求结束,结果为{r.status_code},{r.text}')
            return r