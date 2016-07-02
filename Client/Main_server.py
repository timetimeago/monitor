# __*__coding:utf-8__*__
'''
@author: Tiehua
'''
import RedisOperate
import time,pickle
class Client(object):
    def __init__(self):
        r1 = RedisOperate.Redis_Instance()
        