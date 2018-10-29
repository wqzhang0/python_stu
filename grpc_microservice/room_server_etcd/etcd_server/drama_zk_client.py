import time

import etcd3

from grpc_microservice.room_server_etcd.common_cls import Singleton

"""
etcd_server 客户端集成类
"""
class EtcdClient(metaclass=Singleton):

    def __init__(self) -> None:
        super().__init__()
        self.etcd_client =    etcd3.client()


    def get_etcd_client(self):
        """这里加异常捕捉 防止本服务不可以用"""
        return self.etcd_client
