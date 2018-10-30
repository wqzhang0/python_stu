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
