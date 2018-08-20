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


class zkWatch():

    def __init__(self, zk, biz_path, callback, _data):
        super().__init__()
        self.biz_path = biz_path
        self.zk = zk
        self.handler = callback
        self._data = _data

        self.acquire()

    def acquire(self):
        """
        这里设置节点 并且监听
        """
        # 创建子节点
        self.node_path = self.zk.create("/".join([self.biz_path, ""]), sequence=True, ephemeral=True, makepath=True)
        self.node_number = int(self.node_path.split("/")[-1])

        self.handler_event()

    def handler_event(self):
        # 判断是否是最小节点
        is_min, pre_node = self.getMinNode()
        if is_min:
            try:
                self.handler(self._data)
            finally:
                self.release()
        else:
            # 监听节点
            self.watch_node(pre_node)

    def watch_pre_node(self, event):
        # event
        self.handler_event()

    def watch_node(self, pre_node):
        """
        监听上一个节点
        """
        _watch_node = self.zk.exists(pre_node, watch=self.watch_pre_node)
        if _watch_node == None:
            self.handler_event()
        # print("监听上一个节点 %s" % pre_node)
        # print(type(_watch_node))
        #
        # _rand = random.randint(0, 1)
        # if _rand:
        #     time.sleep(4)
        #     self.release()

    def release(self):
        """
        释放节点
        """
        self.zk.delete(self.node_path)
        # print("释放节点 %s" % self.node_path)

    def getMinNode(self):
        node_list = self.zk.get_children(self.biz_path, )
        # print(len(node_list))
        sort_list = []
        for node_child in node_list:
            sort_list.append(int(node_child))
        sort_list.sort()
        pre = True
        if self.node_number == sort_list[0]:
            # 获得锁
            # print("获得锁")
            return True, ""
        else:
            # print(reverse)
            # if reverse:
            sort_list.reverse()
            for index, value in enumerate(sort_list):
                if value < self.node_number:
                    pre = value
                    break
                # if pre is None:
                #     pre = sort_list[-1]
            # else:
            #     for index, value in enumerate(sort_list):
            #         if value >= self.node_number:
            #             pre = sort_list[index - 1]
            #             break
            #     # if pre is None:
            #     #     pre = sort_list[-1]
            pre = str(pre).zfill(10)
            return False, "/".join([self.biz_path, pre])
