class locker:

    def __init__(self):
        print("locker.__init__() should be not called.")

    @staticmethod
    def acquire(node_path):
        print("locker.acquire() called :%s" % node_path)

    @staticmethod
    def release(node_path):
        print("locker.release() called :%s" % node_path)


def w2(room_path, path):
    def decorator(func):
        # @functools.wrap(func)
        def wrapper(event):
            return func(room_path, path, event.path, event.state, event.type)

        return wrapper

    return decorator


class zkWatch(locker):
    # biz_path = None
    # node_number = None
    # callback = None

    def __init__(self, zk, biz_path, callback):
        super().__init__()
        self.biz_path = biz_path
        self.zk = zk
        self.handler = callback

    #
    # @staticmethod
    # def filter_lock(zk, tmp_node, ROOT, ROOM_ID, handler):
    #     suffix_num = int(tmp_node.split('/')[-1])
    #     room_path = "/".join([ROOT, ROOM_ID])
    #     node_list = zk.get_children(room_path)
    #     sort_list = []
    #     for node_child in node_list:
    #         sort_list.append(int(node_child))
    #     sort_list.sort()
    #     if suffix_num == sort_list[0]:
    #         # 获得锁
    #         print("获得锁")
    #         """执行任务 2s删除自己节点"""
    #         handler()
    #     else:
    #         pre = None
    #         for index, value in enumerate(sort_list):
    #             if value >= suffix_num:
    #                 pre = sort_list[index - 1]
    #                 break
    #         if pre is None:
    #             pre = sort_list[-1]
    #         pre = str(pre).zfill(10)
    #         print("监听比自己小的上一位node :%s" % pre)
    #         zk.exists("/".join([ROOT, ROOM_ID, pre]), watch=w2(room_path, tmp_node)(watch_pre_node))
    #         print(node_list)
    #         # 创建房间
    #         if not zk.exists("/".join([ROOT, ROOM_ID])):
    #             zk.create("/".join([ROOT, ROOM_ID]))

    def acquire(self):
        """
        这里设置节点 并且监听
        """

        suffix_num = self.node_number
        room_path = self.biz_path

        # 创建子节点
        self.node_path = self.zk.create("/".join([room_path, ""]), sequence=True, ephemeral=True)
        self.node_number = self.node_path.split("/")[-1]

        # 判断是否是最小节点
        is_min, pre_node = self.getMinNode()
        if is_min:
            self.handler()
        else:
            # 监听节点
            self.watch_node(pre_node)

    def watch_pre_node(self):
        pass

    def watch_node(self, pre_node):
        """
        监听上一个节点
        """
        self.zk.exists(pre_node, watch=self.watch_pre_node)

    def release(self):
        """
        释放节点
        """
        pass

    def getMinNode(self):
        node_list = self.zk.get_children(self.biz_path)

        sort_list = []
        for node_child in node_list:
            sort_list.append(int(node_child))
        sort_list.sort()
        pre = True
        if self.node_number == sort_list[0]:
            # 获得锁
            print("获得锁")
            return True, pre
        else:
            for index, value in enumerate(sort_list):
                if value >= self.node_number:
                    pre = sort_list[index - 1]
                    break
            if pre is None:
                pre = sort_list[-1]
            pre = str(pre).zfill(10)
            return False, pre
