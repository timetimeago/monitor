# __*__coding:utf-8__*__
import redis
class Redis_Instance:
    def __init__(self):
        self.handle = redis.Redis(host='114.112.153.121')
        self.publish_channel = 'fm100'
        self.subscribe_channel = 'fm100' 
    
    def Set(self,key,value):
        self.handle.set(key, value)
        
    def Get(self,key):
        return self.handle.get(key)
    
    def Publish(self,msg):
        return self.handle.publish(self.publish_channel,msg)
        
    def Listen(self):
        self.handle_l2 = self.handle.pubsub()
        self.handle_l2.subscribe(self.subscribe_channel)
        return self.handle_l2.parse_response()
    

if __name__ == '__main__':
    ww = Redis_Instance()
    ww.Set('asd','asdasd')
    print ww.Get('asd')
            