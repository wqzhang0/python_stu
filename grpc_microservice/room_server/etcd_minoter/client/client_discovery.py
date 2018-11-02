import json
import logging
import pprint
import threading
from functools import wraps

import grpc
from etcd3.events import PutEvent, DeleteEvent

from grpc_microservice.room_server.etcd_minoter.client.load_balance import ProcssBalanceStrategy, FinalBalanceStrategy, \
    BalanceStrategy
from grpc_microservice.room_server.etcd_minoter.etcd_manager import EtcdServer
from grpc_microservice.room_server.etcd_minoter.zk_server_content import ServerContent
from grpc_microservice.room_server.meta_cls import Singleton
from grpc_microservice.smart_client import header_manipulator_client_interceptor


def choose_address(server_name, **kwargs):
    """
    选择所连接的服务地址 这里预留接口
    """
    return ServerDiscovery().choice_grpc_server(server_name, **kwargs)
    # return '127.0.0.1:50002' ,'token'


def proxy_grpc_func(stub, module_name):
    _stub = stub
    _module_name = module_name

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            _func = func.__name__
            _point, _token = choose_address('/{}/{}/'.format(_module_name, _func), **kwargs)
            #
            header_adder_interceptor = header_manipulator_client_interceptor.server_access_interceptor(_token)
            with grpc.insecure_channel(_point) as channel:
                intercept_channel = grpc.intercept_channel(channel, header_adder_interceptor)
                __stub = _stub(intercept_channel)
                _func_stub = getattr(__stub, _func)
                ret = _func_stub(args[1])
                return ret

        return wrapper

    return decorate


class ServerDiscovery(EtcdServer, metaclass=Singleton):
    log = logging.getLogger(__name__)

    def __init__(self, balance_strategy=None, logger=None):
        super().__init__(logger)
        if balance_strategy == "ProcssBalanceStrategy":
            self.balance_strategy = ProcssBalanceStrategy()
        elif balance_strategy == "FinalBalanceStrategy":
            self.balance_strategy = FinalBalanceStrategy()
        else:
            self.balance_strategy = BalanceStrategy()
        self.server_colletion = {}
        self.logger = logger or self.log
        self.pro = True  # debug False

    def set_balance_strategy(self, balance_strategy):
        if balance_strategy == "ProcssBalanceStrategy":
            self.balance_strategy_cls = ProcssBalanceStrategy()
        elif balance_strategy == "FinalBalanceStrategy":
            self.balance_strategy_cls = FinalBalanceStrategy()
        else:
            raise Exception('please select a load balancing type in [ProcssBalanceStrategy,FinalBalanceStrategy]')

    def start(self):
        """开始服务调用接口"""
        self.read_servers()
        self.logger.info("etcd_minoter 注册中心启动成功")
        t = threading.Thread(target=self.loop, name='LoopThread')
        t.start()

    def loop(self):
        # 进行监听
        events_iterator, cancel = self.etcd_client.watch_prefix(self.ROOT)
        for event in events_iterator:
            self.logger.info("刷新服务开始")
            print(event.key)
            if isinstance(event, PutEvent):
                print(str(event.value, encoding='utf-8'))
                print('放入')
            elif isinstance(event, DeleteEvent):
                print('删除')

    def tran_s(self):
        self.__normal_server = {}
        self.__force_server = {}
        _server_colletion = self.server_colletion

        for _uuid, _server_info in _server_colletion.items():

            _path = _uuid.split('/')
            _module = _path[1]
            _api = _path[2]
            _uuid = '/{}/{}'.format(_module,_api)
            # 过滤下线接口
            if _server_info['pro'] != self.pro or _server_info['offline']:
                continue
            # 如果有强制调用的接口
            if _server_info['force']:
                _force_server = self.__force_server.get(_uuid, [])
                _force_server.append(_server_info['uuid'])
                self.__force_server[_uuid] = _force_server
            _normal_server = self.__normal_server.get(_uuid, [])
            _normal_server.append(_server_info['uuid'])
            self.__normal_server[_uuid] = _normal_server

    def filter_foce(self, server_name):
        server_pool = self.__force_server.get(server_name)
        if server_pool and len(server_pool) > 0:
            return server_pool
        server_pool = self.__normal_server.get(server_name)
        if server_pool and len(server_pool) > 0:
            return server_pool
        raise Exception('no server can user')

    def read_servers(self):
        """获取服务列表"""
        self.server_colletion = {}
        childrens = self.etcd_client.get_prefix(self.ROOT)
        for value, _meta in childrens:
            _v = value.decode("utf-8")
            _path = _meta.key.decode("utf-8").replace('/GRPC', '').split('/')
            _module = _path[1]
            _api = _path[2]
            _server_uuid = _path[3]
            _server_info = json.loads(_v, encoding='utf-8')
            _server_info['_module'] = _module
            _server_info['_api'] = _api
            _server_name = '/{}/{}/{}'.format(_module, _api, _server_uuid)

            # __server_infos = self.server_colletion.get(_server_name, [])
            # __server_infos.append(_server_info)
            self.server_colletion[_server_name] = _server_info

    def get_point(self, server_name,server_key):
        server_node = self.server_colletion[server_name+'/'+server_key]
        return ":".join([server_node['ip'], server_node['port']])

    def choice_grpc_server(self, server_name, **kwargs):
        return self.get_point(server_name,self.balance_strategy.choice(self.filter_foce(server_name), **kwargs))

    def get_server(self):
        return self.balance_strategy_cls.choice(ServerContent.get_list())

    def designation_point(self, ):
        """
        指定服务端点
        """
        # 测试环境分为是否需要验证
        # force 被强制调用，选项 IP：port / uuid
        pass

    # 生产环境只开放生产环境的服务 offline

    # 如果无 唯一调用 选择时 根据规则 权重 进行分配 否则选择强制调用


if __name__ == '__main__':
    server_inspecte = ServerDiscovery(balance_strategy="ProcssBalanceStrategy")
    server_inspecte.start()
    server_inspecte.tran_s()
    node_info = server_inspecte.choice_grpc_server('/RoomServer/CreateRoom')
    print(node_info)
    print("启动成功")
