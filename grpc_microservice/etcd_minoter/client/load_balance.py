import random


class BalanceStrategy():
    """负载均衡策略"""

    @classmethod
    def choice(self, server_list, **kwargs):
        # 随便获取一个节点做匹配
        node = random.choice(server_list)
        if node is None:
            return BalanceStrategy.choice(server_list)
        else:
            return node


# RandomLoadBalance:随机负载均衡。随机的选择一个。是Dubbo的默认负载均衡策略。
# RoundRobinLoadBalance:轮询负载均衡。轮询选择一个。
# LeastActiveLoadBalance:最少活跃调用数，相同活跃数的随机。活跃数指调用前后计数差。使慢的 Provider 收到更少请求，因为越慢的 Provider 的调用前后计数差会越大。
# ConsistentHashLoadBalance:一致性哈希负载均衡。相同参数的请求总是落在同一台机器上。
# 需要实时知道活跃度（定时刷新）
# 最少活跃调用数负载均衡：每个服务维护一个活跃数计数器。当A机器开始处理请求，该计数器加1，此时A还未处理完成。若处理完毕则计数器减1。而B机器接受到请求后很快处理完毕。那么A,B的活跃数分别是1，0。当又产生了一个新的请求，则选择B机器去执行(B活跃数最小)，这样使慢的机器A收到少的请求

class RandomLoadBalance(BalanceStrategy):
    """过程负载均衡策略"""

    @classmethod
    def choice(self, server_list, **kwargs):
        # 随便获取一个节点做匹配
        node = random.choice(server_list)
        if node is None:
            return BalanceStrategy.choice(server_list)
        else:
            return node


class ProcssBalanceStrategy(BalanceStrategy):
    """过程负载均衡策略"""
    pass


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
