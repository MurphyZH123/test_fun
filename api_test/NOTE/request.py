


"""
python3做multipart/form-data上传请求

http协议本身的原始方法不支持multipart/form-data请求,这个请求由原始方法演变而来的。
multipart/form-data的基础方法是post,也就是说是由post方法来组合实现的
请求头必须包含一个特殊的头信息:Content-Type,必须为multipart/form-data,同时还一个内容分割符 (boundary) 用于分割请求体中的多个post的内容。
因为接收方解析和还原文件必须要根据这个boundary。
"""
#具体的头信息必须包含如下设置
{"Content-Type": "multipart/form-data; boundary=${bound}"}


##以下是例子
import os, random, sys, requests 
from requests_toolbelt.multipart.encoder import MultipartEncoder 
#请求地址
url = 'http://192.168.1.48' 

#头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0', 
    'Referer': url 
}

#路径 
file = 'D:\\test\上传测试.doc'    
multipart_encoder = MultipartEncoder(
    fields = {
      #这里根据服务器需要的参数格式进行修改
            'params': json.dumps({
            'folderId':-100,
            'type':'onlinedisk',
            'name':'5106024f8a22422172bd88d455be48a0.gif',
            'size':16043,
            'md5':'57c1a6348e35d4f86ed4d520da8e1dc2',
            'ignoreSame':false,
            'autoRename':false,
            'startPosition':0,
            'blockMd5':'57c1a6348e35d4f86ed4d520da8e1dc2',
            'blockSize':16043,
            'quickVerifyCode':'3c91184c5c91e13a60ebbf144f13783c',
            'repaire':false
        }),
        'file': ('file', open(file, 'rb'), 'application/octet-stream')
    },
    boundary=boundary
)
headers['Content-Type'] = multipart_encoder.content_type
#请求头必须包含一个特殊的头信息,类似于Content-Type: multipart/form-data; boundary=${bound}
#注意：这里请求头也可以自己设置Content-Type信息，用于自定义boundary
r = requests.post(url, data=multipart_encoder, headers=headers)
print(r.text)
#注意,不要设置cookies等其他参数,否则会报错






"""

 To check that a request is successful, use r.raise_for_status() or check r.status_code is what you expect.
request官方网址https://requests.readthedocs.io/en/master/user/quickstart/#make-a-request


 """




 """
 请求状态码为415时，表示请求的格式不符合要求
 """














 