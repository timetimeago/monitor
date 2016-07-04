# __*__coding:utf-8__*__
'''
@author: Tiehua
'''
import RedisOperate,serialize,pickle,threading,time,Data_Deal_API
class Server(object):
    def __init__(self):
        self.r1 = RedisOperate.Redis_Instance()

    
    def Deal_with_Pickle(self):
        if not serialize.Flush_IP_conf_to_redis():
            print 'Flush Config to redis Failed'
            exit(1)
        if self.r1.Listen():
            print 'Begin to Monitor'
            self.Time = time.time()
        while True:    
            msg = self.r1.Listen()
            Time1 = time.time()
            t = threading.Thread(target=self.task,args=(msg,Time1,))
            t.start()
    def task(self,msg,Time1):
        data = {}
        data = pickle.loads(msg[2])
       # print data
        for key,value in data.items():
            Paramter = key.split(':')
            Service_name = Paramter[1]
            Client_Ip = Paramter[2]
            func = getattr(Data_Deal_API, Service_name)
            self.Time = func(Client_Ip,value,Time1,self.Time)
if __name__ == '__main__':
    S1 = Server()
    S1.Deal_with_Pickle()
