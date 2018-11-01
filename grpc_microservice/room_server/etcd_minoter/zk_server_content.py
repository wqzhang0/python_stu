import datetime
import pprint

"""
存放服务节点上下文
"""


class ServerContent():
    SERVER_LIST = {}
    last_update_time = None

    @staticmethod
    def get_list():
        if ServerContent.last_update_time is None or (
                datetime.datetime.now() - ServerContent.last_update_time).total_seconds() > 30:
            ServerContent.last_update_time = datetime.datetime.now()
            print("ServerContent 刷新服务节点--------------------start")
            pprint.pprint(ServerContent.SERVER_LIST)
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

            print("ServerContent 刷新服务节点----------------------end")
            pprint.pprint(ServerContent.SERVER_LIST)
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        return ServerContent.SERVER_LIST
