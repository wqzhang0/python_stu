import datetime
import json
import logging

import sys

from grpc_microservice.room_server.etcd_server.ietcd.etcd_client import EtcdClient
from grpc_microservice.room_server.etcd_server.load_balance import ProcssBalanceStrategy, FinalBalanceStrategy, \
    BalanceStrategy
from grpc_microservice.room_server.etcd_server.zk_server_content import ServerContent
from grpc_microservice.room_server.meta_cls import Singleton

"""
基于etcd的服务监听
"""
# log = logging.getLogger(__name__)

log = logging.basicConfig(
    level=logging.DEBUG
    , stream=sys.stdout
    , format='%(asctime)s %(pathname)s %(funcName)s%(lineno)d %(levelname)s: %(message)s')


class ServerInspecte(metaclass=Singleton):
    BIZ_PATH = "websocket"
    WEBSOCKET = "server"

    def __init__(self, balance_strategy=None, logger=None):
        if balance_strategy == "ProcssBalanceStrategy":
            self.balance_strategy_cls = ProcssBalanceStrategy()
        elif balance_strategy == "FinalBalanceStrategy":
            self.balance_strategy_cls = FinalBalanceStrategy()
        else:
            self.balance_strategy = BalanceStrategy()
        self._lease = None
        self.provide_server = None
        self.logger = logger or log

    def set_balance_strategy(self, balance_strategy):
        if balance_strategy == "ProcssBalanceStrategy":
            self.balance_strategy_cls = ProcssBalanceStrategy()
        elif balance_strategy == "FinalBalanceStrategy":
            self.balance_strategy_cls = FinalBalanceStrategy()
        else:
            raise Exception('please select a load balancing type in [ProcssBalanceStrategy,FinalBalanceStrategy]')

    def get_server(self):
        return self.balance_strategy_cls.choice(ServerContent.get_list())

    def server_transfer(self):
        """服务转移"""
        self.logger.info("----------------触发服务转移----------------")

    def start(self):
        """开始服务调用接口"""
        self.read_servers()
        self.logger.info("etcd_server 注册中心启动成功")

    def read_state(self):
        for node_name in ServerContent.get_list().keys():
            data = EtcdClient().get_etcd_client().get("/".join([self.BIZ_PATH, self.WEBSOCKET, node_name]))[0].decode(
                "utf-8")
            server_node = json.loads(data)
            ServerContent.get_list()[node_name] = server_node
        print(datetime.datetime.now())

    def read_servers(self):
        """获取服务列表"""
        node_list = EtcdClient().get_etcd_client().get_children("/".join([self.BIZ_PATH, self.WEBSOCKET]),
                                                                watch=self.server_change_listener)

        tmp_server_list = {}
        for node_name in node_list:
            tmp_server_list[node_name] = None
        ServerContent.SERVER_LIST = tmp_server_list
        self.read_state()

    def server_change_listener(self, event):
        # 服务检测  服务注册,节点状态存在延迟
        EtcdClient().get_etcd_client().get_children("/".join([self.BIZ_PATH, self.WEBSOCKET]),
                                                    watch=self.server_change_listener)
        self.read_servers()
        self.server_transfer()

    def choice_grpc_server(self, server_name):
        _server_root = '/GRPC'
        server_name = _server_root + server_name
        _children = EtcdClient().get_etcd_client().get_children(server_name)
        server_node = None
        for i in _children:
            v = EtcdClient().get_etcd_client().get("/".join([server_name, i]))
            server_node = json.loads(str(v[0], encoding='utf-8'))
            break
        if server_node is None:
            raise Exception("没有可用的服务")
        return ":".join([server_node['ip'], server_node['port']]), server_node['uuid']

    def check_lease(self):
        if self._lease is None:
            self._lease = EtcdClient().get_etcd_client().lease(11)
        else:
            remaining_ttl = self._lease.remaining_ttl
            granted_ttl = self._lease.granted_ttl
            if remaining_ttl == -1:
                raise Exception("lease invalid")
    def reset_node(self):
        etcd_client = EtcdClient().get_etcd_client()
        self._lease = etcd_client.lease(10)
        self.register_server()

    def fresh_lease(self):
        pass

    def register_server(self):
        etcd_client = EtcdClient().get_etcd_client()
        _server_root = 'GRPC'
        self._lease = etcd_client.lease(10)
        for k , v in self.provide_server.items():
            etcd_client.put('/{}{}/{}'.format(_server_root,k,v['uuid']),json.dumps(v, ensure_ascii=False),self._lease)

    def add_provide_server(self, _server):
        assert isinstance(_server, dict)
        self.provide_server = _server


if __name__ == '__main__':
    server_inspecte = ServerInspecte(balance_strategy="ProcssBalanceStrategy")
    server_inspecte.start()
    print("启动成功")
