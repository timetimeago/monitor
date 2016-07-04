# __*__coding:utf-8__*__
'''
@author: Tiehua
'''
import pickle,RedisOperate
from All_host_were_Monitored import Monitor_group

def Get_Client_Request(client_ip):
    Service = {
           'service':{}
           }
    Service_List = {}
    for group in Monitor_group:
        if client_ip in group.host:
            Service_List.update(group.Monitor_mod)
#     Service_List = set(Service_List)
    for service,value in Service_List.items():
        service = service()
        service.interval = value
        Service['service'][service.name] = [
                                            service.plugin_name,
                                            service.interval,
                                            0,
service.trigger,
                                            ]
#         print service.plugin_name,service.interval
    return Service

def Flush_IP_conf_to_redis():
    r1 = RedisOperate.Redis_Instance()
    host_ip = []
    for group in Monitor_group:
        host_ip.extend(group.host)
    host_ip = set(host_ip)
    for Each in host_ip:
        key = 'Client_Config::%s'%Each
        r1.Set(key, pickle.dumps(Get_Client_Request(Each)))
    return True
def Get_data_from_redis():
    r2 = RedisOperate.Redis_Instance()
    
if __name__ == '__main__':
#     for i in Monitor_group:
#         print i.interval
#     Get_Client_Request('127.0.0.1')
    Flush_IP_conf_to_redis()
