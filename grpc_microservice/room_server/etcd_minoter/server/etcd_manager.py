import json
import logging
import threading

import etcd3
import time

from etcd3.exceptions import Etcd3Exception

from grpc_microservice.room_server.meta_cls import Singleton

"""
基于etcd的服务监听
"""


class EtcdServer(metaclass=Singleton):
    log = logging.getLogger(__name__)

    def __init__(self, logger=None):
        self.logger = logger or self.log
        self.ROOT = '/GRPC'
        self.etcd_client = etcd3.client()


class LeaseInvide(Exception):
    """
    节点无效
    """
    pass


class ServerInspecte(EtcdServer, metaclass=Singleton):
    log = logging.getLogger(__name__)

    def __init__(self, logger=None, env='production'):
        super().__init__(logger)
        self._lease = None
        self.provide_server = None
        self.logger = logger or self.log
        self.env = env  # debug

    def start(self):
        """开始服务调用接口"""
        self.logger.info("etcd_minoter 注册中心启动成功")
        self.register_server()

        t = threading.Thread(target=self.loop, name='LoopThread')
        t.start()

    def loop(self):
        while True:
            self.logger.info("刷新服务开始")
            try:
                granted_ttl, remaining_ttl = self.fresh_lease()
                next_flush_time = int(granted_ttl / 3 * 2)
                time.sleep(next_flush_time)
            except LeaseInvide:
                self.register_server()
            except Etcd3Exception as e:
                self.logger.info("刷新服务 异常", e)
                time.sleep(3)

    def register_server(self):
        """
        注册服务
        """
        self._lease = self.etcd_client.lease(10)
        if (not self.provide_server) or (not isinstance(self.provide_server, dict)):
            self.logger.info('没有服务可以进行注册，请检查。如果是初始化阶段请忽略')
        else:
            for k, v in self.provide_server.items():
                self.etcd_client.put('{}{}/{}'.format(self.ROOT, k, v['uuid']), json.dumps(v, ensure_ascii=False),
                                     self._lease)

    def add_provide_server(self, _server):
        """
        增加要注册的服务
        """
        assert isinstance(_server, dict)
        self.provide_server = _server

    def fresh_lease(self):
        """
        检查lease 是否活跃
        """
        if self._lease is None:
            raise LeaseInvide("无lease")
        else:
            print(self._lease.remaining_ttl)

            self._lease.refresh()
            self.logger.info('刷新节点')

            remaining_ttl = self._lease.remaining_ttl
            granted_ttl = self._lease.granted_ttl
            if remaining_ttl == -1:
                raise LeaseInvide("lease invalid")

            return granted_ttl, remaining_ttl


if __name__ == '__main__':
    # log = logging.basicConfig(
    #     level=logging.DEBUG
    #     , stream=sys.stdout
    #     , format='%(asctime)s %(pathname)s %(funcName)s%(lineno)d %(levelname)s: %(message)s')

    # server_inspecte = ServerInspecte(log)
    # server_inspecte = ServerInspecte(log)
    # server_inspecte = ServerInspecte(log)
    # server_inspecte.start()
    print("启动成功")
