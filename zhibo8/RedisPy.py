# coding=utf-8
'''

Python连接并操作Redis

'''
import redis


class Python_redis():
    def __init__(self, host, port, password):
        self.host = host
        self.port = port
        self.password = password

    # 连接redis
    def connRedis(self):
        pool = redis.ConnectionPool(host=self.host, port=self.port)

        r = redis.StrictRedis(connection_pool=pool)

        # r = redis.StrictRedis(self.host, self.port, decode_responses=True)

        data = r.get('gender')

        print(data)


_redis = Python_redis('localhost', 6379, '1210933445')
_redis.connRedis()
