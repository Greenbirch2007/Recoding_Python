# 第11章 网络和web编程
# 11.1  以客户端的形式同http服务交互
# 11.1.1 问题
# 我们需要以客户端的形式通过http协议访问多种服务。比如下载数据或同一个基于rest的api进行交互
# 11.1.2  解决方案
# 对于简单的任务来说，使用urllib.request模块通常就足够，了

from urllib3 import request,parse

# 直接使用requsts库
import requests

url = 'http://httpbin.org/post'
parms = {
    'name1':'value1',
    'name2':'value2'
}

headers = {
    'User-agent':'none/ofyourbusiness',
    'Spam':'Eggs'
}

resp = requests.post(url,data=parms,headers=headers)
# requests库可以多种方式从请请求中返回响应结果的内容。resp.text带给我们的是以unicode解码的响应文本。如果是resp.content,就会得到
# 原始的二进制数据，resp.json基金会的到json格式的响应