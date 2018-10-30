import random


class BalanceStrategy():
    """负载均衡策略"""

    @classmethod
    def choice(self, server_list):
        # 随便获取一个节点做匹配
        node = random.choice(list(server_list.keys()))
        if node is None:
            return BalanceStrategy.choice(server_list)
        else:
            return node


class ProcssBalanceStrategy(BalanceStrategy):
    """过程负载均衡策略"""


class Director(object):

    def __init__(self) -> None:
        self.builder = None
class Builder(object):

    def __init__(self) -> None:
        self.building = None
    def new_building(self):
        self.building =  Building()

class Building(object):

    def __init__(self) -> None:
        self.floor = None
        self.size = None

    def __repr__(self):
        print('dict')


class Customize():


    def __init__(self) -> None:
        self.builder = None

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building

    def build_debug(self,is_debug):
        """
        指定环境
        """
        pass
    def build_choice_uuid(self,uuid):
        """
        指定uuid
        """
        pass
    def build_choice_point(self,uuid):
        """
        选择端点 ip port
        """
        pass
    def build_version(self,uuid):
        """
        创建版本
        """
        pass
    def build_env(self,online):
        """
        创建环境
        """
        pass

class TT():

    @classmethod
    def choice(self, server_list):
        pass

    def select_by_uuid(self,):
        assert self.env == 'deve'

    # self.env = False
    #
    # def select():
    #     if self.env == 'deve':


class FinalBalanceStrategy():
    """最终负载均衡策略"""

    @classmethod
    def choice(self, server_list):
        # 优先获取少的
        online_player = [{'websocket_path': v['websocket_path'], 'online_num': v['online_num'], 'server_node': k} for
                         k, v in
                         server_list.items() if v is not None]
        online_player.sort(key=lambda x: x['online_num'])
        if len(online_player) == 0:
            print("没有服务节点 重新选择")
            return self.choice(server_list)
        node = online_player[0]
        if node is None:
            return self.choice(server_list)
        else:
            return node['server_node']
