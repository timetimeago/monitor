# __*__coding:utf-8__*__
'''
@author: Tiehua
'''
import RedisOperate,serialize,pickle,threading,time,Data_Deal_API
class Server(object):
    def __init__(self):
        self.r1 = RedisOperate.Redis_Instance()
    
    def Listen_Data(self):
        return self.r1.Listen()
    
    def Deal_with_Pickle(self,msg):
        data = {}
        if not serialize.Flush_IP_conf_to_redis():
            print 'Flush Config to redis Failed'
            break
        if self.r1.Listen():
            print 'Begin to Monitor'
            Time = 0
        while True:    
            msg = self.r1.Listen()
            Time1 = time.time()
            Flag = Time1 - Time
    def task(self,msg,Time1,Flag):
        data = pickle.loads(msg[2])
        for key,value in data.items():
            Paramter = key.split(':')
            Service_name = Paramter[1].replace(' ','_')
            Client_Ip = Paramter[2]
            func = getattr(Data_Deal_API, Service_name)
            func(Client_Ip,value,Time1,Flag)
        
if __name__ == '__main__':
    if not serialize.Flush_IP_conf_to_redis():
        print 'Flush Config to Redis Failed'
        exit(1)
    
    r4 = Server()
    try:
        r4.Listen_Data()
    except Exception:
        print 'Listen the Redis Failed'
        exit(1)
    while True:
        msg = r4.Listen_Data()
        if msg:
            threading.Thread(target=r4.Deal_with_Pickle(msg))
        
        
    
        
    
    
    