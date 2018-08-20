import uuid

import redis
import random

"""
redis 测试工具
"""
r = redis.Redis(host='127.0.0.1', db=6, port=6379, decode_responses=True)


class redisOperation:
    @classmethod
    def redis_set_str(self, key, value):
        return r.set(key, value)

    @classmethod
    def redis_set_str_time(self, key, value, day):
        seconds = day * 24 * 60 * 60
        return r.set(key, value, ex=seconds)

    @classmethod
    def redis_get(self, key):
        return r.get(key)

    @classmethod
    def redis_delete_key(self, key):
        return r.delete(key)

    @classmethod
    def get_redis(self):
        return r

    @classmethod
    def exits(self, key):
        return r.exists(key)


if __name__ == '__main__':
    """
    生成10数据 查看运行时间
    """
    rds = redisOperation.get_redis()

    for i in range(1000000):
        r.incr("ROOM")
        # r.set("TEST" + str(i), str(i))
# for i in range(10000):
#     r.get('TEST' + str(random.randint(1, 100000)))
