#命令行模式启动 nameko shell
# n.rpc.greeting_service.hello("wqzhang")

# 客户端调用方法
from nameko.standalone.rpc import ServiceRpcProxy

def rpc_proxy():
    # the ServiceRpcProxy instance isn't thread safe so we constuct one for
    # each request; a more intelligent solution would be a thread-local or
    # pool of shared proxies
    config = {'AMQP_URI': 'amqp://guest:guest@localhost/'}
    return ServiceRpcProxy('greeting_service', config)

if __name__ == '__main__':
    with rpc_proxy() as _proxy:
         print(_proxy.hello('123'))

