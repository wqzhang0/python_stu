# rpc_server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server

import time


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print("start")
    time.sleep(20)
    print("end")

    return [b'<h1>Hello, web!</h1>']

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()