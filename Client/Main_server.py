# __*__coding:utf-8__*__
'''
@author: Tiehua
'''
import RedisOperate
import time,pickle
import threading
import Plugin_API
# Plugin.
str = getattr(Plugin_API, 'Get_Cpu_status')
client_ip='127.0.0.1'
class Client(object):
    def __init__(self):
        self.r1 = RedisOperate.Redis_Instance()
        
    def Get_conf_from_Redis(self):
        Conf = self.r1.Get('Client_Config::%s'%client_ip)
#         print Conf
        return pickle.loads(Conf)
    def Get_plugin_interval_from_conf(self):
        self.Conf_List = {}
        self.Conf_List = self.Get_conf_from_Redis()
        while True:
            temp = {}
            for service_name,val in self.Conf_List['service'].items():
                plugin_name,interval,last_check,temp = val
                if time.time() - last_check >= interval:
                    t = threading.Thread(target=self.run,args=[service_name,plugin_name])
                    t.start()
                    self.Conf_List['service'][service_name][2] = time.time()
    def run(self,service_name,plugin_name):
        func = getattr(Plugin_API,plugin_name)
        result = {'Monitor:%s:%s'%(service_name,client_ip):func()}
        self.r1.Publish(pickle.dumps(result))
if __name__ == '__main__':
    r3 = Client()
#     print r3.Get_conf_from_Redis()
    r3.Get_plugin_interval_from_conf()
