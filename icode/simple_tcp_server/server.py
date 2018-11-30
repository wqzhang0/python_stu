import socket

# 创建服务端的socket对象socketserver
import os

socketserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9092
# 绑定地址（包括ip地址会端口号）
socketserver.bind((host, port))
# 设置监听
socketserver.listen(5)
# 等待客户端的连接
# 注意：accept()函数会返回一个元组
# 元素1为客户端的socket对象，元素2为客户端的地址(ip地址，端口号)


while True:
    clientsocket, addr = socketserver.accept()  # 接收连接
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

    print("Connected by", addr)
    while True:
        try:
            data = clientsocket.recv(1024)
            if not data:
                break
            print(str(pid) + "-------Received", data)
            clientsocket.send((str(pid) + "test msg").encode("utf-8"))

        except socket.error:
            break
    clientsocket.close()
